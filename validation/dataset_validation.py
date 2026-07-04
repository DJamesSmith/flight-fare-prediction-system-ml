import os
import pandas as pd

REQUIRED_COLUMNS = [
    "Airline",
    "Source",
    "Destination",
    "Journey_Date",
    "Departure_Time",
    "Arrival_Time",
    "Duration",
    "Total_Stops",
    "Additional_Information",
    "Fare"
]

class DatasetValidation:
    @staticmethod
    def validate_dataset_exists(file_path: str) -> bool:
        return os.path.exists(file_path)

    @staticmethod
    def validate_empty_dataset(dataframe: pd.DataFrame) -> bool:
        return not dataframe.empty

    @classmethod
    def validate_required_columns(cls, dataframe: pd.DataFrame) -> bool:
        return all(column in dataframe.columns for column in cls.REQUIRED_COLUMNS)

    @staticmethod
    def validate_missing_values(dataframe: pd.DataFrame) -> bool:
        return dataframe.isnull().sum().sum() == 0

    @staticmethod
    def validate_duplicate_rows(dataframe: pd.DataFrame) -> bool:
        return dataframe.duplicated().sum() == 0