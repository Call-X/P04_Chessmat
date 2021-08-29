
from Views.home_menu_view import HomeMenuView
from Models.options_viewer_menu import *


class ControlGame:


    def __init__(self):
        self.control = None

    def start(self):
        self.control = HomeMenuControl()
        while self.control:
            self.control = self.control()


class HomeMenuControl:
    def __init__(self):

        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self):
        #construction du menu
        self.menu.append("auto", "Tounament Launcher", NewTournamentControl()),"\n"
        self.menu.append("auto", "create player", PlayerControl()), "\n"
        self.menu.append("auto", "Ranking modification", RankingControl()), "\n"
        self.menu.append("auto", "Minority menu ", MinorityReportMenuControl()), "\n"
        self.menu.append("auto", "Sub-report menu", SubReportMenuControl()), "\n"
        self.menu.append("auto", "Quit", SubReportMenuControl()), "\n"
        #demander a la vue d'afficher le menu et collecter la réponse de 'lutilisateur
        user_choice = self.view.get_user_choice()
        #retrouner le controller associé au choix de  l'utilisateur au controller principal
        return user_choice.handler



        # while True:
        #     menu_option = self.view.game_view_options()
        #     if menu_option == 1:
        #         self.menu.append("[1]", "Tounament Launcher", NewTournamentControl())
        #     elif menu_option == 2:
        #         while True:
        #             self.control_player.create_new_player()
        #             option = self.view.ask_validation('Create new player ?')
        #             self.control_player.save_player_list()
        #             if option == "0":
        #                 continue
        #             elif option == "1":
        #                 break
        #     elif menu_option == 3:
        #         self.menu.append("[3]", "Ranking modification", RankingControl())
        #     elif menu_option == 4:
        #         self.menu.append("[4]", "Minority menu ", MinorityReportMenuControl())
        #     elif menu_option == 5:
        #         self.menu.append("[5]", "Sub-report menu", SubReportMenuControl())
        #     elif menu_option == 6:
        #         self.menu.append("[6]", "Quit", SubReportMenuControl())
        #         break

        # return menu_option.handler





    # def home_menu(self):
    #     pass
    #
    # def connexion_menu(self):
    #     pass

        # # 2 . Demander à la vue d'afficher le menu et collecter les réponses de l'utilisateur
        # user_option = self.view.get_user_option()
        # user_sub_option = self.view.get_user_sub_option()
        #
        # # 3 . Retourner le controller lié au choix de l'utilisateur au controleur principal
        # return user_option. , user_sub_option.handler




class Option:
    pass


class RankingControl:
    pass


class RoundsControl:
    pass


class MinorityReportMenuControl:
    pass


class SubReportMenuControl:
    pass


class NewTournamentControl:
    def __call__(self):
        print("In the NewTournament Control")




class PlayerControl:
    pass

