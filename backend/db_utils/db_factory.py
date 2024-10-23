from enum import Enum
from backend.db_utils.connections import SQLiteConnection


class DBType(Enum):
    SQLITE = "sqlite"
    MYSQL = "mysql"
    POSTGRES = "postgres"

db_configs = {
    DBType.SQLITE: {
        "NAME": "db.sqlite3",
    },
    DBType.POSTGRES: {
        "NAME": "my_postgres_db",
        "USER": "postgres_user",
        "PASSWORD": "postgres_pass",
        "HOST": "hostname",
        "PORT": "portnum",
    },
}


class DBFactory:
    def get_db_connection(db_type):
        if db_type == DBType.SQLITE:
            return SQLiteConnection(db_configs[DBType.SQLITE])
        else:
            raise ValueError("Unsupported database type")