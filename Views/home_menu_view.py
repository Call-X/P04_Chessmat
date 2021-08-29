from Models.options_viewer_menu import Menu


# report_menu = [
#     "Player list", "\n", "Current player list", "\n", "All tournament list", "\n",
#     "All match list of the Tournament", "\n", "All round list of the Tournament", "\n", "Return"]
#
# sub_report_menu = ["By letter", "\n", "By ranking"]

# affichage du menu aux utilisateurs


class HomeMenuView:
    input = {}


    def __init__(self, menu):
        self.menu = Menu()

    def menu_display(self):
        print("Welcome to the Game Menu")
        for key, entry in self.menu.items():
            print(f"{key}: {entry.option}")



            # retourner de le choix de l'utilisateur

    def get_user_choice(self):
        # while True:
        #     self.menu_display()
        #     if choice in self.menu:
        #         return self.menu(choice)
        while True:

            try:
                print("[1] Tournament Launcher",
                      "[2] Add player",
                      "[3] Modifie a ranking player",
                      "[4] Minority Report",
                      "[5] Quit",
                      "CHOOSE YOUR OPTION : ",
                      sep='\n')
                choice = input()
                if choice in self.menu:
                    print('you are in')

                elif choice not in self.menu:
                    print('Option no available')
                    continue
                else:
                    break
            except ValueError:
                print('ENTER A NUMBER')
                continue

        return self.menu.choice


=

    #     while True:
    #         try:
    #             for key, option in enumerate(menus):
    #                 print(f"[{key}] - {option}")
    #
    #             user_choice = int(input("Enter index options you choose: "))
    #         except ValueError:
    #             print("You need to enter a number")
    #             continue
    #         if user_choice not in list(range(len(menus))):
    #             print("your option is out of scope")
    #             continue
    #
    #         elif sub_user_choice in [0, 1]:
    #
    #             try:
    #                 for key, sub_user_choice in enumerate(report_menu):
    #                     print(f"[{key}] - {sub_user_choice}")
    #                     sub_user_choice = int(input("Enter the index options that you choose : "))
    #             except ValueError:
    #                 print("you need to choose a number")
    #             if sub_user_choice not in list(range(len(report_menu))):
    #                 print("the number that you choose doesn't exist")
    #                 continue
    #             break
    #         else:
    #             break
    #
    #     return user_choice, sub_user_choice
# validation du choix de l'utilisateur

    # def ask_validation(self, msg):

        # print(msg)
        # print('[0] - Yes\n[1] - No\n')
        # user_choice = input('your answer : ')
        # return user_choice

# if __name__ == '__main__':
#     menu = HomeMenuView()
#     menu.OptionsViewerMenu()
#     menu.get_user_choice()




