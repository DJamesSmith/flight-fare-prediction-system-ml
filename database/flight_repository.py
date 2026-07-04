# ✔ Save Flight
# ✔ Get Flight By ID
# ✔ Get All Flights
# ✔ Delete Flight

from database.db_connection import DatabaseConnection
from models.flight import Flight
class FlightRepository():
    def _map_row_to_flight(self, row: tuple) -> Flight:
        return Flight(
            flight_id = row[0],
            airline = row[1],
            source = row[2],
            destination = row[3],
            journey_date = row[4],
            departure_time = row[5],
            arrival_time = row[6],
            duration = row[7],
            total_stops = row[8],
            additional_information = row[9],
        )

    # Insert a flight record
    def create_flight(self, flight: Flight) -> Flight:
        pass

    # Retrieve a flight using the flight ID
    def get_flight_by_id(self, flight_id: int) -> Flight | None:
        pass

    # Retrieve all flight records
    def get_all_flights(self) -> list[Flight]:
        pass

    # Update flight details
    def update_flight(self, flight: Flight) -> bool:
        pass

    # Delete a flight record
    def delete_flight(self, flight_id: int) -> bool:
        pass

    # def search_flights(airline=None, source=None, destination=None):
    def search_flights(self, airline: str | None = None, source: str | None = None, destination: str | None = None, journey_date: str | None = None) -> list[Flight]:
        pass

# Exception query for SEARCH_FLIGHTS which will be dynamic