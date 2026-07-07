# Train, save, load ML models:
# ✔ Load feature dataset
# ✔ Split dataset
# ✔ Train Linear Regression
# ✔ Train Decision Tree
# ✔ Train Random Forest
# ✔ Evaluate Models
# ✔ Save Best Model

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.base import RegressorMixin
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

class TrainingService:
    def __init__(self):
        self.dataframe: pd.DataFrame = pd.DataFrame()
        self.x_train: pd.DataFrame | None = None
        self.x_test: pd.DataFrame | None = None
        self.y_train: pd.Series | None = None
        self.y_test: pd.Series | None = None
        self.encoder: dict[str, LabelEncoder] = {}
        self.models: dict[str, RegressorMixin] = {}
        self.best_model: RegressorMixin | None = None
        self.metrics: pd.DataFrame = pd.DataFrame()

    def load_feature_dataset(self):
        pass

    def encode_features(self):
        pass

    def split_dataset(self):
        pass

    def train_linear_regression(self):
        pass

    def train_decision_tree(self):
        pass

    def train_random_forest(self):
        pass

    def evaluate_models(self):
        pass

    def save_best_model(self):
        pass

    def save_encoder(self):
        pass