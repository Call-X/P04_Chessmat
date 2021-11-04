from Views.tournament_viewer import TournamentView
from Views.player_viewer import PlayerView
from Controls.home_menu_control import HomeMenuControl
# from Models.match import Match
from Models.player import Player
# from Models.round import Round
from Data_base import db


class TournamentControl:

    def __init__(self):
        self.tournament_menu = TournamentMenu()
        self.view = TournamentView(self.tournament_menu)
        self.player = PlayerView
        self.home_menu = HomeMenuControl()
        self.round = round
        self.player = Player
        self.DatabaseService = db



    def __call__(self):
        print("{Tournament Management}")

        choice = self.view.choose_option_tournament()

        # Create a Tournament
        if choice == "1":
            tournament = self.view.get_new_tournament_information()
            db.insert_data_tournament(tournament)

            print("{°°°Tournament is created with succes°°°}")
            choice = self.view.choose_option_tournament()

        # Select Tournament

        if choice == "2":
            choice_select = self.view.select_options_tournament()

            if choice_select == "1":
                tournament_id = self.view.display_all_tournaments_and_choose_one(db.gb_tournaments)
                self.view.display_all_informations_for_one_tournament(db.gb_tournaments[int(tournament_id)])
                self.home_menu_control = self.home_menu()

             #Add a player to a tournament
            if choice_select == "2":
                tournament_id = self.view.display_all_tournaments_and_choose_one(db.gb_tournaments)
                player_id = self.view.display_all_players_and_choose_one(db.gb_players, db.gb_tournaments[int(tournament_id)])
                db.add_player_into_tournament(int(player_id), int(tournament_id))

                print("{°°°Player added with sucess°°°}")

                # self.view.choose_option_tournament()

            # if choice_select == "3":
            #     match_id = TournamentView.display_all_match_and_choose_one
            #     db.select_all_players(match_id)

            if choice_select == "3":
                tournament = self.view.get_new_tournament_information()
                self.launch_tournament(tournament)

            if choice_select == "4":
                self.home_menu_control = self.home_menu()

        # For debug purpose
    def notify(self, txt_type, text):
        balise = ""
        if txt_type == 'ERROR':
            balise = " ! "
        elif txt_type == "SUCCESS":
            balise = ' ▼ '

        print('\n' + balise + text + balise + '\n')

    def launch_tournament(self, tournament):
        if tournament is None:
            return None
        if len(tournament.players) < 4:
            self.notify("ERROR", 'This tournament contain only ' + str(len(tournament.players)) +
                        ' players. Add more players please.')
            return None
        if (len(tournament.players) % 2) != 0:
            self.notify("ERROR", "Impossible to start a tournament with an odd number players"
                                 "( " + str(len(tournament.players)) + ' )')
            return None
        print('Your are playing to the tournament named : ' + tournament.name)
        rounds = tournament.pairing(tournament)
        if len(rounds) < 2:
            self.notify("ERROR", " All matchs of this tournaments :  " + tournament.name + " have been played.")
            self.notify("SUCCESS", "the tournament :" + tournament.name + " is over")
            return None
        self.notify('SUCCESS', str(len(tournament.rounds)) + " Rounds which figure in the tournament")
        return rounds, tournament


        # Adds a round to a tournament

    def add_round(self, tournament, round):
        tournament.rounds.append(round)


    def pairing(self, tournament):
        db.gb_players.items().sorted(key=lambda player: player[3])
        # first round
        if len(tournament.rounds) == 0:
            sorted_players = db.gb_players.sorted()
            length = len(sorted_players)
            median = length // 2
            first_half = sorted_players[:median]  # slice first half
            games = []
            for player_id in range(0, len(first_half)):
                match = ([db.gb_players[player_id], 0],
                         [db.gb_players[player_id + median], 0])
                games.append(match)
            return games

    # def matchs_results(self, score_match):
    #     score_match = self.view.get_match_into_tournament()



class TournamentMenuInput:
    def __init__(self, option, handler):
        self.option = option
        self.handler = handler


class TournamentMenu:
    def __init__(self):
        self._entries = {}
        self.autokey = 1

    def _add_menu(self, key, option, handler):
        if key == "auto":
            key = str(self.autokey)
            self.autokey += 1

        self._entries[str(key)] = TournamentMenuInput(option, handler)

    def object(self):
        return self._entries.items()

    def __contains__(self, choice):
        return str(choice) in self._entries

    def __getitem__(self, choice):
        return self._entries[choice]
