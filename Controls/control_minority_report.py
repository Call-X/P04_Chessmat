from Controls.control_player import PlayerControl
from Controls.control_tournament import TournamentControl
from Controls.control_sub_report import SubReportMenuControl
from Views.minority_report_menu_viewer import MinorityReportMenu
# from Controls.control_game import HomeMenuControl
from Models.options_viewer_menu import Menu
from Controls.control_screen import ScreenControl

class MinorityReportMenuControl:
    def __init__(self):
        self.menu = Menu()
        self.view = MinorityReportMenu(self.menu)


    def __call__(self):
        print(" °Consulting the Minority report° ")
        while True:

            self.menu._add_menu("auto", "Player list", PlayerControl()), "\n"
            self.menu._add_menu("auto", "Current player list", PlayerControl()), "\n"
            self.menu._add_menu("auto", "All tournament list", TournamentControl()), "\n"
            self.menu._add_menu("auto", "All match list of the Tournament", TournamentControl()), "\n"
            self.menu._add_menu("auto", "All round list of the Tournament", TournamentControl()), "\n"
            self.menu._add_menu("auto", "Go to the Sub Report Menu", SubReportMenuControl()), "\n"
            self.menu._add_menu("q", "return to the main menu", ScreenControl()),



            user_choice = self.view.get_user_minority_choice()
            return user_choice.handler

