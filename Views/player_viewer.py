from Models.player import Player
from Models.tournament import Tournament


class PlayerView:
    input = {}

    def __init__(self, player):
        self.player = player
        self.familly_name = "familly name"
        self.first_name = "first name"
        self.rank = "rank"
        self.age = "age"
        self.gender = "gender"
        self.player_id = 'id'
        self.tournament = Tournament
        self.tournament_id = 'tournament_id'

    def choose_option_player(self):

        condition = False
        choice = 0
        while condition is False:
            choice = input('''
~~~ Welcome to the Player Menu ~~~

1: { $ Create player $ }
2: { $$ Select options player $$ }
3: { $$$ Return to the Home Menu $$$ }
>> choose you're options >>''')
            if choice == "":
                print("  °°° ENTER A NUMBER IN LINK WITH THE MENU CHOICES °°° ")
            elif not choice.isdigit():
                print(" °°° ENTER A NUMBER IN LINK WITH THE MENU CHOICES °°° ")
            elif int(choice) not in [1, 2, 3]:
                print(" °°° ENTER A NUMBER IN LINK WITH THE MENU CHOICES °°° ")
            else:
                condition = True
        return choice


    def select_options_players(self):
        condition = False
        choice = 0
        while condition is False:
            choice = input('''
~~~ Welcome to the Player Selecter Menu ~~~

1: { * Select player by rank * }
2: { ** select player order by familly name ** }
3: { *** Return to the Main Menu *** }
>> choose you're options >>''')
            if choice == "":
                print(" °°° ENTER A NUMBER IN LINK WITH THE MENU CHOICES °°°")
            elif not choice.isdigit():
                print(" °°° ENTER A NUMBER IN LINK WITH THE MENU CHOICES °°°")
            elif int(choice) not in [1, 2, 3]:
                print(" °°° ENTER A NUMBER IN LINK WITH THE MENU CHOICES °°°")
            else:
                condition = True
        return choice


    def get_new_player(self):
        condition = False
        while condition is False:
            self.familly_name = input("___Enter the familly name player > ").capitalize()
            if self.familly_name == "":
                print(" °°° ENTER A SOMETHING °°° ")
            elif self.familly_name.isdigit():
                print(" °°° ENTER A FAMILLY NAME °°°")
            else:
                condition = True

        condition = False
        while condition is False:
            self.first_name = input(" ___Enter the fisrt name player >> ").capitalize()
            if self.first_name == "":
                print(" °°° ENTER A SOMETHING °°°")
            elif self.first_name.isdigit():
                print(" °°° ENTER A FIRST NAME NAME °°°")
            else:
                condition = True

        condition = False
        while condition is False:
            self.age = input(" ___Enter your age >>>  ")
            if self.age == "":
                print(" °°° ENTER A SOMETHING °°° ")
            elif not self.age.isdigit():
                print(" °°° ENTER AN AGE °°° ")
            else:
                condition = True

        condition = False
        while condition is False:
            self.gender = input(" ___Enter your gender >>>> ")
            if self.gender == "":
                print(" °°° ENTER A SOMETHING °°° ")
            elif self.gender.isdigit():
                print(" °°° ENTER A GENDER °°° ")
            else:
                condition = True

        condition = False
        while condition is False:
            self.rank = input(" ___Player Rank >>>>> ")
            if self.rank == "":
                print(" °°° ENTER A SOMETHING °°° ")
            elif not self.rank.isdigit():
                print(" °°° ENTER A RANK °°°")
            else:
                condition = True
            print('\n')

        return Player(0, self.familly_name, self.first_name, self.age, self.gender, self.rank)


    def display_all_players(self, sorted_player):
        for player in sorted_player:
            print("Name: " + player[1] + " || rank: " + str(player[5]))




