import sqlite3
from sqlite3 import Error




class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the __init__ argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DataBaseService(metaclass=SingletonMeta):
    connexion = None

    def __init__(self):
        try:
            self.connexion = sqlite3.connect("players.db")
            print("CONNECTION SUCCEED. SQL LITE VERSION " + sqlite3.version)
        except Error as e:
            print(e)

    def create_table(self):
        cur = self.connexion.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS players(
        id.integer PRIMARY KEY,
        first  text NOT NULL,
        familly  text NOT NULL,
        rank real;''')

    def insert_data(self):

        player_list = [('Camille', 'Lefebvre', '15'),
                      ('Emile', 'Miath', '20'),
                      ('Pierre', 'Raulet', '5'),
                      ('Ben', 'JAoui', '10')]

        cur = self.connexion.cursor()
        cur.executemany('''INSERT INTO players ( first, familly, rank) VALUES ( ?, ?, ? )''', player_list)
        self.connexion.commit()


        return cur.lastrowid

    def close(self):
        if self.connexion:
            self.connexion.close()


db = DataBaseService()

db.insert_data()



