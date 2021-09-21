from Views.player_viewer import PlayerView





class PlayerControl:
    def __init__(self):
        self.player = PlayerMenu()
        self.view = PlayerView(self.player)
        self.player_list = []

    def __call__(self):
        print("~~~ Create or Modify a Player ~~~ ")
        while True:
        #demander a la vue d'afficher le menu et collecter la réponse de 'lutilisateur
            user_choice = self.view.get_new_player()

            return user_choice


class PlayerMenuInput:
    def __init__(self, option, handler):
        self.option = option
        self.handler = handler


class PlayerMenu:
    def __init__(self):
        self._entries = {}
        self.autokey = 1

    def _add_menu(self, key, option, handler):
        if key == "auto":
            key = str(self.autokey)
            self.autokey += 1

        self._entries[str(key)] = PlayerMenuInput(option, handler)

    def object(self):
        return self._entries.items()

    def __contains__(self, choice):
        return str(choice) in self._entries

    def __getitem__(self, choice):
        return self._entries[choice]








