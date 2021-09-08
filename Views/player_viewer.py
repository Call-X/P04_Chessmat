class Player:
    input = {}

    def __init__(self, player):
        self.player = player

    def ask_player_index_display(self):
        while True:
            print("Index {} Player Full Name ")
            for key, entry in self.player.object():
                print(f"{key}: {entry.option}")

    def ask_new_rank_display(self, player):
        while True:
            print(f'Actual Rank of {player.first_name} {player.familly_name} : {player.rank}')
            for key, entry in self.player.object():
                print(f"{key}: {entry.option}")

    def display_stat(self, player):
        while True:
            print(f"{player.first_name} - {player.last_name}  "
                  f"Birthdate : {player.birth_date} - Genre : {player.gender}  "
                  f"Rank : {player.rank}")


    def get_new_player(self):
        while True:
            self.display_stat()
            choice = input(">>")
            if choice in self.player:
                return self.player[choice]
            break


    def show_player_list(self, player_list):
        print(
            "Name", "\n"
            "Last Name", "\n"
            "Birthdate", "\n"
            "Gender", "\n"
            "Rank"
        )
        for player in player_list:
            print(player)
















    # def ask_player_name_display(self):
    #     first_name = input("Entrez le prenom du joueur : ").capitalize()
    #     familly_name = input("Entrez le nom du joueur : ").capitalize()
    #     return first_name, familly_name


    # def ask_player_index_display(self, players_list):
    #     while True:
    #         print("Index {} Player Full Name ")
    #         for index, player in enumerate(players_list):
    #             print(f"[{player.id}] - {player.last_name} {player.first_name} - {player.rank}")
    #         player_index = input("Enter the index player : ")
    #         return player_index



    # def ask_new_rank_display(self, player):
    #     while True:
    #         print(f'Actual Rank of {player.first_name} {player.last_name} : {player.rank}')
    #         new_rank = input("Enter the new rank : ")
    #         return new_rank



    # def ask_new_player(self, _first_name="", _familly_name=""):
    #     while True:
    #
    #         if _first_name == "" and _familly_name == "":
    #             first_name = input("First Name : ").strip()
    #             familly_name = input("Familly Name : ").strip()
    #         else:
    #
    #             first_name = _first_name.strip()
    #             familly_name = _familly_name.strip()
    #         birth_date = input("Date Of Birth (jj/mm/aaaa) : ").strip()
    #         gender = input("Gender (H/F) : ").strip()
    #         rank = input("Player Rank : ")
    #         return first_name, familly_name, birth_date, gender, rank


