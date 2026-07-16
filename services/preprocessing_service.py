# Responsibilities:
# ✔ Load dataset
# ✔ Validate dataset
# ✔ Clean dataset
# ✔ Feature engineering
# ✔ Save cleaned dataset
# ✔ Save feature dataset

import pandas as pd
from models.flight import Flight
from services.flight_service import FlightService
from utilities.constants import DATASET_PATH, CLEANED_DATASET_PATH, FEATURE_DATASET_PATH
from utilities.file_handler import FileHandler
from utilities.logger import ApplicationLogger
from utilities.feature_engineering import FeatureTransformer
from validation.dataset_validation import DatasetValidation
from decorators.execution_time import log_execution_time

class PreprocessingService:
    def __init__(self):
        self.flight_service = FlightService()
        self.cleaned_dataframe: pd.DataFrame = pd.DataFrame()
        self.feature_dataframe: pd.DataFrame = pd.DataFrame()

    def dataset_already_processed(self) -> bool:
        return self.flight_service.flights_exist()

    @log_execution_time
    def load_dataset(self) -> pd.DataFrame:
        ApplicationLogger.info("Loading dataset.")
        self.cleaned_dataframe = FileHandler.read_csv(DATASET_PATH)
        ApplicationLogger.info(f"Dataset loaded successfully. Records: {len(self.cleaned_dataframe)}")
        return self.cleaned_dataframe

    def rename_columns(self):
        # Kaggle Column: Internal Column
        column_mapping = {
            "Date_of_Journey": "Journey_Date",
            "Dep_Time": "Departure_Time",
            "Additional_Info": "Additional_Information",
            "Price": "Fare"
        }
        self.cleaned_dataframe.rename(columns=column_mapping, inplace=True)
        ApplicationLogger.info("Dataset columns renamed successfully.")

    # ----------------------------- DATA VALIDATION (start) - Validation before cleaning -----------------------------
    # Only validate things that prevent the pipeline from running.

    @log_execution_time
    def validate_dataset_structure(self):
        DatasetValidation.validate_dataset_exists(DATASET_PATH)
        DatasetValidation.validate_empty_dataset(self.cleaned_dataframe)
        DatasetValidation.validate_required_columns(self.cleaned_dataframe)

    # -------------------- DATA CLEANING (start) --------------------
    # orchestrates smaller cleaning steps
    @log_execution_time
    def clean_dataset(self):
        self.handle_missing_values()
        self.remove_duplicates()
        self.trim_whitespace()
        self.standardize_columns()
        self.convert_data_types()
        ApplicationLogger.info("Dataset cleaned successfully.")

    def handle_missing_values(self):
        self.cleaned_dataframe.dropna(inplace=True)
        ApplicationLogger.info("Missing values handled successfully.")

    def remove_duplicates(self):
        self.cleaned_dataframe.drop_duplicates(inplace=True)
        ApplicationLogger.info("Duplicate rows removed.")

    def trim_whitespace(self):
        object_columns = self.cleaned_dataframe.select_dtypes(include="object").columns
        self.cleaned_dataframe[object_columns] = (self.cleaned_dataframe[object_columns].apply(lambda column: column.str.strip()))
        ApplicationLogger.info("Whitespace removed successfully.")

    def standardize_columns(self):
        categorical_columns = ["Airline", "Source", "Destination", "Route", "Total_Stops", "Additional_Information"]
        for column in categorical_columns: self.cleaned_dataframe[column] = (self.cleaned_dataframe[column].str.strip().str.title())
        ApplicationLogger.info("Categorical columns standardized.")

    def convert_data_types(self):
        self.cleaned_dataframe["Journey_Date"] = pd.to_datetime(self.cleaned_dataframe["Journey_Date"], dayfirst=True)
        self.cleaned_dataframe["Departure_Time"] = pd.to_datetime(self.cleaned_dataframe["Departure_Time"], format="mixed")
        self.cleaned_dataframe["Arrival_Time"] = pd.to_datetime(self.cleaned_dataframe["Arrival_Time"], format="mixed", dayfirst=True)
        self.cleaned_dataframe["Fare"] = self.cleaned_dataframe["Fare"].astype(float)
        ApplicationLogger.info("Column data types converted successfully.")

    # -------------------- DATA CLEANING (end) --------------------
    # Validation after cleaning: Post-clean validation confirms the cleaning process succeeded before feature engineering and model training.
    @log_execution_time
    def validate_cleaned_dataset(self):
        DatasetValidation.validate_missing_values(self.cleaned_dataframe)
        DatasetValidation.validate_duplicate_rows(self.cleaned_dataframe)
        ApplicationLogger.info("Dataset validation completed successfully.")

    # ----------------------------- DATA VALIDATION (end) -----------------------------

    def save_cleaned_dataset(self):
        FileHandler.save_csv(self.cleaned_dataframe, CLEANED_DATASET_PATH)
        ApplicationLogger.info(f"Cleaned dataset saved to {CLEANED_DATASET_PATH}")

    @log_execution_time
    def populate_flights_table(self):
        ApplicationLogger.info(f"Populating flights table using dataframe: {self.cleaned_dataframe.columns.tolist()}")
        flights: list[Flight] = []
        for _, row in self.cleaned_dataframe.iterrows():
            flights.append(
                Flight(
                    airline=row["Airline"],
                    journey_date=row["Journey_Date"].date(),
                    source=row["Source"],
                    destination=row["Destination"],
                    route=row["Route"],
                    departure_time=row["Departure_Time"].time(),
                    arrival_time=row["Arrival_Time"].time(),
                    duration=row["Duration"],
                    total_stops=row["Total_Stops"],
                    additional_information=row["Additional_Information"],
                    fare=float(row["Fare"]),
                ))
        self.flight_service.truncate_flights()
        self.flight_service.import_flights(flights)
        ApplicationLogger.info(f"{len(flights)} flights imported into PostgreSQL.")

    @log_execution_time
    def save_feature_dataset(self):
        self.feature_dataframe = FeatureTransformer.feature_transform(self.cleaned_dataframe)           # original cleaned dataframe remains untouched
        FileHandler.save_csv(self.feature_dataframe, FEATURE_DATASET_PATH)
        ApplicationLogger.info(f"Feature dataset saved to {FEATURE_DATASET_PATH}")


# After this process it'll product 2 files for training the models:
# 1. cleaned dataset
# 2. feature dataset