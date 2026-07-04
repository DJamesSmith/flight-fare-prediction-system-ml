# PostgreSQL connection
# Executing SQL queries
# CRUD operations
# Returning model objects

import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

class DatabaseConnection:
    def __init__(self):
        self.connection = None

    def connect(self):
        if self.connection is None:
            self.connection = psycopg.connect(
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD")
            )
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
            self.connection = None

    def get_connection(self):
        return self.connect()