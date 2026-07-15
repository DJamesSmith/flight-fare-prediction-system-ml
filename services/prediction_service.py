# ✔ Load trained model
# ✔ Encode user input
# ✔ Predict fare
# ✔ Save prediction
# ✔ View prediction history

import pandas as pd
from sklearn.base import RegressorMixin
from sklearn.preprocessing import OrdinalEncoder
from models.user import User
from models.flight import Flight
from models.prediction import Prediction
from repositories.prediction_repository import PredictionRepository
from utilities.constants import MODEL_PATH, ENCODER_PATH
from utilities.file_handler import FileHandler
from utilities.feature_engineering import FeatureTransformer
from utilities.logger import ApplicationLogger

class PredictionService:
    def __init__(self):
        self.prediction_repository: PredictionRepository = PredictionRepository()
        self.model: RegressorMixin | None = None
        self.encoder: OrdinalEncoder | None = None
        self.feature_columns: list[str] = []

    def _load_model(self) -> None:
        if self.model is not None:
            return

        if not FileHandler.file_exists(MODEL_PATH):
            raise FileNotFoundError("No trained model found.")
        if not FileHandler.file_exists(ENCODER_PATH):
            raise FileNotFoundError("Encoder not found.")

        self.model = FileHandler.load_pickle(MODEL_PATH)
        encoder_data: dict[str, object] = FileHandler.load_pickle(ENCODER_PATH)
        self.encoder = encoder_data["encoder"]
        self.feature_columns = encoder_data["feature_columns"]

    # No categorical_columns to loop through, encoder handles all the columns
    def encode_features(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        categorical_columns: list[str] = ["Airline", "Source", "Destination", "Route", "Additional_Information"]
        dataframe[categorical_columns] = self.encoder.transform(dataframe[categorical_columns])
        return dataframe

    def create_prediction(self, user_id: int, flight: Flight) -> Prediction:
        self._load_model()
        dataframe = pd.DataFrame([flight.to_dictionary()])
        dataframe = FeatureTransformer.feature_transform(dataframe)
        dataframe = self.encode_features(dataframe)
        dataframe = dataframe[self.feature_columns]
        predicted_fare = float(self.model.predict(dataframe)[0])
        prediction = Prediction(user_id=user_id, flight_id=flight.flight_id, predicted_fare=round(predicted_fare, 2))
        prediction = self.prediction_repository.create_prediction(prediction)
        ApplicationLogger.info("Prediction generated successfully.")
        return prediction

    def get_prediction_by_id(self, prediction_id: int) -> Prediction | None:
        return (self.prediction_repository.get_prediction_by_id(prediction_id))

    def get_prediction_history(self, user_id: int) -> list[Prediction]:
        return (self.prediction_repository.get_predictions_by_user(user_id))

    def delete_prediction(self, current_user: User, prediction_id: int) -> bool:
        prediction: Prediction | None = self.get_prediction_by_id(prediction_id)
        if prediction is None:
            return False

        # Ownership check for deleting predictions. Normal users may delete only their own predictions.
        if (current_user.role != User.ADMIN and prediction.user_id != current_user.user_id):
            raise PermissionError("You cannot delete another user's prediction.")
        return self.prediction_repository.delete_prediction(prediction_id)