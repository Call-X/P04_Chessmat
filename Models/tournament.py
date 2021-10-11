from Data_base import DataBaseService


class Tournament(object):
    players_table = DataBaseService
    connexion = None

    def __init__(self, tournament_name = None, tournament_location = None, tournament_start_date =None,
                 tournament_end_date=None, tournament_player_number=None, tournament_max_turn=None,
                 tournament_play_style=None):

        self.tournament_name = tournament_name
        self.tournament_location = tournament_location
        self.tournament_start_date = tournament_start_date
        self.tournament_end_date = tournament_end_date
        self.tournament_player_number = tournament_player_number
        self.tournament_max_turn = tournament_max_turn
        self.tournament_play_style = tournament_play_style
