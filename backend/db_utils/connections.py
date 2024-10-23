import sqlite3
from abc import ABC, abstractmethod


class DBConnection(ABC):
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection = None

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self, query):
        pass

    @abstractmethod
    def disconnect(self):
        pass


class SQLiteConnection(DBConnection):
    def connect(self):
        self.connection = sqlite3.connect(self.db_config["NAME"])

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor.fetchall()

    def disconnect(self):
        if self.connection:
            self.connection.close()