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
    def validate_dataset_exists(file_path: str) -> bool:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Dataset not found: {file_path}")
        return os.path.exists(file_path)                                            # Should this "return" statement be included in the method ?

    @staticmethod
    def validate_empty_dataset(dataframe: pd.DataFrame) -> bool:
        if dataframe.empty:
            raise ValueError("Dataset is empty.")
        return not dataframe.empty                                                  # Should this "return" statement be included in the method ?

    @classmethod
    def validate_required_columns(cls, dataframe: pd.DataFrame) -> bool:
        missing_columns = [column for column in cls.REQUIRED_COLUMNS if column not in dataframe.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
        return all(column in dataframe.columns for column in cls.REQUIRED_COLUMNS)   # Should this be "return missing_columns" instead or remove this line?

    @staticmethod
    def validate_missing_values(dataframe: pd.DataFrame) -> bool:
        missing = dataframe.isnull().sum()
        missing = missing[missing > 0]
        if not missing.empty:
            raise ValueError(f"Missing values found:\n{missing}")
        return dataframe.isnull().sum().sum() == 0

    @staticmethod
    def validate_duplicate_rows(dataframe: pd.DataFrame) -> bool:
        duplicates = dataframe.duplicated().sum()
        if duplicates:
            raise ValueError(f"{duplicates} duplicate rows detected.")
        return dataframe.duplicated().sum() == 0