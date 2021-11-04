from Models.tournament import Tournament
from Views.player_viewer import PlayerView




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
3: Launch a Tournament
4: Return to the Home Menu

>> choose you're options >>''')
        return choice

    def display_all_tournaments_and_choose_one(self, gb_tournaments):
        print("\n\n")
        print("---- LIST OF TOURNAMENT ----")
        for id, tournament in gb_tournaments.items():
            print(str(id) + ": " + tournament.name + " | " + tournament.location +
                  " | nombre de joueur: " + str(len(tournament.players)))
        print("\n\n")
        choice = input(">> Enter the tournament id to add a player >>")
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
            print(str(id) + ": " + player.first_name + " | " +
                  player.familly_name + " | #" + str(player.rank))
            if id in tournament.players:
                print("  ---- DEJA INSCRIT ")
        print("\n\n")
        choice = input(
            ">> Enter the player id to add it to the selected tournament >>")
        return choice


    def erase_tournament_by_id(self):
        tournament_id = input("What is the id of the tournament you want to erase? : ")
        return tournament_id

    def get_round(self):
        name_of_the_round = input("Enter the name of the round :  ")
        tournament_id = input("Enter the id of the tournament : ")
        return {'name_of_the_round': name_of_the_round, 'tournament_id': tournament_id}

    def get_match_into_tournament(self):
        tournament_id = input("Enter the id of the tournament : ")
        round_number = input("Enter the number of the round : ")
        player1_rank = input("Enter the rank of the player n°1 : ")
        player2_rank = input("Enter the rank of the player n°2 : ")
        score = input('f player n°1 : {player1_score} - player n°2 : {player2_score}')
        return {'tournament_id': tournament_id, 'round_number': round_number, 'player1_rank': player1_rank,
                'player2_rank': player2_rank, 'score': score}

    # def display_launch_tournament(self):
    #     tournament = self.display_all_tournaments_and_choose_one(gb_tournaments)
    #     try:
    #         matches, tournament = launch_tournament()
    #         chess_round = self.tournament.handle_match(matches, tournament)
    #         self.handle_match_scores(chess_round, tournament)
    #
    #     except TypeError:
    #         pass

    def display_round_results(self, games):
        for result in games:
            if result[0][1] == 1:
                print(
                    result[0][0].player.familly_name + ' | ' + result[0][0].player.first_name + ' VICTORY')
            elif result[0][1] == 0.5:
                print(result[0][0].player.familly_name + ' | ' + result[0][0].player.first_name + ', '
                      + result[1][0].player.familly_name + ' | ' + result[1][0].player.first_name + ' EQUALITY')
            else:
                print(
                    result[1][0].player.familly_name + ' | ' + result[1][0].player.first_name + ' VICTORY')

        print("\n Insert a coin to continue")
        input()
        return None





