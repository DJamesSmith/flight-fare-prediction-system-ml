import os
import pandas as pd

REQUIRED_COLUMNS = [
    "Airline",
    "Journey_Date",
    "Source",
    "Destination",
    "Route",
    "Departure_Time",
    "Arrival_Time",
    "Duration",
    "Total_Stops",
    "Additional_Information",
    "Fare"
]

class DatasetValidation:
    @staticmethod
    def validate_dataset_exists(file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Dataset not found: {file_path}")

    @staticmethod
    def validate_empty_dataset(dataframe: pd.DataFrame):
        if dataframe.empty:
            raise ValueError("Dataset is empty.")

    @classmethod
    def validate_required_columns(cls, dataframe: pd.DataFrame):
        missing_columns = [column for column in cls.REQUIRED_COLUMNS if column not in dataframe.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")

    @staticmethod
    def validate_missing_values(dataframe: pd.DataFrame):
        missing = dataframe.isnull().sum()
        missing = missing[missing > 0]
        if not missing.empty:
            raise ValueError(f"Missing values found:\n{missing}")

    @staticmethod
    def validate_duplicate_rows(dataframe: pd.DataFrame):
        duplicates = dataframe.duplicated().sum()
        if duplicates:
            raise ValueError(f"{duplicates} duplicate rows detected.")