from Models.tournament import Tournament
from Views.player_viewer import PlayerView
from Models.match import Match




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
        self.player = PlayerView
        self.match = Match

    def get_new_tournament_information(self):
        while True:
            self.tournament_name = input("Enter the name of this tournament: ")
            self.tournament_location = input("enter the localisaiton of this Tournament: ")
            self.tournament_start_date = input("Enter the start date of this Tournament (DD/MM/YYYY) : ")
            self.tournament_end_date = input("Enter the end date of this tournament (DD/MM/YYYY) : ")
            # self.tournament_player_number = input("Enter the number of player : ")
            # self.tournament_max_turn = input("Enter the number of turn : ")
            self.tournament_play_style = input("Enter the gamestyle of this Tournament (bullet / blitz / rush) : ")

            return Tournament(self.tournament_name, self.tournament_location, self.tournament_start_date,
                    self.tournament_end_date, self.tournament_play_style)

    def choose_option_tournament(self):
        while True:
            choice = input('''
Welcome to the Tournament Menu
1: Create Tournament
2: Select options Tournament
3: Return to the Main Menu
4: Launch a Tournament
>> choose you're options >>''')

            return choice

    def select_options_tournament(self):
        choice = input('''
Welcome to the Tournament Selecter Menu
1: Select All Tournament and choose one
2: Select All Player and choose one
3: Return to the Home Menu

>> choose you're options >>''')
        return choice

    def display_all_tournaments_and_choose_one(self, gb_tournaments):
        print("\n\n")
        print("---- LIST OF TOURNAMENT ----")
        for id, tournament in gb_tournaments.items():
            print(str(id) + ": " + tournament.name + " | " + tournament.location +
                  " | number of players : " + str(len(tournament.players)))
        print("\n\n")
        choice = input(">> Enter the tournament id to choose it >>")
        return choice

    def display_all_informations_for_one_tournament(self, tournament):
        print("\n")
        print("°°° TOURNAMENT INFORMATIONS °°°")
        print("\n")
        print(tournament.name + '|' + tournament.location + '|' + str(tournament.start_date)
              + '|' + str(tournament.end_date) + '|' + tournament.play_style + '|'
              + '|' + str(tournament.max_turn))
        for id, player in tournament.players.items():
            print(player.familly_name)

    def display_all_players_and_choose_one(self, players, tournament):
        print("\n\n")
        print("---- LIST OF PLAYERS ----")
        for id, player in players.items():
            print('id : ' + str(id) + " | " + player.first_name + " | " +
                  player.familly_name + " |  " + 'rank : ' + str(player.rank))
            if id in tournament.players:
                print("  ---- DEJA INSCRIT ")
        print("\n\n")
        choice = input(
            ">> Enter the player id to add it to the selected tournament >>")
        return choice


    def erase_tournament_by_id(self):
        tournament_id = input("What is the id of the tournament you want to erase? : ")
        return tournament_id

    def display_round(self, round):
        for id, match in round.match_list.items():
            print(match.player1.first_name + ' ' + '°°°' + ' ' + 'VS' + ' ' + '°°°' + ' ' + match.player2.first_name)


    def update_score(self, match):
        print(match.player1.id + ' ' + '°°°' + ' ' + 'VS' + ' ' + '°°°' + ' ' + match.player2.id)
        result_player = input(f" Please enter the id of the player to know who was winn, loose or was equality : " f" {match.player.id} ")

        if result_player == 1:
            print(f" {match.player.id} : " f" got 1 point :" f"{match.player.point} = 1 ")
        elif result_player == 2:
            print(f" {match.player.id} : " f" got 0,5 point :" f"{match.player.point} = 0,5 ")
        else:
            print(f" {match.player.id} : " f" got 0 point :" f"{match.player.point} = 0 ")













