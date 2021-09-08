from Controls.control_round import RoundControl
from Controls.control_player import PlayerControl
from Views.tournament_viewer import TournamentView
from Models.tournament import TournamentMenu
# from Controls.control_game import HomeMenuControl

class TournamentControl:

    def __init__(self):
        self.tournament = TournamentMenu()
        self.view = TournamentView(self.tournament)

    def __call__(self):
        print("{Trounament Launcher}")

        self.tournament_name = input("Enter the name of this tournament: ")
        self.tournament_location = input("enter the localisaiton of this Tournament: ")
        self.tournament_start_date = input("Enter the start date of this Tournament (DD/MM/YYYY) : ")
        self.tournament_end_date = input("Enter the end date of this tournament (DD/MM/YYYY) : ")
        self.tournament_player_number = input("Enter the number of player : ")
        self.tournament_max_turn = input("Enter the number of turn : ")
        self.tournament_play_style = input("Enter the gamestyle of this Tournament (bullet / blitz / rush) : ")

        self.tournament._add_menu("auto", "Create player", PlayerControl()), "\n"
        self.tournament._add_menu("auto", "Create or consult the player list", PlayerControl()), "\n"
        self.tournament._add_menu("auto", "Consult or Modify the player's ranking", PlayerControl()), "\n"
        self.tournament._add_menu("auto", "create the Round's options", RoundControl()), "\n"
        # self.tournament._add_menu("auto", "create the Round's options", HomeMenuControl()),

        user_choice = self.view.get_new_tournament_indic()
        return user_choice.handler
