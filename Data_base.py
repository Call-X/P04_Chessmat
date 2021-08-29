from tinydb import TinyDB
db = TinyDB('db.json')
db.all()


class DBSingleton:

    _db_instance = None

    @classmethod
    def get_db(cls):
        if cls._db_instance is None:
            cls._db_instance = TinyDB('db/data.json')
        return cls._db_instance
