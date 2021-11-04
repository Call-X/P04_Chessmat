
class Tournament(object):

    connexion = None

    def __init__(self, id=0, name=None, location=None, start_date=None,
                 end_date=None, max_turn=None, play_style=None):
        self.id = id
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.max_turn = max_turn
        # self.tournament_player_number = tournament_player_number
        # self.rounds = rounds
        self.play_style = play_style

        # All players registered for the tournament
        self.players = {}

        # All matchs for the tournament
        self.matchs = {}

        # All rounds for the tournament
        self.rounds = {}





