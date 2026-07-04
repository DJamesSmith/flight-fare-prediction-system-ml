# ✔ Save Flight
# ✔ Get Flight By ID
# ✔ Get All Flights
# ✔ Delete Flight

from database.db_connection import DatabaseConnection

class FlightRepository():
    def __init__(self):
        self.database = DatabaseConnection()

    # Insert a flight record
    def insert(self, flight):
        pass

    # Retrieve a flight using the flight ID
    def find_by_id(self, flight_id):
        pass

    # Retrieve all flight records
    def find_all(self):
        pass

    # Update flight details
    def update(self, flight):
        pass

    # Delete a flight record
    def delete(self, flight_id):
        pass