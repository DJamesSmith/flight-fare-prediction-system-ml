# ✔ Save Prediction
# ✔ Get Prediction By ID
# ✔ Get Prediction History
# ✔ Delete Prediction

from abc import abstractmethod

from database.base_repository import BaseRepository


class PredictionRepository(BaseRepository):

    @abstractmethod
    def insert(self):
        # Save a prediction record.
        pass

    @abstractmethod
    def find_by_id(self):
        # Retrieve a prediction using the prediction ID.
        pass

    @abstractmethod
    def find_all(self):
        # Retrieve all prediction records.
        pass

    @abstractmethod
    def update(self):
        # Update an existing prediction record.
        pass

    @abstractmethod
    def delete(self):
        # Delete a prediction record.
        pass

    @abstractmethod
    def find_by_user(self):
        # Retrieve all predictions made by a specific user.
        pass