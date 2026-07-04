from dataclasses import dataclass
from models.flight import Flight

@dataclass
class Prediction:
    prediction_id: int
    user_id: int
    flight: Flight
    predicted_fare: float
    prediction_time: str

    def display_prediction(self):
        self.flight.display_details()
        print("\nPrediction Details\n", "-" * 30)
        print(f"Predicted Fare : ₹{self.predicted_fare}")
        print(f"Prediction Time : {self.prediction_time}")