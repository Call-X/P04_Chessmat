# from Controls.control_round import RoundControl
# from Controls.control_player import PlayerControl
from Views.tournament_viewer import TournamentView
# from Models.tournament import TournamentMenu
from Data_base import DataBaseService


class TournamentControl:

    def __init__(self):
        self.tournament_menu = TournamentMenu()
        self.view = TournamentView(self.tournament_menu)

    def __call__(self):
        print("{Trounament Launcher}")

        # self.tournament._add_menu("auto", "Create player", PlayerControl()), "\n"
        # self.tournament._add_menu("auto", "Create or consult the player list", PlayerControl()), "\n"
        # self.tournament._add_menu("auto", "Consult or Modify the player's ranking", PlayerControl()), "\n"
        # self.tournament._add_menu("auto", "create the Round's options", RoundControl()), "\n"
        # # self.tournament._add_menu("auto", "create the Round's options", HomeMenuControl()),
        # user_choice = self.view.get_new_tournament_information()
        # return user_choice.handler



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
