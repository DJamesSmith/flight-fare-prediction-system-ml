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


class PreprocessingService():
    def __init__(self):
        pass

    def rename_columns():
        # | Kaggle Column   | Internal Column        |
        # | --------------- | ---------------------- |
        # | Date_of_Journey | Journey_Date           |
        # | Dep_Time        | Departure_Time         |
        # | Arrival_Time    | Arrival_Time           |
        # | Price           | Fare                   |
        # | Additional_Info | Additional_Information |

        pass

    def load_dataset(self):
        pass

    def validate_dataset(self):
        pass

    # orchestrate smaller cleaning steps.
    def clean_dataset(self):
        pass

    def handle_missing_values():
        pass

    def remove_duplicates():
        pass

    def standardize_columns():
        pass

    def feature_engineering(self):
        pass

    def save_cleaned_dataset(self):
        pass

    def save_feature_dataset(self):
        pass


# pd.read_csv() - internally opens the file, reads it, parses it, and closes it automatically.
# df.to_csv() - opens, writes, flushes, and closes the file.