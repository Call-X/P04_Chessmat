from Views.tournament_viewer import TournamentView
from Views.home_menu_view import HomeMenuView
from Data_base import db


class TournamentControl:

    def __init__(self):
        self.tournament_menu = TournamentMenu()
        self.view = TournamentView(self.tournament_menu)

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

            # Add multiple players
            #players = db.select_all_players()
            #players_selected_ids = self.view.add_players_into_tournament(players)
            #for player_id in players_selected_ids:
            #    db.add

        # Select Tournament
        if choice == "2":
            choice_select = self.view.select_options_tournament()

            # if choice_select == "1":
            #     tournament_name = self.view.load_tournament()
            #     db.load_data_tournament(tournament_name)

            if choice_select == "1":
                tournament = self.view.select_data_tournament_by_id()
                db.select_data_tournament_by_id(tournament)

            if choice_select == "2":
                players_tournament = self.view.consult_players_tournament()
                db.consult_players_tournament(players_tournament)

            if choice_select == "3":
                matchs_tournament = self.view.consult_matchs_tournament()
                db.consult_matchs_tournament(matchs_tournament)

            if choice_select == "4":
                home_menu = self.view.menu_display(HomeMenuView)

        # select modification tournament
        if choice == "3":
            choice_select = self.view.select_modification_tournament()

            if choice_select == "1":
                tournament = self.view.update_tournament()
                db.update_tournament(tournament['tournament_name'], tournament['tournament_location'],
                                     tournament['tournament_start_date'], tournament['tournament_end_date'],
                                     tournament['tournament_player_number'], tournament['tournament_max_turn'],
                                     tournament['tournament_play_style'], tournament['id'])
                print(tournament)

            if choice_select == "2":
                tournament_id = self.view.erase_tournament_by_id()
                db.erase_data_tournament_by_id(tournament_id)
                print(tournament_id)


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
