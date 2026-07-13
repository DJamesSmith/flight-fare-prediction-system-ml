from database.db_connection import DatabaseConnection
from utilities.id_generator import IDGenerator

class BaseRepository:
    def generate_unique_code(self, exists_query: str) -> str:
        while True:
            code: str = IDGenerator.generate()
            with DatabaseConnection() as db:
                db.cursor.execute(exists_query, (code,))
                exists = db.cursor.fetchone()[0]
            if not exists:
                return code