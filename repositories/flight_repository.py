# ✔ Save Flight
# ✔ Get Flight By ID
# ✔ Get All Flights
# ✔ Delete Flight

from psycopg2 import Error
from models.flight import Flight
from utilities.logger import ApplicationLogger
from database.db_connection import DatabaseConnection
from repositories.base_repository import BaseRepository
from database.queries import (
    INSERT_FLIGHT,
    GET_FLIGHT_BY_ID,
    GET_ALL_FLIGHTS,
    SEARCH_FLIGHTS,
    DELETE_ALL_FLIGHTS,
    EXISTS_FLIGHT_CODE
)

class FlightRepository(BaseRepository):
    def insert_flights(self, flights: list[Flight]):
        try:
            with DatabaseConnection() as db:
                values: list[tuple] = []
                for flight in flights:
                    flight.flight_code = self.generate_unique_code(EXISTS_FLIGHT_CODE)
                    values.append((
                        flight.flight_code,
                        flight.airline,
                        flight.journey_date,
                        flight.source,
                        flight.destination,
                        flight.route,
                        flight.departure_time,
                        flight.arrival_time,
                        flight.duration,
                        flight.total_stops,
                        flight.additional_information,
                        flight.fare,
                    ))
                db.cursor.executemany(INSERT_FLIGHT, values)
                ApplicationLogger.info(f"{len(flights)} flights inserted successfully.")
        except Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to insert flights: {error}")

    # Convert a database row into a Flight model
    def _map_row_to_flight(self, row: tuple) -> Flight:
        return Flight(
            flight_id = row[0],
            flight_code=row[1],
            airline = row[2],
            journey_date = row[3],
            source = row[4],
            destination = row[5],
            route = row[6],
            departure_time = row[7],
            arrival_time = row[8],
            duration = row[9],
            total_stops = row[10],
            additional_information = row[11],
            fare=row[12],
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
            query: str = SEARCH_FLIGHTS
            parameters: list = []

            if airline:
                query += " AND LOWER(airline) = LOWER(%s)"
                parameters.append(airline)
            if source:
                query += " AND LOWER(source) = LOWER(%s)"
                parameters.append(source)
            if destination:
                query += " AND LOWER(destination) = LOWER(%s)"
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

    def delete_all_flights(self):
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(DELETE_ALL_FLIGHTS)
                ApplicationLogger.info("Existing flights removed.")
        except Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to delete flights: {error}")