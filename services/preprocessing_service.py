# Responsibilities:
# ✔ Load dataset
# ✔ Validate dataset
# ✔ Clean dataset
# ✔ Feature engineering
# ✔ Save cleaned dataset
# ✔ Save feature dataset

# dataset_validation.py used here
# Flow:
# load_dataset()
# ↓
# DatasetValidation.validate_dataset_exists()
# ↓
# read_csv()
# ↓
# DatasetValidation.validate_required_columns()
# ↓
# DatasetValidation.validate_missing_values()
# ↓
# DatasetValidation.validate_duplicate_rows()
# ↓
# clean_dataset()

from utilities.constants import DATASET_PATH
from utilities.file_handler import FileHandler
from utilities.logger import ApplicationLogger
from validation import DatasetValidation

class PreprocessingService():
    def __init__(self):
        pass

    def load_dataset(self):
        ApplicationLogger.info("Loading dataset.")
        self.dataframe = FileHandler.read_csv(DATASET_PATH)
        ApplicationLogger.info(f"Dataset loaded successfully. Records: {len(self.dataframe)}")
        return self.dataframe

    def rename_columns(self):
        # | Kaggle Column: Internal Column |
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
    # orchestrate smaller cleaning steps.
    def clean_dataset(self):
        pass

    def handle_missing_values(self):
        pass

    def remove_duplicates(self):
        pass

    def trim_whitespace(self):
        pass

    def standardize_columns(self):
        pass

    def convert_data_types(self):
        pass

    # -------------------------------------------------------
    def feature_engineering(self):
        # From: Journey_Date
        # create:
        #     Journey_Day
        #     Journey_Month
        pass

    def save_cleaned_dataset(self):
        pass

    def save_feature_dataset(self):
        pass


# pd.read_csv() - internally opens the file, reads it, parses it, and closes it automatically.
# df.to_csv() - opens, writes, flushes, and closes the file.