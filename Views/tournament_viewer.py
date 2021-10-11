from Models.tournament import Tournament


class TournamentView:
    input = {}

    def __init__(self, tournament):
        self.tournament = tournament
        self.tournament_name = "tournament_name"
        self.tournament_location = "tournament_location"
        self.tournament_start_date = "tournament_start_date"
        self.tournament_end_date = "tournament_end_date"
        self.tournament_player_number = "tournament_player_number"
        self.tournament_max_turn = "tournament_max_turn"
        self.tournament_play_style = "tournament_play_style"

    def get_new_tournament_information(self):
        while True:
            self.tournament_name = input("Enter the name of this tournament: ")
            self.tournament_location = input("enter the localisaiton of this Tournament: ")
            self.tournament_start_date = input("Enter the start date of this Tournament (DD/MM/YYYY) : ")
            self.tournament_end_date = input("Enter the end date of this tournament (DD/MM/YYYY) : ")
            self.tournament_player_number = input("Enter the number of player : ")
            self.tournament_max_turn = input("Enter the number of turn : ")
            self.tournament_play_style = input("Enter the gamestyle of this Tournament (bullet / blitz / rush) : ")

            return Tournament(self.tournament_name, self.tournament_location, self.tournament_start_date,
                    self.tournament_end_date,  self.tournament_player_number, self.tournament_max_turn,
                    self.tournament_play_style)

    def choose_option_tournament(self):
        while True:
            choice = input('''
Welcome to the Tournament Menu
1: Create Tournament
2: Select options Tournament
3: Select modification Tournament
4: Return to the main menu
>> choose you're options >>''')

            return choice

    def select_options_tournament(self):
        choice = input('''
Welcome to the Tournament Selecter Menu
1: Select Tournament by id
2: Consult Player's Tournament
3: Consult match's Tournament
4: quit

>> choose you're options >>''')
        return choice

    def select_modification_tournament(self):
        choice = input('''
Welcome to the Player Selecter modification Menu
1: Update tournament by id
2: Erase tournament by id
5: Quit

>> choose you're options >>''')
        return choice

    # def load_tournament(self):
    #     tournament_id = input("What is the id of the tournament would you load? : ")
    #     return tournament_id

    def select_data_tournament_by_id(self):
        tournament_id = input("What is the id of the tournament? : ")
        return tournament_id

    def consult_players_tournament(self):
        pass

    def consult_matchs_tournament(self):
        pass

    def update_tournament(self):
        tournament_name = input("Enter the name of this tournament: ")
        tournament_location = input("enter the localisaiton of this Tournament: ")
        tournament_start_date = input("Enter the start date of this Tournament (DD/MM/YYYY) : ")
        tournament_end_date = input("Enter the end date of this tournament (DD/MM/YYYY) : ")
        tournament_player_number = input("Enter the number of player : ")
        tournament_max_turn = input("Enter the number of turn : ")
        tournament_play_style = input("Enter the gamestyle of this Tournament (bullet / blitz / rush) : ")
        tournament_id = input("Enter the id of this Tournament : ")
        return {'tournament_name': tournament_name, 'tournament_location': tournament_location,
                'tournament_start_date': tournament_start_date, 'tournament_end_date': tournament_end_date,
                'tournament_player_number': tournament_player_number, 'tournament_max_turn': tournament_max_turn,
                'tournament_play_style': tournament_play_style, 'tournament_id': tournament_id}

    def erase_tournament_by_id(self):
        tournament_id = input("What is the id of the tournament you want to erase? : ")
        return tournament_id

    def add_player_into_tournament(self):
        player_id = input("Enter the id of the player to registered: ")
        tournament_id = input("Enter the id of the tournament:")

        return {'player_id': player_id, 'tournament_id': tournament_id}

    def add_players_into_tournament(self, players):
        for player in players:
            print(player.id + " " + player.first_name + " " + player.familly_name)
        player_ids = input("Enter id of each player you want to registered for this tournament (separated with coma \",\") ")
        return player_ids




