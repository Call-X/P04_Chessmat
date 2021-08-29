class Tournament:
    def __init__(self, name, end_date, start_date,  game_style, location, match_number, players_number, players_list,
                 time_controler, general_quotations):
        self.name = name
        self.end_date = end_date
        self.start_date = start_date
        self.game_style = game_style
        self.location = location
        self.match_number = match_number
        self.players_number = players_number
        self.players_list = players_list
        self.time_controler = time_controler
        self.general_quotations = general_quotations
        self.round_list = []


