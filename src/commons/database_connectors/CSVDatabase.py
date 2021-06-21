import pandas as pd
from .Database import Database
from ..local_env.Directory import Directory



class CSVDatabase(Database):

    @staticmethod
    def read(database, **queries):
        # find the database in /data
        # if database does not exist: create directory/file
        # if it database exists, apply query -> dict {var1: test..}
        directory = Directory()
        db = directory.get(database, "csv")

        if db:

            try:
                db = pd.read_csv(db)
                for query, filter in queries.items():
                    mask = db[query] == filter
                    db = db[mask]
            except FileNotFoundError:
                db = {}

        else:
            db = {}

        return db.to_dict() if db else db

    @staticmethod
    def write(database, model):
        directory = Directory()
        db_name = directory.get(database, "csv")

        try:
            db = pd.read_csv(db_name)
        except FileNotFoundError:
            db = pd.DataFrame({k:[] for k in model.getHeaders()})

        params = model.getParams()

        db.append(params, ignore_index=True)
        db.to_csv(db_name)
