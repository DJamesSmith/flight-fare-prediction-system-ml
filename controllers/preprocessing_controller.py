# Responsibilities:
# 1. Load dataset
# 2. Validate dataset
# 3. Clean dataset
# 4. Save cleaned dataset
# 5. Save feature dataset

from services.preprocessing_service import PreprocessingService

class PreprocessingController:
    def __init__(self) -> None:
        self.preprocessing_service: PreprocessingService = PreprocessingService()

    def preprocess_dataset(self) -> None:
        try:
            print("\nLoading dataset...")
            self.preprocessing_service.load_dataset()

            print("Renaming dataset columns...")
            self.preprocessing_service.rename_columns()

            print("Validating dataset...")
            self.preprocessing_service.validate_dataset()

            print("Cleaning dataset...")
            self.preprocessing_service.clean_dataset()

            print("Saving cleaned dataset...")
            self.preprocessing_service.save_cleaned_dataset()

            print("Saving feature dataset...")
            self.preprocessing_service.save_feature_dataset()

            print("\nDataset preprocessing completed successfully.")
        except Exception as error:
            print(error)