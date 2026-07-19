import os
import pandas as pd
from utilities.logger import ApplicationLogger

class DatasetValidation:
    REQUIRED_COLUMNS: list[str] = [
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
        missing_columns: list[str] = [column for column in cls.REQUIRED_COLUMNS if column not in dataframe.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")

    @staticmethod
    def validate_missing_values(dataframe: pd.DataFrame):
        missing = dataframe.isnull().sum()
        missing = missing[missing > 0]

        if not missing.empty:
            ApplicationLogger.warning(f"Missing values detected.\n{missing}")
            rows = dataframe[dataframe.isnull().any(axis=1)]                    # returns "Entire bad rows" or missing values in columns / Series

            for index, row in rows.iterrows():
                missing_columns = row[row.isnull()].index.tolist()
                ApplicationLogger.warning(f"Row {index}: Missing -> {missing_columns}")
                ApplicationLogger.warning(f"Row {index} Data -> {row.to_dict()}")
            raise ValueError(f"Dataset containing missing values found:\n{missing}")

    @staticmethod
    def validate_duplicate_rows(dataframe: pd.DataFrame):
        duplicates = dataframe.duplicated().sum()
        if duplicates:
            raise ValueError(f"{duplicates} duplicate rows detected.")