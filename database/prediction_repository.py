# ✔ Save Prediction
# ✔ Get Prediction By ID
# ✔ Get Prediction History
# ✔ Delete Prediction

from database.db_connection import DatabaseConnection

class PredictionRepository:
    def __init__(self):
        self.database = DatabaseConnection()

    # Save a prediction record
    def insert(self, prediction):
        pass

    # Retrieve a prediction using the prediction ID
    def find_by_id(self, prediction_id):
        pass

    # Retrieve all prediction records
    def find_all(self):
        pass

    # Update an existing prediction record
    def update(self, prediction):
        pass

    # Delete a prediction record
    def delete(self, prediction_id):
        pass

    # Retrieve all predictions made by a specific user
    def find_by_user(self, user_id):
        pass