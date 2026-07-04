from dataclasses import dataclass
from models.flight import Flight
from datetime import datetime

@dataclass
class Prediction:
    prediction_id: int | None = None
    user_id: int = 0
    flight_id: int = 0
    predicted_fare: float = 0.0
    prediction_time: datetime | None = None

    def display_prediction(self):
        self.flight.display_details()
        print("\nPrediction Details\n", "-" * 30)
        print(f"Predicted Fare : ₹{self.predicted_fare}")
        print(f"Prediction Time : {self.prediction_time}")