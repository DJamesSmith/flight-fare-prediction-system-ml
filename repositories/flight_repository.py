# ✔ Save Flight
# ✔ Get Flight By ID
# ✔ Get All Flights
# ✔ Delete Flight

from psycopg2 import Error
from models.flight import Flight
from utilities.logger import ApplicationLogger
from database.db_connection import DatabaseConnection
from database.queries import (
    GET_FLIGHT_BY_ID,
    GET_ALL_FLIGHTS,
)

class FlightRepository:
    # Convert a database row into a Flight model
    def _map_row_to_flight(self, row: tuple) -> Flight:
        return Flight(
            flight_id = row[0],
            airline = row[1],
            journey_date = row[2],
            source = row[3],
            destination = row[4],
            route = row[5],
            departure_time = row[6],
            arrival_time = row[7],
            duration = row[8],
            total_stops = row[9],
            additional_information = row[10],
        )

    # Retrieve a flight using the flight ID
    def get_flight_by_id(self, flight_id: int) -> Flight | None:
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(GET_FLIGHT_BY_ID, (flight_id,))
                row = db.cursor.fetchone()
                if row:
                    return self._map_row_to_flight(row)
                return None
        except Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to retrieve flight: {error}")

    # Retrieve all flight records
    def get_all_flights(self) -> list[Flight]:
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(GET_ALL_FLIGHTS)
                rows = db.cursor.fetchall()
                return [self._map_row_to_flight(row) for row in rows]
        except Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to retrieve flights: {error}")

    # Search flights using optional filters - dynamic search - no constant query - depending on input given by user
    def search_flights(self, airline: str | None = None, source: str | None = None, destination: str | None = None, journey_date: str | None = None) -> list[Flight]:
        try:
            query = "SELECT * FROM flights WHERE 1=1"
            parameters = []

            if airline:
                query += " AND airline = %s"
                parameters.append(airline)
            if source:
                query += " AND source = %s"
                parameters.append(source)
            if destination:
                query += " AND destination = %s"
                parameters.append(destination)
            if journey_date:
                query += " AND journey_date = %s"
                parameters.append(journey_date)
            query += " ORDER BY journey_date;"

            with DatabaseConnection() as db:
                db.cursor.execute(query, tuple(parameters))
                rows = db.cursor.fetchall()
                return [self._map_row_to_flight(row) for row in rows]
        except Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to search flights: {error}")