from Data_base import DataBaseService


class Player(object):
    players_table = DataBaseService
    connexion = None

    def __init__(self, first_name=None, familly_name=None, rank=None):
        self.familly_name = familly_name
        self.first_name = first_name
        self.rank = rank

















