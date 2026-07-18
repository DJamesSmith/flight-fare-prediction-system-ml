# ✔ Save Flight
# ✔ Get Flight By ID
# ✔ Get All Flights
# ✔ Delete Flight

from psycopg2 import Error
from models.flight import Flight
from utilities.logger import ApplicationLogger
from database.db_connection import DatabaseConnection
from repositories.base_repository import BaseRepository
from decorators.execution_time import log_execution_time
from database.queries import (
    INSERT_FLIGHT,
    GET_FLIGHT_BY_ID,
    GET_ALL_FLIGHTS,
    SEARCH_FLIGHTS,
    TRUNCATE_FLIGHTS,
    EXISTS_FLIGHT_CODE,
    COUNT_FLIGHTS,
    SEARCH_FLIGHTS_FOR_PREDICTION
)

class FlightRepository(BaseRepository):
    @log_execution_time
    def insert_flights(self, flights: list[Flight]):
        try:
            with DatabaseConnection() as db:
                generated_codes: list[str] = self.generate_bulk_codes(EXISTS_FLIGHT_CODE, len(flights))
                values: list[tuple] = []
                for flight, code in zip(flights, generated_codes):
                    flight.flight_code = code
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

    # create_custom_prediction
    def find_prediction_candidates(self, airline: str, source: str, destination: str, journey_date: str) -> list[Flight]:
        try:
            with DatabaseConnection() as db:
                # print("\nSearching with:")
                # print(f"Airline      : '{airline}'")
                # print(f"Source       : '{source}'")
                # print(f"Destination  : '{destination}'")
                # print(f"Journey Date : '{journey_date}'")
                db.cursor.execute(SEARCH_FLIGHTS_FOR_PREDICTION, (airline, source, destination, journey_date))
                rows = db.cursor.fetchall()
                # print(f"Rows found: {len(rows)}")
                return [self._map_row_to_flight(row) for row in rows]
        except Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to search flights: {error}")

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

    def flights_exist(self) -> bool:
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(COUNT_FLIGHTS)
                return db.cursor.fetchone()[0] > 0
        except Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to determine whether flights exist: {error}")

    def truncate_flights(self):
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(TRUNCATE_FLIGHTS)
                ApplicationLogger.info("Flights table truncated successfully.")
        except Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to truncate flights table: {error}")