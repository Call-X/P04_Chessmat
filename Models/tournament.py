
class Tournament(object):

    connexion = None

    def __init__(self, id=0, tournament_name=None, tournament_location=None, tournament_start_date=None,
                 tournament_end_date=None, rounds=None, tournament_play_style=None):
        self.id = id
        self.tournament_name = tournament_name
        self.tournament_location = tournament_location
        self.tournament_start_date = tournament_start_date
        self.tournament_end_date = tournament_end_date
        self.rounds = rounds
        self.tournament_play_style = tournament_play_style

        # All players registered for the tournament
        self.players = {}




