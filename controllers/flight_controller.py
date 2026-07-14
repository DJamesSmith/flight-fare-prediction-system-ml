# Responsibilities:
# 1. View Flights
# 2. Search Flights
# 3. Import Dataset (Admin)

from models.flight import Flight
from services.flight_service import FlightService

class FlightController:
    def __init__(self):
        self.flight_service: FlightService = FlightService()

    def view_flights(self):
        try:
            flights: list[Flight] = self.flight_service.get_all_flights()
            if not flights:
                print("\nNo flights available.")
                return

            print("\n" + "-" * 180)
            print(
                f"{'ID':<5}"
                f"{'Airline':<20}"
                f"{'Journey Date':<15}"
                f"{'Source':<15}"
                f"{'Destination':<15}"
                f"{'Departure':<12}"
                f"{'Arrival':<12}"
                f"{'Stops':<12}"
                f"{'Fare (₹)':>12}"
            )
            print("-" * 180)

            for flight in flights:
                print(
                    f"{flight.flight_id:<5}"
                    f"{flight.airline:<20}"
                    f"{str(flight.journey_date):<15}"
                    f"{flight.source:<15}"
                    f"{flight.destination:<15}"
                    f"{str(flight.departure_time):<12}"
                    f"{str(flight.arrival_time):<12}"
                    f"{flight.total_stops:<12}"
                    f"{flight.fare:>12.2f}"
                )
            print("-" * 180)
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
            print("\nLeave a field blank to ignore it.\n")              # ??
            airline: str | None = input("Airline : ").strip() or None
            source: str | None = input("Source : ").strip() or None
            destination: str | None = input("Destination : ").strip() or None
            journey_date: str | None = input("Journey Date (DD/MM/YYYY) : ").strip() or None
            flights: list[Flight] = self.flight_service.search_flights(airline=airline, source=source, destination=destination, journey_date=journey_date)

            if not flights:
                print("\nNo matching flights found.")
                return

            print(f"\n{len(flights)} flight(s) found.\n")
            print(f"\n{len(flights)} flight(s) found.\n")
            print("+----+--------+----------------------+------------+-------------+------------+------------+----------+-----------+")
            print("| ID | Code   | Airline              | Source     | Destination | Departure  | Arrival    | Duration | Stops     |")
            print("+----+--------+----------------------+------------+-------------+------------+------------+----------+-----------+")

            for flight in flights:
                print(
                    f"| {flight.flight_id:<4} "
                    f"| {flight.flight_code:<6} "
                    f"| {flight.airline:<20} "
                    f"| {flight.source:<10} "
                    f"| {flight.destination:<11} "
                    f"| {str(flight.departure_time):<10} "
                    f"| {str(flight.arrival_time):<10} "
                    f"| {flight.duration:<8} "
                    f"| {flight.total_stops:<9} |"
                )
            print("+----+--------+----------------------+------------+-------------+------------+------------+----------+-----------+")
        except Exception as error:
            print(error)