# ✔ Save Flight
# ✔ Get Flight By ID
# ✔ Get All Flights
# ✔ Delete Flight

from psycopg2 import Error
from models.flight import Flight
from utilities.logger import ApplicationLogger
from database.db_connection import DatabaseConnection
from database.queries import (
    INSERT_FLIGHT,
    GET_FLIGHT_BY_ID,
    GET_ALL_FLIGHTS,
    UPDATE_FLIGHT,
    DELETE_FLIGHT,
)

class FlightRepository:
    # Convert a database row into a Flight model
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

    # Insert a flight into the database
    def create_flight(self, flight: Flight) -> Flight:
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(INSERT_FLIGHT, (
                    flight.airline, 
                    flight.source, 
                    flight.destination, 
                    flight.journey_date, 
                    flight.departure_time,
                    flight.arrival_time, 
                    flight.duration, 
                    flight.total_stops, 
                    flight.additional_information
                ))
                result = db.cursor.fetchone()
                flight.flight_id = result[0]
                ApplicationLogger.info(f"Flight created successfully. Flight ID: {flight.flight_id}")
                return flight
        except Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to create flight: {error}")

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

    # Update flight details
    def update_flight(self, flight: Flight) -> bool:
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(UPDATE_FLIGHT, (
                    flight.airline,
                    flight.source,
                    flight.destination,
                    flight.journey_date,
                    flight.departure_time,
                    flight.arrival_time,
                    flight.duration,
                    flight.total_stops,
                    flight.additional_information,
                    flight.flight_id
                ))
                if db.cursor.rowcount == 0:
                    return False
                ApplicationLogger.info(f"Flight ID {flight.flight_id} updated successfully.")
                return True
        except Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to update flight: {error}")

    # Delete a flight record
    def delete_flight(self, flight_id: int) -> bool:
        try:
            with DatabaseConnection() as db:
                db.cursor.execute(DELETE_FLIGHT, (flight_id,))
                if db.cursor.rowcount == 0:
                    return False
                ApplicationLogger.info(f"Flight ID {flight_id} deleted successfully.")
                return True
        except Error as error:
            ApplicationLogger.error(str(error))
            raise RuntimeError(f"Unable to delete flight: {error}")

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