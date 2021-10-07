from Models.player import Player


class PlayerView:
    input = {}

    def __init__(self, player):
        self.player = player
        self.first_name = "first name"
        self.familly_name = "familly name"
        self.rank = "rank"
        self.player_id = 'id'

    def get_new_player(self):
        while True:
            self.first_name = input("Enter the fisrt name player: ").capitalize()
            self.familly_name = input("Enter the familly name player : ").capitalize()
            self.rank = input("Player Rank : ")
            return Player(self.first_name, self.familly_name, self.rank)

    def choose_option_player(self):
        while True:
            choice = input('''
Welcome to the Player Menu
1: Create player
2: Select options player
3: Modify player
5: Quit
>> choose you're options >>''')

            return choice

    def select_options_players(self):
        choice = input('''
Welcome to the Player Selecter Menu
1: Select player by name
2: Select player by rank
3: Select player by id
4: Select all players
5: Quit
 
>> choose you're options >>''')
        return choice

    def select_modification_players(self):
        choice = input('''
Welcome to the Player Selecter modification Menu
1: Update player
2: Erase player
5: Quit

>> choose you're options >>''')
        return choice

    def select_players_by_name(self):
        player_familly_name = input("What is the familly name of the player(s)? : ")
        return player_familly_name

    def select_players_by_rank(self):
        player_rank = input("What is the rank of the player(s)? : ")
        return player_rank


    def select_players_by_id(self):
        player_id = input("What is the id of the player(s)? : ")
        return player_id


    def erase_player_by_id(self):
        player_id = input("What is the id of the player(s) you want to erase? : ")
        return player_id


    def update_player(self):
        player_familly_name = input("What is the familly name of the player(s) you want to update? : ")
        player_first_name = input("What is the first name of the player(s) you want to update? : ")
        player_rank = input("What is the rank of the player(s) you want to update? : ")
        player_id = input("What is the id of the player(s) you want to update? : ")
        return {'familly_name': player_familly_name, 'first_name': player_first_name, 'rank': player_rank,
                'id': player_id}


