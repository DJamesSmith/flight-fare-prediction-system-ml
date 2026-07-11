# Responsibilities:
# Predict Fare
# Batch Prediction
# Prediction History
# Delete Prediction

from models.user import User
from models.flight import Flight
from models.prediction import Prediction

from services.flight_service import FlightService
from services.prediction_service import PredictionService


class PredictionController:
    def __init__(self):
        self.flight_service: FlightService = FlightService()
        self.prediction_service: PredictionService = PredictionService()

    # Predict fare for one flight
    def predict_fare(self, current_user: User):
        try:
            flight_id: int = int(input("Enter Flight ID : "))
            flight: Flight | None = self.flight_service.get_flight_by_id(flight_id)
            if flight is None:
                print("\nFlight not found.")
                return
            prediction: Prediction = self.prediction_service.create_prediction(current_user.user_id, flight)
            print("\nPrediction Generated Successfully\n")
            prediction.display_prediction()
        except Exception as error:
            print(error)

    # Batch Prediction Placeholder
    def batch_prediction(self):
        print("\nBatch Prediction will be implemented later.")

    # View Prediction History
    def view_prediction_history(self, current_user: User):
        try:
            predictions: list[Prediction] = self.prediction_service.get_prediction_history(current_user.user_id)
            if not predictions:
                print("\nNo prediction history found.")
                return
            print()
            for prediction in predictions:
                print("-" * 40)
                prediction.display_prediction()
        except Exception as error:
            print(error)

    # Delete Prediction
    def delete_prediction(self, current_user: User):
        try:
            prediction_id: int = int(input("Prediction ID : "))
            success: bool = self.prediction_service.delete_prediction(current_user, prediction_id)
            if success:
                print("\nPrediction deleted successfully.")
            else:
                print("\nPrediction not found.")
        except PermissionError as error:
            print(error)
        except Exception as error:
            print(error)