# from Views.player_viewer import PlayerView
from Data_base import DataBaseService


class Player(object):
    players_table = DataBaseService
    # player_list = PlayerView

    def __init__(self, first_name, familly_name, rank):
        self.first_name = first_name
        self.familly_name = familly_name
        self.rank = rank

    def __repr__(self):
        return "Player(first name ='{}', familly name ='{}')".format(self.first_name, self.familly_name)


    def serialize_player(self):

        serialize_player = {
            'first_name': self.first_name,
            'familly_name': self.familly_name,
            'rank': self.rank
        }
        return serialize_player

    def select_player_by_ID(self):
        pass

    def insert_player_to_db(self):
        pass

    def update_player_rank_in_db(self):
        pass

    def delete_palyer_to_db(self):
        pass






