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
from sklearn.preprocessing import OrdinalEncoder
from sklearn.base import RegressorMixin
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from utilities.constants import FEATURE_DATASET_PATH, MODEL_PATH, ENCODER_PATH, METRICS_REPORT_PATH
from utilities.file_handler import FileHandler
from utilities.logger import ApplicationLogger

class TrainingService:
    def __init__(self):
        self.dataframe: pd.DataFrame = pd.DataFrame()
        self.x_train: pd.DataFrame | None = None
        self.x_test: pd.DataFrame | None = None
        self.y_train: pd.Series | None = None
        self.y_test: pd.Series | None = None
        self.encoder: OrdinalEncoder | None = None
        self.models: dict[str, RegressorMixin] = {}
        self.best_model: RegressorMixin | None = None
        self.metrics: pd.DataFrame = pd.DataFrame()
        self.feature_columns: list[str] = []                    # lets PredictionService know the exact order expected by the trained model

    def load_feature_dataset(self):
        self.dataframe = FileHandler.read_csv(FEATURE_DATASET_PATH)
        ApplicationLogger.info(f"Feature dataset loaded. Records: {len(self.dataframe)}")

    def encode_features(self):
        categorical_columns: list[str] = ["Airline", "Source", "Destination", "Route", "Additional_Information"]
        self.encoder = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=-1)
        self.dataframe[categorical_columns] = self.encoder.fit_transform(self.dataframe[categorical_columns])
        ApplicationLogger.info("Categorical features encoded successfully.")

    def split_dataset(self):
        x = self.dataframe.drop(columns=["Fare"])
        y = self.dataframe["Fare"]
        # "self.feature_columns" contains the list of string values from model data ["Airline", "Source",..., "Journey_Day", "Journey_Month", ...., "Duration_Minutes"]
        self.feature_columns = list(x.columns)
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        ApplicationLogger.info("Dataset split into train and test.")

    def train_linear_regression(self):
        model: LinearRegression = LinearRegression()
        model.fit(self.x_train, self.y_train )
        self.models["Linear Regression"] = model
        ApplicationLogger.info( "Linear Regression trained." )

    def train_decision_tree(self):
        model: DecisionTreeRegressor = DecisionTreeRegressor(random_state=42)
        model.fit(self.x_train, self.y_train)
        self.models["Decision Tree"] = model
        ApplicationLogger.info("Decision Tree trained.")

    def train_random_forest(self):
        model: RandomForestRegressor = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(self.x_train, self.y_train )
        self.models["Random Forest"] = model
        ApplicationLogger.info("Random Forest trained." )

    def evaluate_models(self) -> pd.DataFrame:
        report: list = []
        best_score: float = float("-inf")
        for name, model in self.models.items():
            predictions = model.predict(self.x_test)
            mae: float = mean_absolute_error(self.y_test, predictions)
            mse: float = mean_squared_error(self.y_test, predictions)
            rmse: float = mse ** 0.5
            r2 = r2_score(self.y_test, predictions)
            report.append({
                "Model": name,
                "MAE": mae,
                "MSE": mse,
                "RMSE": rmse,
                "R2 Score": r2
            })
            if r2 > best_score:
                best_score = r2
                self.best_model = model
        self.metrics = pd.DataFrame(report)
        FileHandler.save_csv(self.metrics, METRICS_REPORT_PATH)
        ApplicationLogger.info("Model evaluation completed.")
        return self.metrics

    def save_best_model(self):
        if self.best_model is None:
            raise ValueError("No trained model available.")
        FileHandler.save_pickle(self.best_model, MODEL_PATH)
        ApplicationLogger.info("Best model saved successfully.")

    def save_encoder(self):
        FileHandler.save_pickle({
                "encoder": self.encoder,
                "feature_columns": self.feature_columns
            }, ENCODER_PATH)
        ApplicationLogger.info("Encoders and feature schema saved successfully.")


# From save_encoder(), the file "encoder.pkl" will contain dictionary data.
# {
#     "encoders": {
#         "Airline": LabelEncoder(...),
#         "Source": LabelEncoder(...),
#         "Destination": LabelEncoder(...),
#         "Route": LabelEncoder(...),
#         "Additional_Information": LabelEncoder(...)
#     },
#     "feature_columns": [
#         "Airline",
#         "Source",
#         "Destination",
#         "Route",
#         "Total_Stops",
#         "Additional_Information",
#         "Journey_Day",
#         "Journey_Month",
#         "Departure_Hour",
#         "Departure_Minute",
#         "Arrival_Hour",
#         "Arrival_Minute",
#         "Duration_Minutes"
#     ]
# }

# In prediction, we'll do:
# encoders = encoder_data["encoders"]
# feature_columns = encoder_data["feature_columns"]