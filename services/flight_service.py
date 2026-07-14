# Responsibilities:
# ✔ Get flight by ID
# ✔ View all flights
# ✔ Search flights

from models.flight import Flight
from repositories.flight_repository import FlightRepository


class FlightService:
    def __init__(self):
        self.flight_repository: FlightRepository = FlightRepository()

    def import_flights(self, flights: list[Flight]):
        self.flight_repository.insert_flights(flights)

    def truncate_flights(self):
        self.flight_repository.truncate_flights()

    def get_flight_by_id(self, flight_id: int) -> Flight | None:
        return self.flight_repository.get_flight_by_id(flight_id)

    def get_all_flights(self) -> list[Flight]:
        return self.flight_repository.get_all_flights()

    def search_flights(self, airline: str | None = None, source: str | None = None, destination: str | None = None, journey_date: str | None = None) -> list[Flight]:
        return self.flight_repository.search_flights(airline=airline, source=source, destination=destination, journey_date=journey_date)

    def flights_exist(self) -> bool:
        return self.flight_repository.flights_exist()