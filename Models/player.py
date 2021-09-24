from Data_base import DataBaseService


class Player(object):
    players_table = DataBaseService
    connexion = None

    def __init__(self, first_name, familly_name, rank):
        self.first_name = first_name
        self.familly_name = familly_name
        self.rank = rank

    @classmethod
    def player_list(cls):
        cur = cls.connexion.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS players(
        id.integer PRIMARY KEY,
        first  text NOT NULL,
        familly  text NOT NULL,
        rank real;''')

    def add_to_db(self):
        serialize_player = self.serialize_player()
        self.player_table.insert(serialize_player)

    # @classmethod
    def check_if_player_exists(self):
        """
        Return true if player exist in db
        """
        self.db = TinyDB('Models/db.json')
        self.player_table = self.db.table('player_table')
        self.query = Query()
        if (self.player_table.search(self.query.last_name == self.last_name)
           and self.player_table.search(self.query.first_name == self.first_name)):
            return True

    @classmethod
    def get_players_by_index(self, players_index_list):
        self.db = TinyDB('Models/db.json')
        self.player_table = self.db.table('player_table')
        self.query = Query()
        player_list = []
        for index in players_index_list:
            player = self.player_table.get(doc_id=index)
            player_list.append(player)
        return player_list

    @classmethod
    def update_player_rank(self, player_id, new_rank):
        self.db = TinyDB('Models/db.json')
        self.player_table = self.db.table('player_table')
        self.query = Query()
        self.player_table.update({'rank': new_rank}, doc_ids=[player_id])

    @classmethod
    def delete_player(self, player_id):
        self.db = TinyDB('Models/db.json')
        self.player_table = self.db.table('player_table')
        self.query = Query()
        self.player_table.remove(doc_ids=[player_id])




    # # def __repr__(self):
    # #     return "Player(first name ='{}', familly name ='{}')".format(self.first_name, self.familly_name)
    #
    def serialize_player(self):

        serialize_player = {
            'first_name': self.first_name,
            'familly_name': self.familly_name,
            'rank': self.rank
        }
        return serialize_player














