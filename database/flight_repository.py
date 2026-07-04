# ✔ Save Flight
# ✔ Get Flight By ID
# ✔ Get All Flights
# ✔ Delete Flight

from abc import abstractmethod
from database.base_repository import BaseRepository

class FlightRepository(BaseRepository):
    @abstractmethod
    def insert(self):
        # Insert a flight record.
        pass

    @abstractmethod
    def find_by_id(self):
        # Retrieve a flight using the flight ID.
        pass

    @abstractmethod
    def find_all(self):
        # Retrieve all flight records.
        pass

    @abstractmethod
    def update(self):
        # Update flight details.
        pass

    @abstractmethod
    def delete(self):
        # Delete a flight record.
        pass