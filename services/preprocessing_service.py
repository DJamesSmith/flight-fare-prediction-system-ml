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
    def load_dataset(self):
        pass

    def validate_dataset(self):
        pass

    def clean_dataset(self):
        pass

    # def preprocess_input():
    #     pass

    def feature_engineering(self):
        pass

    def save_cleaned_dataset(self):
        pass

    def save_feature_dataset(self):
        pass