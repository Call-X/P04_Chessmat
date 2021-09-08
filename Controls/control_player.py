from Views.player_viewer import Player
from Models.player import PlayerMenu

class PlayerControl:
    def __init__(self):
        self.player = PlayerMenu()
        self.view = Player(self.player)
        self.player_list = []


    def __call__(self):
        print("~~~ Create or Modify a Player ~~~ ")
        while True:

            self.first_name = input("Entrez le prenom du joueur : ").capitalize()
            self.familly_name = input("Entrez le nom du joueur : ").capitalize()
            self.player_index = input("Enter the index player : ")
            self.new_rank = input("Enter the new rank : ")
            self.birth_date = input("Date Of Birth (jj/mm/aaaa) : ").strip()
            self.rank = input("Player Rank : ")


        # demander a la vue d'afficher le menu et collecter la réponse de 'lutilisateur
            user_choice = self.view.get_new_player()
            self.player_list = self.view.get_new_player()

            return user_choice




