

class MenuInput:
    def __init__(self, option, handler):
        self.option = option
        self.handler = handler



class Menu:
    def __init__(self):
        self._entries = {}
        self.autokey = 1


    def append(self, key, option, handler):
        if key == "auto":
            key = str(self.autokey)
            self.autokey += 1
        self._entries[str(key)] = MenuInput(option, handler)

    def items(self):
        return self._entries.items()

    def __contains__(self, choice):
        return str(choice) in self._entries

    def __getitem__(self, choice):
        return self._entries[choice]





# if __name__ == '__main__':
#     menu = Menu()
#     menu.append("auto", "Tounament Launcher", NewTournamentControl()), "\n",
#     menu.append("auto", "create player", PlayerControl()), "\n",
#     menu.append("auto", "Ranking modification", RankingControl()), "\n",
#     menu.append("auto", "Minority menu ", MinorityReportMenuControl()), "\n",
#     menu.append("auto", "Sub-report menu", SubReportMenuControl()), "\n",
#     menu.append("auto", "Quit", SubReportMenuControl()), "\n"
#     print(menu._entries)









