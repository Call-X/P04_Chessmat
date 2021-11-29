from Views.player_viewer import PlayerView
from Controls.home_menu_control import HomeMenuControl
from Data_base import db



class PlayerControl:
    def __init__(self):
        self.player_menu = PlayerMenu()
        self.view = PlayerView(self.player_menu)
        self.home_menu = HomeMenuControl()
        self.DataBaseService = db


    def __call__(self):
        print("~~~ Player Management ~~~ ")

        choice = self.view.choose_option_player()

        # Create a player
        if choice == "1":
            player = self.view.get_new_player()
            db.insert_data_player(player)
            choice = self.home_menu_control = self.home_menu()

        # Select Player
        if choice == "2":
            choice_select = self.view.select_options_players()

            if choice_select == "1":
                players = db.select_data_player_order_by_rank()
                self.view.display_all_players(players)

            if choice_select == "2":
                players = db.select_data_player_order_by_name()
                self.view.display_all_players(players)

            if choice_select == "3":
                choice = self.home_menu_control = self.home_menu()


        # select modification players
        if choice == "3":
            choice_select = self.view.select_modification_players()

            if choice_select == "1":
                player = self.view.update_player()
                db.update_player(player['familly_name'], player['first_name'], player['rank'], player['id'])

            if choice_select == "2":
                self.home_menu_control = self.home_menu()


class PlayerMenuInput:
    def __init__(self, option, handler):
        self.option = option
        self.handler = handler


class PlayerMenu:
    def __init__(self):
        self._entries = {}
        self.autokey = 1

    def _add_menu(self, key, option, handler):
        if key == "auto":
            key = str(self.autokey)
            self.autokey += 1

        self._entries[str(key)] = PlayerMenuInput(option, handler)

    def object(self):
        return self._entries.items()

    def __contains__(self, choice):
        return str(choice) in self._entries

    def __getitem__(self, choice):
        return self._entries[choice]
