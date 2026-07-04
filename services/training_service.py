# ✔ Load feature dataset
# ✔ Split dataset
# ✔ Train Linear Regression
# ✔ Train Decision Tree
# ✔ Train Random Forest
# ✔ Evaluate Models
# ✔ Save Best Model

from abc import ABC, abstractmethod

class TrainingService(ABC):
    @abstractmethod
    def load_feature_dataset(self):
        pass

    @abstractmethod
    def split_dataset(self):
        pass

    @abstractmethod
    def train_linear_regression(self):
        pass

    @abstractmethod
    def train_decision_tree(self):
        pass

    @abstractmethod
    def train_random_forest(self):
        pass

    @abstractmethod
    def evaluate_models(self):
        pass

    @abstractmethod
    def save_best_model(self):
        pass