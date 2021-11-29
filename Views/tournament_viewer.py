from Models.tournament import Tournament
from Views.player_viewer import PlayerView
from Models.match import Match
from Data_base import DataBaseService




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
        self.db = DataBaseService()


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
1: Display all informations from one tournament
2: Add player in one tournament 
3: Select all players from one tournament order by rank
4: Select all players from one tournament order by name
5: Select all tournament
6: Select all match from one tournament
7: Select all round from one tournament
8: Return to the Home Menu

>> choose you're options >>''')
        return choice

    # Chose a tournament from the tournaments list, returns the ID of it
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
            print(player.familly_name, player.first_name, player.rank, player.age, player.gender, player.point)

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

    def update_score_round(self, match, tournament):

        print(str(match.player1.id) + ' | ' + match.player1.familly_name + ' | ' + match.player1.first_name + ' ' +
              '°°°' + ' ' + 'VS' + ' ' + '°°°' + ' ' + str(match.player2.id) + ' | ' + match.player2.familly_name +
              ' | ' + match.player2.first_name)
        print('\n')
        results = input(" Please enter the id of the player to know who winn, or 0 in cas of equality : ")
        print('\n')
        # if result_player =! match.player1.id or result_player =! match.player2.id or result_player =! 0:
        #     print ("Error, please enter a valide value")

        if int(results) == match.player1.id:
            match.results = 1
            tournament.players[match.player1.id].point += 1
            self.db.update_points(tournament.players[match.player1.id])
            self.db.update_results(match)
            print(match.player1.first_name + " : 1  " + match.player2.first_name + " : 0 ")
        elif int(results) == match.player2.id:
            match.results = 2
            tournament.players[match.player2.id].point += 1
            self.db.update_points(tournament.players[match.player2.id])
            self.db.update_results(match)
            print(match.player2.first_name + " : 1  " + match.player1.first_name + " : 0 ")
        else:
            match.results = 0
            tournament.players[match.player1.id].point += 0.5
            tournament.players[match.player2.id].point += 0.5
            self.db.update_points(tournament.players[match.player1.id])
            self.db.update_points(tournament.players[match.player2.id])
            self.db.update_results(match)
            print(match.player1.first_name + " : 0.5  " + match.player2.first_name + " : 0.5 ")

    def display_players_from_one_tournament_order_by_rank(self, tournament):

        players_sorted = sorted(tournament.players.items(), key=lambda player: player[1].rank)
        for i in range(len(players_sorted)):
            print((players_sorted[i][1]).familly_name)

    def display_players_from_one_tournament_order_by_name(self, tournament):

        players_sorted = sorted(tournament.players.items(), key=lambda player: player[1].familly_name)
        for i in range(len(players_sorted)):
            print((players_sorted[i][1]).familly_name)

    # Prints every match from a defined tournament
    def display_all_match_for_one_tournament(self, tournament):
        print("\n")
        print("°°° MATCH INFORMATIONS °°°")
        print("\n")
        for id_round, round in tournament.round_list.items():
            print("°°° ", round.name, "°°°")
            for id_match, match in round.match_list.items():
                if match.results == 0:
                    print('---' + match.player1.familly_name + ' VS ' + match.player2.familly_name + ' : EQUALITY')
                elif match.results == 1:
                    print('---' + match.player1.familly_name + ' VS ' + match.player2.familly_name + ' ---- : ' + '{ ' +
                          match.player1.familly_name + ' }' + ' ' + 'WINN')
                elif match.results == 2:
                    print('---' + match.player1.familly_name + ' VS ' + match.player2.familly_name + ' ---- : ' + '{ ' +
                          match.player2.familly_name + ' }' + ' ' + 'WINN')
                elif match.results == None:
                    print('--- ' + match.player1.familly_name + ' VS ' + match.player2.familly_name +
                          ' ---- : MATCH NONE PLAYED YET')
            print('\n')

    # Prints every round from a defined tournament
    def display_all_round_for_one_tournament(self, tournament):
        print("\n")
        print("°°° MATCH INFORMATIONS °°°")
        print("\n")
        for id_round, round in tournament.round_list.items():
            print("---", tournament.name, "---", ":", "°°° ", round.name, "°°°")




