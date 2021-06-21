from .CSVDatabase import CSVDatabase


class DatabaseFactory:

    @staticmethod
    def get(db_type):
        if db_type.lower() == "csv":
            return CSVDatabase()
        elif db_type.lower() == "sql":
            return SQLDatabase()
