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




