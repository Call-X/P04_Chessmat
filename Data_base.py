import sqlite3
from sqlite3 import Error
from Models.tournament import Tournament
from Models.player import Player




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

    def __init__(self):

        self.gb_players = {}
        self.gb_tournaments = {}
        try:
            self.connexion = sqlite3.connect("chessmat.db")
            self.connexion.execute("PRAGMA foreign_keys = 1")
            # print("CONNECTION SUCCEED. SQL LITE VERSION " + sqlite3.version)
        except Error as e:
            print(e)

    # - # Création du bloc de fonction pour charger la base de donnée dès l'ouverture du jeu

    ''' Function services '''

    def load(self):
        # create all table when program is laucnh
        self.create_all_tables_db()

        # Load all the players
        # [[1, Emile, Miath, 3],[2, Kevin, Bogo, 5]]...
        players = self.select_all_players()
        # if find players
        if len(players) > 0:
            for p in players:
                player = Player(*p)  # Player(1, Emile, Miath, 3)
                # for example : emile = players[1]
                #creation de l'objet player dans ma variable globale
                self.gb_players[player.id] = player


        # Load all the tournaments
        tournaments = self.select_all_tournament()
        if len(tournaments) > 0:
            for t in tournaments:
                tournament = Tournament(*t)
                self.gb_tournaments[tournament.id] = tournament

        # Select all tournaments where the player is registered
        # items() permet de parcourir les dictionnaire dans une boucle for
        for id, player in self.gb_players.items():
            rows = self.select_all_tournaments_from_one_player(
                player.id)
            # Si il y a des resultats (ici des tournois)
            if len(rows) > 0:
                for row in rows:
                    tournament_id = row[2]
                    self.gb_players[id].gb_tournaments[tournament_id] = self.gb_tournaments[tournament_id]

        # Select all players from one tournament
        for id, tournament in self.gb_tournaments.items():
            rows = self.select_all_players_for_one_tournament(
                tournament.id)
            if len(rows) > 0:
                for row in rows:
                    player_id = row[1]
                    self.gb_tournaments[id].players[player_id] = self.gb_players[player_id]

    def create_all_tables_db(self):
        self.create_table_tournament()
        self.create_table_player()
        self.create_table_player_in_tournament()
        self.create_table_round()
        self.create_table_match()

    '''Tournament'''
    def create_table_tournament(self):
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
        rows = cur.fetchall()
        for row in rows:
            print(row)
        return rows

    def select_all_tournament(self):
        cur = self.connexion.cursor()
        cur.execute('SELECT * FROM tournaments')
        rows = cur.fetchall()
        for row in rows:
            print(row)
        return rows


    def update_tournament(self, tournament_name, tournament_location, tournament_start_date, tournament_end_date,
                          tournament_player_number, tournament_max_turn, tournament_play_style, id):
        cur = self.connexion.cursor()
        cur.execute("UPDATE tournaments SET tournament_name=?, tournament_location=?, tournament_start_date=?,tournament_end_date=?, tournament_player_number=?, tournament_max_turn=?, tournament_play_style=? WHERE id=?",
                    (tournament_name, tournament_location, tournament_start_date, tournament_end_date,
                     tournament_player_number, tournament_max_turn, tournament_play_style, id))
        self.connexion.commit()
        rows = cur.fetchall()
        for row in rows:
            print(row)
        return rows
    # print("Tournament updated!")

    def erase_data_tournament_by_id(self, tournament_id):
        cur = self.connexion.cursor()
        cur.execute('DELETE FROM tournaments WHERE id=?', (tournament_id,))
        self.connexion.commit()
        rows = cur.fetchall()
        for row in rows:
            print(row)
        return rows
    # print("Tournament deleted!")


    '''players'''
    def create_table_player(self):
        cur = self.connexion.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS players(
        id.integer PRIMARY KEY,             
        familly_name TEXT,
        first_name TEXT,
        rank INTEGER;''')

    def insert_data_player(self, player):
        player = [(player.player_id, player.familly_name, player.first_name, player.rank)]

        cur = self.connexion.cursor()
        cur.executemany('''INSERT INTO players (id, familly_name, first_name, rank) VALUES ( ?, ?, ?, ? )''', player)
        self.connexion.commit()

        return cur.lastrowid

    def select_all_players(self):

        cur = self.connexion.cursor()
        cur.execute('SELECT * FROM players')
        rows = cur.fetchall()
        for row in rows:
            print(f' Player id, player familly name, player first name, player rank : \n {row}')
        return rows

    def select_data_player_order_by_rank(self):
        cur = self.connexion.cursor()
        cur.execute('SELECT * FROM players ORDER BY rank')
        rows = cur.fetchall()
        for row in rows:
            print(f' player id , player familly name, player first name, rank : \n {row}')
        return rows

    def select_data_player_by_name(self, familly_name):
        cur = self.connexion.cursor()
        cur.execute('SELECT * FROM players WHERE familly_name=?', (familly_name,))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        return rows

    def select_data_player_by_id(self, player_id):
        cur = self.connexion.cursor()
        cur.execute('SELECT * FROM players WHERE id=?', (player_id,))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        return rows

    def erase_player_by_id(self, player_id):
        cur = self.connexion.cursor()
        cur.execute('DELETE FROM players WHERE id=?', (player_id,))
        self.connexion.commit()
        rows = cur.fetchall()
        for row in rows:
            print(row)
        return rows
    # print("Player deleted!")


    def update_player(self, familly_name, first_name, rank, id):
        cur = self.connexion.cursor()
        cur.execute("UPDATE players SET familly_name=?, first_name=?, rank=? WHERE id=?",
                    (familly_name, first_name, rank, id))
        self.connexion.commit()
        print("Player updated!")

    '''table players in tournament'''
    def create_table_player_in_tournament(self):
        cur = self.connexion.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS players_in_tournament(
        id.integer PRIMARY KEY,
        player_id INTEGER,
        tournament_id INTEGER,
        FOREIGN KEY(player_id) REFERENCES player(id),
        FOREIGN KEY(tournament_id) REFERENCES tournament(id);''')

    def add_player_into_tournament(self, player_id, tournament_id):
        param = [(player_id, tournament_id)]
        cur = self.connexion.cursor()
        cur.executemany('''INSERT INTO players_in_tournament (player_id, tournament_id) VALUES ( ?, ? )''', param)
        self.connexion.commit()
        return cur.lastrowid

    def is_player_is_registered(self, player_id, tournament_id):
        cur = self.connexion.cursor()
        cur.execute(
            'SELECT * FROM players_in_tournament WHERE tournament_id=? AND player_id=?', (tournament_id, player_id))
        rows = cur.fetchall()

        return rows

    def select_all_players_in_tournament(self):
        cur = self.connexion.cursor()
        cur.execute('SELECT * FROM players_in_tournament')
        rows = cur.fetchall()
        for row in rows:
            print(f'id, Player id, Tournament id: \n {row}')
        return rows

    def select_all_tournaments_from_one_player(self, player_id):
        cur = self.connexion.cursor()
        cur.execute(
            'SELECT * FROM players_in_tournament WHERE player_id=?', (player_id,))
        rows = cur.fetchall()
        return rows

    def select_all_players_for_one_tournament(self, tournament_id):
        cur = self.connexion.cursor()
        cur.execute(
            'SELECT * FROM players_in_tournament WHERE id=?', (tournament_id,))
        rows = cur.fetchall()
        return rows

    def select_player_registered_by_id(self, player_id):
        cur = self.connexion.cursor()
        cur.execute('SELECT * FROM players_in_tournament WHERE id=?', (player_id,))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        return rows


    def select_tournament_contain_player_by_id(self, tournament_id):
        cur = self.connexion.cursor()
        cur.execute('SELECT * FROM players_in_tournament WHERE id=?', (tournament_id,))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        return rows

    def erase_player_registered_by_id(self, player_id):
        cur = self.connexion.cursor()
        cur.execute('DELETE FROM players_in_tournament WHERE id=?', (player_id,))
        self.connexion.commit()
        print("Player deleted!")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        return rows

    def erase_tournament_contain_player_by_id(self, tournament_id):
        cur = self.connexion.cursor()
        cur.execute('DELETE FROM players_in_tournament WHERE id=?', (tournament_id,))
        self.connexion.commit()
        print("Tournament deleted!")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        return rows

    '''match'''
    def create_table_match(self):
        cur = self.connexion.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS matchs_in_tournament(
        id.integer PRIMARY KEY,
        tournament_id INTEGER,
        FOREIGN KEY(player_id_1) REFERENCES player(id),
        FOREIGN KEY(player_id_2) REFERENCES player(id),
        FOREIGN KEY(tournament_id) REFERENCES tournament(id);''')

    '''round'''
    def create_table_round(self):
        cur = self.connexion.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS rounds_in_tournament(
        id.integer PRIMARY KEY,
        name TEXT,
        number INTEGER,
        FOREIGN KEY(tournament_id) REFERENCES tournament(id);''')




    def close(self):
        if self.connexion:
            self.connexion.close()


db = DataBaseService()





