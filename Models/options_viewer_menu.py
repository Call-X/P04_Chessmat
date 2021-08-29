from Controls.control_game import *

class MenuInput:
    def __init__(self, option, handler):
        self.option = option
        self.handler = handler

    def __repr__(self):
        return f"MenuInput({self.option},{self.handler})"

class Menu:
    def __init__(self):
        self.input = {}
        self.autokey = 1


    def append(self, key, option, handler):
        if key == "auto":
            key = str(self.autokey)
            self.autokey += 1
        self.input[str(key)] = MenuInput(option, handler)

    def items(self):
        return self.input.items()

    def __contains__(self, choice):
        return str(choice) in self.input

    def __getitem__(self, choice):
        return self.input[choice]





# if __name__ == '__main__':
#     menu = Menu()
#     menu.append("auto", "Tounament Launcher", NewTournamentControl()), "\n",
#     menu.append("auto", "create player", PlayerControl()), "\n",
#     menu.append("auto", "Ranking modification", RankingControl()), "\n",
#     menu.append("auto", "Minority menu ", MinorityReportMenuControl()), "\n",
#     menu.append("auto", "Sub-report menu", SubReportMenuControl()), "\n",
#     menu.append("auto", "Quit", SubReportMenuControl()), "\n"
#     print(menu.input)









