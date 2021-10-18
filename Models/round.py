from Models.match import Match


class Round:
    match_list = []

    def __init__(self, name=None, match_list=None, round_number=None, round_start_time=None, round_end_time=None):

        self.name = name
        self.match_list = match_list
        self.round_number = round_number
        self.round_start_time = round_start_time
        self.round_end_time = round_end_time

