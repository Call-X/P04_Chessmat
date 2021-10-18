from Data_base import DataBaseService


class Player(object):
    players_table = DataBaseService
    connexion = None

    def __init__(self, player_id=None, familly_name=None, first_name=None, rank=None):
        self.player_id = player_id
        self.familly_name = familly_name
        self.first_name = first_name
        self.rank = rank

















