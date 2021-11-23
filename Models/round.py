class Round:

    def __init__(self, id=0, tournament_id=None, name=None, start_time=None, end_time=None):
        self.id = id
        self.tournament_id = tournament_id
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.match_list = {}

    @classmethod
    def add_match(cls, round, match):
        round.match_list[match.id] = match
