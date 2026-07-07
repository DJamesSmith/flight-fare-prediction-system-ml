# Responsibilities:
# ✔ Load dataset
# ✔ Validate dataset
# ✔ Clean dataset
# ✔ Feature engineering
# ✔ Save cleaned dataset
# ✔ Save feature dataset

import pandas as pd
from utilities.constants import DATASET_PATH, CLEANED_DATASET_PATH, FEATURE_DATASET_PATH
from utilities.file_handler import FileHandler
from utilities.logger import ApplicationLogger
from validation.dataset_validation import DatasetValidation

class PreprocessingService:
    def __init__(self):
        self.dataframe: pd.DataFrame = pd.DataFrame()

    def load_dataset(self) -> pd.DataFrame:
        ApplicationLogger.info("Loading dataset.")
        self.dataframe = FileHandler.read_csv(DATASET_PATH)
        ApplicationLogger.info(f"Dataset loaded successfully. Records: {len(self.dataframe)}")
        return self.dataframe

    def rename_columns(self):
        # Kaggle Column: Internal Column
        column_mapping = {
            "Date_of_Journey": "Journey_Date",
            "Dep_Time": "Departure_Time",
            "Additional_Info": "Additional_Information",
            "Price": "Fare"
        }
        self.dataframe.rename(columns=column_mapping, inplace=True)
        ApplicationLogger.info("Dataset columns renamed successfully.")

    def validate_dataset(self):
        DatasetValidation.validate_dataset_exists(DATASET_PATH)
        DatasetValidation.validate_empty_dataset(self.dataframe)
        DatasetValidation.validate_required_columns(self.dataframe)
        DatasetValidation.validate_missing_values(self.dataframe)
        DatasetValidation.validate_duplicate_rows(self.dataframe)
        ApplicationLogger.info("Dataset validation completed successfully.")

    # -------------------- DATA CLEANING --------------------
    # orchestrates smaller cleaning steps
    def clean_dataset(self):
        self.handle_missing_values()
        self.remove_duplicates()
        self.trim_whitespace()
        self.standardize_columns()
        self.convert_data_types()
        ApplicationLogger.info("Dataset cleaned successfully.")

    def handle_missing_values(self):
        self.dataframe.dropna(inplace=True)
        ApplicationLogger.info("Missing values handled successfully.")

    def remove_duplicates(self):
        self.dataframe.drop_duplicates(inplace=True)
        ApplicationLogger.info("Duplicate rows removed.")

    def trim_whitespace(self):
        object_columns = self.dataframe.select_dtypes(include="object").columns
        self.dataframe[object_columns] = (self.dataframe[object_columns].apply(lambda column: column.str.strip()))
        ApplicationLogger.info("Whitespace removed successfully.")

    def standardize_columns(self):
        categorical_columns = ["Airline", "Source", "Destination", "Route", "Total_Stops", "Additional_Information"]
        for column in categorical_columns: self.dataframe[column] = (self.dataframe[column].str.strip().str.title())
        ApplicationLogger.info("Categorical columns standardized.")

    def convert_data_types(self):
        self.dataframe["Journey_Date"] = pd.to_datetime(
        self.dataframe["Journey_Date"], dayfirst=True)
        self.dataframe["Departure_Time"] = pd.to_datetime(self.dataframe["Departure_Time"], format="%H:%M")
        self.dataframe["Arrival_Time"] = pd.to_datetime(self.dataframe["Arrival_Time"], format="mixed", dayfirst=True)
        self.dataframe["Fare"] = self.dataframe["Fare"].astype(float)
        ApplicationLogger.info("Column data types converted successfully.")

    # -------------------------------------------------------

    def save_cleaned_dataset(self):
        FileHandler.save_csv(self.dataframe, CLEANED_DATASET_PATH)
        ApplicationLogger.info(f"Cleaned dataset saved to {CLEANED_DATASET_PATH}")

    def save_feature_dataset(self):
        FileHandler.save_csv(self.dataframe, FEATURE_DATASET_PATH)
        ApplicationLogger.info(f"Feature dataset saved to {FEATURE_DATASET_PATH}")