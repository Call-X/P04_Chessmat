from Models.options_viewer_menu import Menu
from Views.home_menu_view import HomeMenuView
from Controls.control_tournament import TournamentControl
from Controls.control_player import PlayerControl
from Controls.control_minority_report import MinorityReportMenuControl
from Controls.control_sub_report import SubReportMenuControl
from Controls.control_screen import ScreenControl

class HomeMenuControl:
    def __init__(self):

        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self):
        #construction du menu
        self.menu._add_menu("auto", "Tounament Management", TournamentControl()),"\n"
        self.menu._add_menu("auto", "Player Management", PlayerControl()), "\n"
        self.menu._add_menu("auto", "Minority menu ", MinorityReportMenuControl()), "\n"
        self.menu._add_menu("auto", "Sub-report menu", SubReportMenuControl()), "\n"
        self.menu._add_menu("auto", "Quit", ScreenControl()), "\n"

        #demander a la vue d'afficher le menu et collecter la réponse de 'lutilisateur
        user_choice = self.view.get_user_choice()

        #retrouner le controller associé au choix de  l'utilisateur au controller principal
        return user_choice.handler