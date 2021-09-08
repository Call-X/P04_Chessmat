class MinorityReportMenu:
    input = {}

    def __init__(self, menu):
        self.menu = menu

    def minority_report_menu_display(self):
        print("Welcome to the Sub-Report-Menu")
        for key, entry in self.menu.object():
            print(f"{key}: {entry.option}")

            # retourner de le choix de l'utilisateur

    def get_user_minority_choice(self):
        while True:
            self.minority_report_menu_display()
            choice = input(">>")
            if choice in self.menu:
                print("°°°You are in°°° : ")
                return self.menu[choice]

            elif choice not in self.menu:
                print('$$$ Option no available, "\n', "Please enter a number between 1 and 2 $$$")

                continue
            else:
                break
