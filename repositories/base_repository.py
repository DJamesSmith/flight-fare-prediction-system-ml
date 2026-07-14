from database.db_connection import DatabaseConnection
from utilities.id_generator import IDGenerator

class BaseRepository:
    @staticmethod
    def generate_unique_code(exists_query: str) -> str:
        while True:
            code: str = IDGenerator.generate()
            with DatabaseConnection() as db:
                db.cursor.execute(exists_query, (code,))
                exists = db.cursor.fetchone()[0]
            if not exists:
                return code

    @staticmethod       # Only meant for FlightRepository.insert_flights() for populating bulk data
    def generate_bulk_codes(exists_query: str, count: int) -> list[str]:
        generated_codes: list[str] = []
        generated_set: set[str] = set()

        with DatabaseConnection() as db:
            while len(generated_codes) < count:
                code: str = IDGenerator.generate()
                if code in generated_set:           # takes approximately O(1) time, set data structure is more appropriate for 10,000+ generated codes
                    continue

                db.cursor.execute(exists_query, (code,))
                exists = db.cursor.fetchone()[0]

                if not exists:
                    generated_codes.append(code)
                    generated_set.add(code)
        return generated_codes

# Introduced to hold shared behavior of flight, user and prediction repos.