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

    def insert_data_player(self, player):

        player = [(player.first_name, player.familly_name, player.rank)]

        cur = self.connexion.cursor()
        cur.executemany('''INSERT INTO players ( first, familly, rank) VALUES ( ?, ?, ? )''', player)
        self.connexion.commit()

        return cur.lastrowid

    def select_data_player(self, player):
        pass

    def erase_data_player(self, player):
        pass

    def close(self):
        if self.connexion:
            self.connexion.close()


db = DataBaseService()
















# DB_name = 'ChessDB'
#
#
# def connect_to_db(db=None):
#     if db is None:
#         chessdb = ':memory:'
#         print('new connection to in-memory SQLite DB...')
#     else:
#         chessdb = '{}.db'.format(db)
#         print('New connection to SQLite DB...')
#     connection = sqlite3.connect(chessdb)
#     return connection
#
# def connect(func):
#
#     def inner_func(conn, *args, **kwargs):
#         try:
#             conn.execute('SELECT name FROM sqlite_temp_master WHERE type="table";')
#         except (AttributeError, Error):
#             conn = connect_to_db(DB_name)
#         return func(conn, *args, **kwargs)
#
#     return inner_func
#
# def disconnect_from_db(db=None, conn=None):
#     if db is not DB_name:
#         print("Your are trying to disconnect from a wrong DB")
#     if conn is not None:
#         conn.close()
#
# @connect
# def create_table(conn, table_name):
#     table_name = scrub(table_name)
#     sql = 'CREATE TABLE {} (rowid INTEGER PRIMARY KEY AUTOINCREMENT,' \
#     'name TEXT UNIQUE, price REAL, quantity INTEGER)'.format(table_name)
#     try:
#         conn.execute(sql)
#     except Error as e :
#         print(e)
#
# def scrub(input_string):
#     return ''.join(k for k in input_string if k.isalnum())
#
#
# @connect
# def insert_one(conn, first_name, familly_name, rank, table_name):
#     table_name = scrub(table_name)
#     sql = "INSERT INTO {} ('name', 'price', 'quantity') VALUES (?, ?, ?)"\
#         .format(table_name)
#     try:
#         conn.execute(sql, (first_name, familly_name, rank))
#         conn.commit()
#     except Error as e:
#         print(
#             '{}: "{}" already stored in table "{}"'.format(e, first_name, table_name))
#
# @connect
# def insert_many(conn, items, table_name):
#     table_name = scrub(table_name)
#     sql = "INSERT INTO {} ('first name', 'familly name', 'rank') VALUES (?, ?, ?)"\
#         .format(table_name)
#     entries = list()
#     for x in items:
#         entries.append((x['first name'], x['familly name'], x['rank']))
#     try:
#         conn.executemany(sql, entries)
#         conn.commit()
#     except Error as e:
#         print('{}: at least one in {} was already stored in table "{}"'
#               .format(e, [x['first name'] for x in items], table_name))
#
# def tuple_to_dict(mytuple):
#     mydict = dict()
#     mydict['id'] = mytuple[0]
#     mydict['first name'] = mytuple[1]
#     mydict['familly name'] = mytuple[2]
#     mydict['rank'] = mytuple[3]
#     return mydict



