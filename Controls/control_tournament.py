from Views.tournament_viewer import TournamentView
from Views.player_viewer import PlayerView
from Controls.home_menu_control import HomeMenuControl
from Models.match import Match
from Data_base import db


class TournamentControl:

    def __init__(self):
        self.tournament_menu = TournamentMenu()
        self.view = TournamentView(self.tournament_menu)
        self.player = PlayerView
        self.home_menu = HomeMenuControl()
        self.total_number_players = []


    def __call__(self):
        print("{Tournament Management}")

        choice = self.view.choose_option_tournament()

        # Create a Tournament
        if choice == "1":
            tournament = self.view.get_new_tournament_information()
            db.insert_data_tournament(tournament)

            # Add one player
            param = self.view.add_player_into_tournament()
            db.add_player_into_tournament(param['player_id'], param['tournament_id'])

            print("{°°°Tournament is created with succes°°°}")
            choice = self.view.choose_option_tournament()

            # Add multiple players
            #players = db.select_all_players()
            #players_selected_ids = self.view.add_players_into_tournament(players)
            #for player_id in players_selected_ids:
            #    db.add


        # Select Tournament

        if choice == "2":
            choice_select = self.view.select_options_tournament()

            if choice_select == "1":
                tournament = self.view.select_data_tournament_by_id()
                db.select_data_tournament_by_id(tournament)
                choice = self.home_menu_control = self.home_menu()

            if choice_select == "2":
                db.select_all_tournament()
                choice = self.home_menu_control = self.home_menu()

            if choice_select == "3":
                db.select_all_players_in_tournament()
                choice = self.home_menu_control = self.home_menu()

            # if choice_select == "4":
            #     matchs_tournament = self.view.consult_matchs_tournament()
            #     db.consult_matchs_tournament(matchs_tournament)
            #     choice = self.view.select_options_tournament()

            if choice_select == "5":
                self.home_menu_control = self.home_menu()


        # select modification tournament
        if choice == "3":
            choice_select = self.view.select_modification_tournament()

            if choice_select == "1":
                tournament = self.view.update_tournament()
                db.update_tournament(tournament['tournament_name'], tournament['tournament_location'],
                                     tournament['tournament_start_date'], tournament['tournament_end_date'],
                                     tournament['tournament_player_number'], tournament['tournament_max_turn'],
                                     tournament['tournament_play_style'], tournament['tournament_id'])
                print(tournament)
                choice_select = self.view.select_modification_tournament()

            if choice_select == "2":
                tournament_id = self.view.erase_tournament_by_id()
                db.erase_data_tournament_by_id(tournament_id)
                print(tournament_id)
                choice_select = self.view.select_modification_tournament()

            if choice_select == "3":
                self.home_menu_control = self.home_menu()

        if choice == "4":

            self.home_menu_control = self.home_menu()

    def player_matchs(self, player):
        i = 1
        self.total_number_players = len(db.select_player_order_by_rank())
        while i <= self.total_number_players/2:
            Match(player[i], player[i + (self.total_number_players/2)])

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
