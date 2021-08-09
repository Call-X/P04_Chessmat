class GameView:

    def new_tournament(self):
        tournament_name = input("enter the Name of this Tourament : ")
        tournament_location = input("Enter the location of the tournament : ")
        tournament_start_date = input("Enter the start date oe the tournament (JJ/MM/AAAA) : ")
        tournament_end_date = input("Enter the end date of the tournament (JJ/MM/AAAA) : ")
        tournament_player_number = input("Enter the number of players : ")
        tournament_max_round = input("Enter the number of rounds : ")
        tournament_game_style = input("Enter the Game style (bullet / blitz / short move) : ")
        return (tournament_name, tournament_location, tournament_start_date, tournament_end_date,
                tournament_max_round, tournament_player_number, tournament_game_style)

    def score_asking(self, match):
        print(f"-- {match.p1.shorted} vs {match.p2.shorted} -- ")
        print(f"Enter the result of the match\n"
              f"[1] {match.p1.first_name}\n Is Victorious  "
              f"[2] {match.p2.first_name}\n Loose "
              "[3] Egalité\n")
        return input("Your Answer : ")

    def tournament_index_asking(self, tournoi_list):
        for index, tournament in enumerate(tournoi_list):
            print(f"[{index}] - {tournament.name}")

        option = int(input("Entrez le numero du tournoi de votre choix : "))

        return option

    def tournament_load_asking(self):

        print("you choose to \n[0] Load a Playing tournament\n[1] Creat a new Tournament\n[2] Consult an old Tournament"
              "\n[3]Quit")
        option = input("Answer : ")
        return option

    def display_tournament_rounds(self, tournament):
        print(f"---- Tournament list {tournament.name} ----")
        for round in tournament.round_list:
            print(round)

    def display_tournament_matchs(self, match_list):
        for match in match_list:
            player1 = match[0][0]
            player2 = match[1][0]
            print(f"{player1} / Score : {match[0][1]}\n"
                  f"{player2} / Score : {match[1][1]}")

    def display_ranking(self, players):
        print("---- Ranking ----")
        for index, p in enumerate(players):
            player, score = p
            print(f"[{index + 1}] - {player.first_name} {player.familly_name} / Score : {score}")

    def display_turn(self):
        print("Start of the round")

    def display_end_match(self):
        print('Check Mat')

    def display_tournament_player(self, tournament, player_list):
        print(f"---- {tournament.familly_name} ----")
        for player in player_list:
            print(player)
            print("-" * 70)

    def display_tournaments(self, list_tournament):
        print("f---- Tournaments ----")
        for tournament in list_tournament:
            print(tournament)
            print('-' * 70)

    def display_match_tournaments(self, match_list):
        for key, matchs in match_list.items():
            print(f"---- {key} ----")
            for match in matchs:
                print(match)

    def display_round_tournaments(self, round_list):
        print('match list')
        print('|'.join([
            "Name".center(20),
            "Match Count".center(20),
            "Start time".center(20),
            "End time".center(20)
        ]))
        for round in round_list:
            print(round)

    def stop_tournament_asking(self):
        print("Do you want to continue this tournament?")
        print('[0] - Yes\n[1] - Not\n')
        option = input('Your answer : ')
        return option