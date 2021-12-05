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

    def choose_option_tournament(self):
        condition = False
        choice = 0
        while condition is False:
            choice = input('''
~~~ Welcome to the Tournament Menu ~~~

1: { $ Create Tournament $ }
2: { $$ Select options Tournament $$ }
3: { $$$ Return to the Main Menu $$$ }
4: { $$$$ Launch a Tournament $$$$ }
>> choose you're options >>''')
            if choice == "":
                print(" °°° ENTER A NUMBER IN LINK WITH THE MENU CHOICES °°° ")
            elif not choice.isdigit():
                print(" °°° ENTER A NUMBER IN LINK WITH THE MENU CHOICES °°° ")
            elif int(choice) not in [1, 2, 3, 4]:
                print(" °°° ENTER A NUMBER IN LINK WITH THE MENU CHOICES °°° ")
            else:
                condition = True
        return choice

    def select_options_tournament(self):
        condition = False
        choice = 0
        while condition is False:
            choice = input('''
~~~ Welcome to the Tournament Selecter Menu ~~~

1: { * Display all informations from one tournament * }
2: { ** Add player in one tournament ** } 
3: { *** Select all players from one tournament order by rank *** }
4: { **** Select all players from one tournament order by name **** }
5: { ***** Select all tournament ***** }
6: { ****** Select all match from one tournament ****** }
7: { ******* Select all round from one tournament ******* }
8: { ******** Return to the Home Menu ******** }

>> choose you're options >>''')
            if choice == "":
                print(" °°° ENTER A NUMBER IN LINK WITH THE MENU CHOICES °°°° ")
            elif not choice.isdigit():
                print(" °°° ENTER A NUMBER IN LINK WITH THE MENU CHOICES °°° ")
            elif int(choice) not in [ 1, 2, 3, 4, 5, 6, 7, 8 ]:
                print(" °°° ENTER A NUMBER IN LINK WITH THE MENU CHOICES °°° ")
            else:
                condition = True
        return choice

    def get_new_tournament_information(self):
        condition = False
        while condition is False:
            self.tournament_name = input("___Enter the name of this tournament > ")
            if self.tournament_name == "":
                print(" °°° ENTER A SOMETHING °°° ")
            elif self.tournament_name.isdigit():
                print(" °°° ENTER A TOURNAMENT NAME °°°")
            else:
                condition = True

        condition = False
        while condition is False:
            self.tournament_location = input("___enter the localisation of this Tournament >> ")
            if self.tournament_location == "":
                print(" °°° ENTER A SOMETHING °°° ")
            elif self.tournament_location.isdigit():
                print(" °°° ENTER A WHERE TAKES PLACE THIS TOURNAMENT °°°")
            else:
                condition = True

        condition = False
        while condition is False:
            self.tournament_start_date = input("___Enter the start date of this Tournament (DD/MM/YYYY) >>> ")
            if self.tournament_start_date == "":
                print(" °°° ENTER A SOMETHING °°° ")
            elif self.tournament_start_date.isdigit():
                print(" °°° ENTER A START DATE TO THIS TOURNAMENT °°°")
            else:
                condition = True

        condition = False
        while condition is False:
            self.tournament_end_date = input("___Enter the end date of this tournament (DD/MM/YYYY) >>>> ")
            if self.tournament_end_date == "":
                print(" °°° ENTER A SOMETHING °°° ")
            elif self.tournament_end_date.isdigit():
                print(" °°° ENTER A END DATE TO THIS TOURNAMENT °°°")
            else:
                condition = True

        condition = False
        while condition is False:
            self.tournament_play_style = input("___Enter the gamestyle of this Tournament (bullet / blitz / rush) "
                                               ">>>>> ")
            if self.tournament_play_style == "":
                print(" °°° ENTER A SOMETHING °°° ")
            elif self.tournament_play_style.isdigit():
                print(" °°° ENTER THE TYPE OF THIS TOURNAMENT °°° ")
            else:
                condition = True

        return Tournament(self.tournament_name, self.tournament_location, self.tournament_start_date,
                          self.tournament_end_date, self.tournament_play_style)

    # Chose a tournament from the tournaments list, returns the ID of it
    def display_all_tournaments_and_choose_one(self, gb_tournaments):
        print("\n\n")
        print("---- LIST OF TOURNAMENT ----")
        for id, tournament in gb_tournaments.items():
            print(str(id) + ": " + tournament.name + " | " + tournament.location +
                  " | number of players : " + str(len(tournament.players)))
            print("\n\n")
        condition = False
        choice = 0
        while condition is False:
            choice = input("---Enter the tournament id to choose it >>>>>")
            print('\n')
            if choice == "":
                print(" °°° PLEASE ENTER A NUMBER IN LINK WITH THE TOURNAMENT'S ID °°° ")
            elif not choice.isdigit():
                print(" °°° ENTER A NUMBER IN LINK WITH THE TOURNAMENT'S ID °°° ")
            elif int(choice) not in gb_tournaments.keys():
                print(" °°° ENTER A NUMBER IN LINK WITH THE TOURNAMENT'S ID °°° ")
            else:
                condition = True
        return int(choice)

    def display_all_informations_for_one_tournament(self, tournament):
        print("\n")
        print(" > { ___TOURNAMENT INFORMATIONS___ } < ")
        print("\n")
        print(tournament.name + '|' + tournament.location + '|' + str(tournament.start_date)
              + '|' + str(tournament.end_date) + '|' + tournament.play_style + '|'
              + '|' + str(tournament.max_turn))
        for id, player in tournament.players.items():
            print(player.familly_name, player.first_name, player.rank, player.age, player.gender, player.point)
            print('\n')

    def display_all_players_and_choose_one(self, players, tournament):
        print("\n\n")
        print("---- LIST OF PLAYERS ----")
        for id, player in players.items():
            print('id : ' + str(id) + " | " + player.first_name + " | " +
                  player.familly_name + " |  " + 'rank : ' + str(player.rank))
            if id in tournament.players:
                print("  ---- DEJA INSCRIT ")
        print("\n\n")
        condition = False
        choice = 0
        while condition is False:
            choice = input("___Enter the player id to add it to the selected tournament >>>>>")
            print('\n')
            if choice == "":
                print(" °°° PLEASE ENTER A NUMBER IN LINK WITH THE PLAYER'S ID °°° ")
            elif not choice.isdigit():
                print(" °°° ENTER A NUMBER IN LINK WITH THE PLAYER'S ID °°° ")
            elif int(choice) not in players.keys():
                print(" °°° ENTER A NUMBER IN LINK WITH THE PLAYER'S ID °°°")
            else:
                condition = True
        return int(choice)

    def update_score_round(self, match, tournament):
        print(str(match.player1.id) + ' | ' + match.player1.familly_name + ' | ' + match.player1.first_name + ' ' +
              '°°°' + ' ' + 'VS' + ' ' + '°°°' + ' ' + str(match.player2.id) + ' | ' + match.player2.familly_name +
              ' | ' + match.player2.first_name)
        print('\n')
        condition = False
        results = 0
        while condition is False:
            results = input("___Please enter the id of the player to know who winn, or 0 in cas of equality >>>>>")
            print('\n')
            if results == "":
                print(" °°° Please enter the id of the player to know who winn, or 0 in cas of equality °°° ")
            elif not results.isdigit():
                print(" °°° Please enter the id of the player to know who winn, or 0 in cas of equality °°° ")
            else:
                condition = True

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
            print(' Rank | ' + str(players_sorted[i][1].rank) + ' | Familly Name || ' +
                  str(players_sorted[i][1].familly_name) +
                  ' | First Name ||| ' + str(players_sorted[i][1].first_name) + ' |  Age |||| ' +
                  str(players_sorted[i][1].age))
            print('\n')

    def display_players_from_one_tournament_order_by_name(self, tournament):

        players_sorted = sorted(tournament.players.items(), key=lambda player: player[1].familly_name)
        for i in range(len(players_sorted)):
            print(' | Familly Name || ' + str(players_sorted[i][1].familly_name) + ' | First Name ||| ' +
                  str(players_sorted[i][1].first_name) + ' Rank | ' + str(players_sorted[i][1].rank) + ' |  Age |||| ' +
                  str(players_sorted[i][1].age))
            print('\n')

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
                elif match.results is None:
                    print('--- ' + match.player1.familly_name + ' VS ' + match.player2.familly_name +
                          ' ---- : MATCH NONE PLAYED YET')

    # Prints every round from a defined tournament
    def display_all_round_for_one_tournament(self, tournament):
        print("\n")
        print("°°° MATCH INFORMATIONS °°°")
        print("\n")
        for id_round, round in tournament.round_list.items():
            print("---", tournament.name, "---", ":", "°°° ", round.name, "°°°")
            print('\n')



