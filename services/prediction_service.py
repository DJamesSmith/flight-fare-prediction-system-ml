# ✔ Load trained model
# ✔ Encode user input
# ✔ Predict fare
# ✔ Save prediction
# ✔ View prediction history

from abc import ABC, abstractmethod

class PredictionService(ABC):
    @abstractmethod
    def load_model(self):
        pass

    @abstractmethod
    def encode_input(self):
        pass

    @abstractmethod
    def predict_fare(self):
        pass

    @abstractmethod
    def save_prediction(self):
        pass

    @abstractmethod
    def prediction_history(self):
        pass