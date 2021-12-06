from Views.home_menu_view import HomeMenuView
from Views.tournament_viewer import TournamentView


class HomeMenuControl:
    def __init__(self):

        self.home_menu = HomeMenu()
        self.view = HomeMenuView(self.home_menu)
        self.tournament_view = TournamentView


    def __call__(self):
        print("~~~ Home Menu Management ~~~ ")

        choice = self.view.choose_option_game_menu()

        # Access to the Tournament Manager
        if choice == "1":
            from Controls.control_tournament import TournamentControl
            self.tournament_menu = TournamentControl()
            self.tournament_control = self.tournament_menu()

        # Access to the Player Manager
        if choice == "2":
            from Controls.control_player import PlayerControl
            self.player_menu = PlayerControl()
            self.player_control = self.player_menu()


class HomeMenuInput:
    def __init__(self, option, handler):
        self.option = option
        self.handler = handler


class HomeMenu:
    def __init__(self):
        self._entries = {}
        self.autokey = 1

    def _add_menu(self, key, option, handler):
        if key == "auto":
            key = str(self.autokey)
            self.autokey += 1
        self._entries[str(key)] = HomeMenuInput(option, handler)

    def object(self):
        return self._entries.items()

    def __contains__(self, choice):
        return str(choice) in self._entries

    def __getitem__(self, choice):
        return self._entries[choice]


