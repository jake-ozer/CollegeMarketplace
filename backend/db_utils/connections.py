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

