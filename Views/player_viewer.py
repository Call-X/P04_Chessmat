from Models.player import Player
from Models.tournament import Tournament


class PlayerView:
    input = {}

    def __init__(self, player):
        self.player = player
        self.familly_name = "familly name"
        self.first_name = "first name"
        self.rank = "rank"
        self.player_id = 'id'
        self.tournament = Tournament
        self.tournament_id = 'tournament_id'

    def get_new_player(self):
        while True:
            # self.player_id = input("player id : ")
            self.familly_name = input("Enter the familly name player : ").capitalize()
            self.first_name = input("Enter the fisrt name player: ").capitalize()
            self.age = input("Enter your age:  ")
            self.gender = input("Enter your gender: ")
            self.rank = input("Player Rank : ")

            return Player(0, self.familly_name, self.first_name, self.age, self.gender, self.rank)


    def choose_option_player(self):
        while True:
            choice = input('''
Welcome to the Player Menu
1: Create player
2: Select options player
3: Modify player
4: Return to the Home Menu
>> choose you're options >>''')

            return choice

    def select_options_players(self):
        choice = input('''
Welcome to the Player Selecter Menu

1: Select player by rank
2: select player order by familly name
3: Return to the Main Menu

 
>> choose you're options >>''')
        return choice

    def select_modification_players(self):
        choice = input('''
Welcome to the Player Selecter modification Menu
1: Update player
2: Return to the Main Menu

>> choose you're options >>''')
        return choice

    def select_order_players_by_rank(self):
        tournament = input("What is the id of the tournament would you choose? : ")
        return tournament

    def erase_player_by_rank(self):
        player_rank = input("What is the rank of the player(s) you want to erase? : ")
        return player_rank

    def update_player(self):
        player_familly_name = input("What is the familly name of the player(s) you want to update? : ")
        player_first_name = input("What is the first name of the player(s) you want to update? : ")
        player_rank = input("What is the rank of the player(s) you want to update? : ")
        player_id = input("What is the id of the player(s) you want to update? : ")
        return {'familly_name': player_familly_name, 'first_name': player_first_name, 'rank': player_rank,
                'id': player_id}

    def display_all_players(self, sorted_player):
        for player in sorted_player:
            print("Name: " + player[1] + " || rank: " + str(player[3]))



