# Responsibilities:
# ✔ Load dataset
# ✔ Validate dataset
# ✔ Clean dataset
# ✔ Feature engineering
# ✔ Save cleaned dataset
# ✔ Save feature dataset

from abc import ABC, abstractmethod

class PreprocessingService(ABC):
    @abstractmethod
    def load_dataset(self):
        pass

    @abstractmethod
    def validate_dataset(self):
        pass

    @abstractmethod
    def clean_dataset(self):
        pass

    @abstractmethod
    def feature_engineering(self):
        pass

    @abstractmethod
    def save_cleaned_dataset(self):
        pass

    @abstractmethod
    def save_feature_dataset(self):
        pass