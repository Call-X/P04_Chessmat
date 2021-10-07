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
            self.connexion = sqlite3.connect("chessmat.db")
            print("CONNECTION SUCCEED. SQL LITE VERSION " + sqlite3.version)
        except Error as e:
            print(e)

    '''Tournament'''
    def tournament_list(self):
        cur = self.connexion.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS tournaments(
                id.integer PRIMARY KEY,       
                tournament_name TEXT,
                tournament_location TEXT,
                tournament_start_date TEXT,
                tournament_end_date TEXT,
                tournament_player_number INTEGER,
                tournament_max_turn INTEGER,
                tournament_play_style TEXT;''')

    def insert_data_tournament(self, tournament):
        tournament = [(tournament.tournament_name, tournament.tournament_location, tournament.tournament_start_date,
                       tournament.tournament_end_date, tournament.tournament_player_number,
                       tournament.tournament_max_turn, tournament.tournament_play_style)]

        cur = self.connexion.cursor()
        cur.executemany('''INSERT INTO tournaments (tournament_name, tournament_location, tournament_start_date,
        tournament_end_date, tournament_player_number, tournament_max_turn, tournament_play_style) VALUES ( ?, ?, ?, ?,
         ?, ?, ? )''', tournament)
        self.connexion.commit()

        return cur.lastrowid

    def select_data_tournament_by_id(self, tournament_id):
        cur = self.connexion.cursor()
        cur.execute('SELECT * FROM tournaments WHERE id=?', (tournament_id,))
        return cur.fetchone()

    def consult_players_tournament(self):
        pass

    def consult_matchs_tournament(self):
        pass

    def update_tournament(self, tournament_name, tournament_location, tournament_start_date, tournament_end_date,
                          tournament_player_number, tournament_max_turn, tournament_play_style, id):
        cur = self.connexion.cursor()
        cur.execute("UPDATE tournaments SET tournament_name=?, tournament_location=?, tournament_start_date=?,tournament_end_date=?, tournament_player_number=?, tournament_max_turn=?, tournament_play_style=? WHERE id=?",
                    (tournament_name, tournament_location, tournament_start_date, tournament_end_date,
                     tournament_player_number, tournament_max_turn, tournament_play_style, id))
        self.connexion.commit()
        print("Tournament updated!")

    def erase_data_player_by_id(self, tournament_id):
        cur = self.connexion.cursor()
        cur.execute('DELETE FROM tournaments WHERE id=?', (tournament_id,))
        self.connexion.commit()
        print("Tournament deleted!")
        return cur.fetchone()








    '''players'''
    def player_list(self):
        cur = self.connexion.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS players(
        id.integer PRIMARY KEY,       
        familly_name TEXT,
        first_name TEXT,
        rank INTEGER;''')

    def insert_data_player(self, player):
        player = [(player.first_name, player.familly_name, player.rank)]

        cur = self.connexion.cursor()
        cur.executemany('''INSERT INTO players (familly_name, first_name, rank) VALUES ( ?, ?, ? )''', player)
        self.connexion.commit()

        return cur.lastrowid

    def select_all_players(self):

        cur = self.connexion.cursor()
        cur.execute('SELECT * FROM players')
        rows = cur.fetchall()
        for row in rows:
            print(row)
        return rows

    def select_data_player_order_by_rank(self):
        cur = self.connexion.cursor()
        cur.execute('SELECT * FROM players ORDER BY rank')
        rows = cur.fetchall()
        for row in rows:
            print(row)
        return rows

    def select_data_player_by_name(self, familly_name):
        cur = self.connexion.cursor()
        cur.execute('SELECT * FROM players WHERE familly=?', (familly_name,))
        return cur.fetchall()

    def select_data_player_by_id(self, player_id):
        cur = self.connexion.cursor()
        cur.execute('SELECT * FROM players WHERE id=?', (player_id,))
        return cur.fetchone()

    def erase_player_by_id(self, player_id):
        cur = self.connexion.cursor()
        cur.execute('DELETE FROM players WHERE id=?', (player_id,))
        self.connexion.commit()
        print("Player deleted!")
        return cur.fetchone()

    def update_player(self, familly_name, first_name, rank, id):
        cur = self.connexion.cursor()
        cur.execute("UPDATE players SET familly_name=?, first_name=?, rank=? WHERE id=?",
                    (familly_name, first_name, rank, id))
        self.connexion.commit()
        print("Player updated!")


    def close(self):
        if self.connexion:
            self.connexion.close()


db = DataBaseService()





