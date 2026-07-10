# Responsibilities:
# 1. View Flights
# 2. Search Flights
# 3. Import Dataset (Admin)

from models.flight import Flight
from services.flight_service import FlightService


class FlightController:
    def __init__(self) -> None:
        self.flight_service: FlightService = FlightService()

    def view_flights(self):
        try:
            flights: list[Flight] = self.flight_service.get_all_flights()
            if not flights:
                print("\nNo flights available.")
                return
            for flight in flights:
                print("-" * 50)
                flight.display_details()
        except Exception as error:
            print(error)

    def view_flight_by_id(self):
        try:
            flight_id: int = int(input("Flight ID : "))
            flight: Flight | None = (self.flight_service.get_flight_by_id(flight_id))
            if flight is None:
                print("\nFlight not found.")
                return
            flight.display_details()
        except Exception as error:
            print(error)

    def search_flights(self):
        try:
            print("\nLeave a field blank to ignore it.\n")
            airline: str | None = input("Airline : ").strip() or None
            source: str | None = input("Source : ").strip() or None
            destination: str | None = input("Destination : ").strip() or None
            journey_date: str | None = input("Journey Date (DD/MM/YYYY) : ").strip() or None
            flights: list[Flight] = self.flight_service.search_flights(airline=airline, source=source, destination=destination, journey_date=journey_date)

            if not flights:
                print("\nNo matching flights found.")
                return

            print(f"\n{len(flights)} flight(s) found.\n")
            for flight in flights:
                print("-" * 50)
                flight.display_details()
        except Exception as error:
            print(error)