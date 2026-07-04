from abc import ABC, abstractmethod

class BaseRepository(ABC):
    @abstractmethod
    def create(self):                   # Insert a new record.
        pass

    @abstractmethod
    def get_by_id(self):                # Retrieve a record using its primary key.
        pass

    @abstractmethod
    def get_all(self):                  # Retrieve all records.
        pass

    @abstractmethod
    def update(self):                   # Update an existing record.
        pass

    @abstractmethod
    def delete(self):                   # Delete a record.
        pass