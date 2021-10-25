
class Round:
    match_list = []

    def __init__(self, name=None, number_of_round=None, round_start_time=None):

        self.name = name
        self.matchs = []
        self.number_of_round = number_of_round
        self.round_start_time = round_start_time
        self.round_end_time = None

