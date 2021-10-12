from Views.player_viewer import PlayerView
from Views.tournament_viewer import TournamentView

# affichage du menu aux utilisateurs


class HomeMenuView:
    input = {}

    def __init__(self, home_menu):
        self.home_menu = home_menu
        self.tournament = TournamentView
        self.player = PlayerView



    def choose_option_game_menu(self):
        while True:
            choice = input('''
Welcome to the Game Menu
1: Tournament Management
2: Player Management
3: Quit
>> choose you're options >>''')

            return choice













    # def menu_display(self):
    #     print("Welcome to the Game Menu")
    #     for key, entry in self.menu.object():
    #         print(f"{key}: {entry.option}")
    #
    #         # retourner de le choix de l'utilisateur
    #
    # def get_user_choice(self):
    #     while True:
    #         self.menu_display()
    #         choice = input(">> choose you're options >>")
    #         if choice in self.menu:
    #             print("°°°You are in°°° : ")
    #             return self.menu[choice]
    #
    #         elif choice not in self.menu:
    #             print("$$$ Option no available, \n", "Please enter a number between 1 and 6 $$$")
    #             continue
    #         else:
    #             break







