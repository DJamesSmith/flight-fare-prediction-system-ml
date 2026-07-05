from dataclasses import dataclass
from datetime import datetime

@dataclass
class Prediction:
    prediction_id: int | None = None
    user_id: int = 0
    flight_id: int = 0
    predicted_fare: float = 0.0
    prediction_time: datetime | None = None

    def display_prediction(self):
        print(f"Prediction ID : {self.prediction_id}")
        print(f"User ID : {self.user_id}")
        print(f"Flight ID : {self.flight_id}")
        print(f"Predicted Fare : ₹{self.predicted_fare}")
        print(f"Prediction Time : {self.prediction_time}")