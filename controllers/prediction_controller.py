# Responsibilities:
# Predict Fare
# Batch Prediction
# Prediction History
# Delete Prediction
import traceback
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
        except FileNotFoundError:
            print("\nNo trained model found.\nPlease train a model first.\nAdmin Menu -> Train ML Models")
        except Exception as error:
            print(error)
            # traceback.print_exc()

    def predict_custom_fare(self, current_user: User):
        try:
            airline = input("Enter Airline : ").strip()
            journey_date = input("Enter Journey Date (DD/MM/YYYY) : ").strip()
            source = input("Enter Source : ").strip()
            destination = input("Enter Destination : ").strip()

            print(f"Before conversion date: {journey_date}")                        # 06/05/2019
            from datetime import datetime
            journey_date = datetime.strptime(journey_date, "%d/%m/%Y").date()
            print(f"After conversion date: {journey_date}")                         # 2019-05-06

            flights = self.flight_service.find_prediction_candidates(airline=airline, source=source, destination=destination, journey_date=journey_date)
            if not flights:
                print("\nNo flights found.")
                return

            if len(flights) == 1:
                prediction = (self.prediction_service.create_prediction(current_user.user_id,flights[0]))
                print("\nPrediction Generated Successfully\n")
                prediction.display_prediction()
                return
            print("\nMatching Flights\n")

            print("+----+------------+------------+----------+-----------+")
            print("| No | Departure  | Arrival    | Duration | Stops     |")
            print("+----+------------+------------+----------+-----------+")

            for index, flight in enumerate(flights, start=1):
                print(
                    f"| {index:<2} "
                    f"| {str(flight.departure_time):<10} "
                    f"| {str(flight.arrival_time):<10} "
                    f"| {flight.duration:<8} "
                    f"| {flight.total_stops:<9} |"
                )

            print("+----+------------+------------+----------+-----------+")

            choice: int = int(input("\nChoose Flight Number : "))
            if choice < 1 or choice > len(flights):
                print("\nInvalid choice.")
                return

            selected_flight = flights[choice - 1]
            prediction = self.prediction_service.create_prediction(current_user.user_id, selected_flight)
            print("\nPrediction Generated Successfully\n")
            prediction.display_prediction()
        except FileNotFoundError:
            print("\nNo trained model found.\nPlease train a model first.")
        except ValueError:
            print("\nInvalid date format.")
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

            print("\nPrediction History\n")
            print("+----+--------+--------+----------------+---------------------+")
            print("| ID | Code   | Flight | Predicted Fare | Prediction Time     |")
            print("+----+--------+--------+----------------+---------------------+")
            for prediction in predictions:
                print(
                    f"| {prediction.prediction_id:<2} "
                    f"| {prediction.prediction_code:<6} "
                    f"| {prediction.flight_id:<6} "
                    f"| ₹{prediction.predicted_fare:<13.2f} "
                    f"| {str(prediction.prediction_time):<19} |"
                )
            print("+----+--------+--------+----------------+---------------------+")
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