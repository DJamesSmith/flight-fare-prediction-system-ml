# Responsibilities:
# 1. Check whether the dataset has already been processed
# 2. Confirm reprocessing if required
# 3. Execute the preprocessing pipeline

from services.preprocessing_service import PreprocessingService

class PreprocessingController:
    def __init__(self):
        self.preprocessing_service: PreprocessingService = PreprocessingService()

    def preprocess_dataset(self):
        if self.preprocessing_service.dataset_already_processed():
            print(
                "\nThe dataset has already been preprocessed.\n\n"
                "Reprocessing will:\n"
                "- Delete all existing flight records\n"
                "- Delete all prediction records\n"
                "- Rebuild the cleaned dataset\n"
                "- Rebuild the feature dataset\n"
                "- Repopulate the flights table\n\n"
                "Do you want to continue?\n"
                "1. Yes\n"
                "2. No\n")

            try:
                ch = int(input("Enter your choice : "))
            except ValueError:
                print("\nPlease enter a valid choice.")
                return

            match ch:
                case 1: 
                    print("\nDataset preprocessing cancelled.")
                    return
                case 2:
                    print("\nInvalid choice.")
                    return
        self._run_preprocessing_pipeline()

    def _run_preprocessing_pipeline(self):
        try:
            print("\nLoading dataset...")
            self.preprocessing_service.load_dataset()

            print("Renaming dataset columns...")
            self.preprocessing_service.rename_columns()

            print("Validating dataset structure...")
            self.preprocessing_service.validate_dataset_structure()

            print("Cleaning dataset...")
            self.preprocessing_service.clean_dataset()

            print("Validating cleaned dataset...")
            self.preprocessing_service.validate_cleaned_dataset()

            print("Saving cleaned dataset...")
            self.preprocessing_service.save_cleaned_dataset()

            print("Populating flights table...")
            self.preprocessing_service.populate_flights_table()

            print("Saving feature dataset...")
            self.preprocessing_service.save_feature_dataset()

            print("\nDataset preprocessing completed successfully.")
        except Exception as error:
            print(error)