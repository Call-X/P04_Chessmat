menus = ["Lancer un tournoi", "\n", "Ajouter un joueur", "\n", "Modifier classement joueur", "\n", "Rapport", "\n",
         "Quitter"]

rapport_menu = [
    "Listes des joueurs", "\n", "Liste joueur d'un tournoi", "\n", "Liste de tout les tournois", "\n",
    "Liste de tout les match d'un tournoi", "\n", "Liste de tout les tours d'un tournoi", "\n", "Retour"]

under_rapport_menu = ["Par ordre Alphabetique", "\n", "Par classement"]


class OptionsViews:

    def __init__(self, options=int):
        self.options = options
        self.options = 0
        self.options = int(input("Makes your choices : "))
        self.sub_options = 0

    def game_view_options(self):

        while not self.options:
            try:
                self.options

            except ValueError:
                print("Enter A Numba between 1 and 5 to choose your option")

            if self.options not in range(1, 6):
                print('choice no available ')
                continue

            elif self.options in range(1, 6):
                print("[1] Tounament Launcher",
                      "[2] Add a Player",
                      "[3] Ranking modification",
                      "[4] Minority report",
                      "[5] Quit")
            else:
                print(" Please enter you option's number ")

        return self.game_view_options()

    def display_rapport_menu(self):
        self.options = 0
        self.sub_options = 0
        while True:
            try:
                for index, number in enumerate(rapport_menu):
                    print(f"[{index}] - {number}")

                options = int(input("Enter index options you chooose: "))
            except ValueError:
                print("You need to enter a number")
                continue
            if options not in list(range(len(rapport_menu))):
                print("your choise is out of scope")
                continue

            elif options in [0, 1]:

                try:
                    for index, sub_option in enumerate(under_rapport_menu):
                        print(f"[{index}] - {sub_option}")
                        sub_option = int(input("Enter the index options that you choose : "))
                except ValueError:
                    print("you need to choose a number")
                if options not in list(range(len(under_rapport_menu))):
                    print("the number that you choose doesn't exist")
                    continue
                break
            else:
                break
        return self.options, self.sub_options

    def ask_validation(self, msg):
        print(msg)
        print('[0] - Yes\n[1] - No\n')
        self.options = input('your answer : ')
        return self.options