# ✔ Save Prediction
# ✔ Get Prediction By ID
# ✔ Get Prediction History
# ✔ Delete Prediction

from psycopg2 import Error
from database.db_connection import DatabaseConnection
from models.prediction import Prediction
from utilities.logger import ApplicationLogger
from database.queries import (
    INSERT_PREDICTION,
    GET_PREDICTION_BY_ID,
    GET_ALL_PREDICTIONS,
    UPDATE_PREDICTION,
    DELETE_PREDICTION,
    GET_PREDICTIONS_BY_USER,
)

class PredictionRepository:
    # Convert database row into Prediction model
    def _map_row_to_prediction(self, row: tuple) -> Prediction:
        return Prediction(
                prediction_id=row[0],
                user_id=row[1],
                flight_id=row[2],
                predicted_fare=float(row[3]),
                prediction_time=row[4],
            )

    # Save a prediction record
    def create_prediction(self, prediction: Prediction) -> Prediction:
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(INSERT_PREDICTION, (prediction.user_id, prediction.flight_id, prediction.predicted_fare,))
                result = db.cursor.fetchone()
                prediction.prediction_id = result[0]
                prediction.prediction_time = result[1]
                ApplicationLogger.info(f"Prediction created successfully. Prediction ID: {prediction.prediction_id}")
                return prediction
        except Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to create prediction: {error}")

    # Retrieve a prediction using the prediction ID
    def get_prediction_by_id(self, prediction_id: int) -> Prediction | None:
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(GET_PREDICTION_BY_ID, (prediction_id,),)
                row = db.cursor.fetchone()
                if row:
                    return self._map_row_to_prediction(row)
                return None
        except Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to retrieve prediction: {error}")

    # Retrieve all prediction records
    def get_all_predictions(self) -> list[Prediction]:
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(GET_ALL_PREDICTIONS)
                rows = db.cursor.fetchall()
                return [self._map_row_to_prediction(row) for row in rows ]
        except Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to retrieve predictions: {error}")

    # Update an existing prediction record
    def update_prediction(self, prediction: Prediction) -> bool:
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(UPDATE_PREDICTION, (prediction.predicted_fare, prediction.prediction_id,))
                if db.cursor.rowcount == 0:
                    return False
                ApplicationLogger.info(f"Prediction ID {prediction.prediction_id} updated successfully.")
                return True
        except Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to update prediction: {error}")

    # Delete a prediction record
    def delete_prediction(self, prediction_id: int) -> bool:
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(DELETE_PREDICTION, (prediction_id,))
                if db.cursor.rowcount == 0:
                    return False
                ApplicationLogger.info(f"Prediction ID {prediction_id} deleted successfully.")
                return True
        except Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to delete prediction: {error}")

    # Retrieve all predictions made by a specific user
    def get_predictions_by_user(self, user_id: int) -> list[Prediction]:
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(GET_PREDICTIONS_BY_USER, (user_id,))
                rows = db.cursor.fetchall()
                return [self._map_row_to_prediction(row) for row in rows ]
        except Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to retrieve prediction history: {error}")