from Views.player_viewer import PlayerView
from Data_base import db


class PlayerControl:
    def __init__(self):
        self.player_menu = PlayerMenu()
        self.view = PlayerView(self.player_menu)

    def __call__(self):
        print("~~~ Player Management ~~~ ")

        choice = self.view.choose_option_player()

        # Create a player
        if choice == "1":
            player = self.view.get_new_player()
            db.insert_data_player(player)

        # Select Player
        if choice == "2":
            choice_select = self.view.select_options_players()

            if choice_select == "1":
                name = self.view.select_players_by_name()
                players = db.select_data_player_by_name(name)
                for player in players:
                    print(player)

            if choice_select == "2":
                rank = self.view.select_players_by_rank()
                players = db.select_data_player_order_by_rank(rank)
                for player in players:
                    print(player)

            if choice_select == "3":
                player_id = self.view.select_players_by_id()
                players = db.select_data_player_by_id(player_id)
                for player in players:
                    print(player)


        # select modification players
        if choice == "3":
            choice_select = self.view.select_modification_players()

            if choice_select == "1":
                player = self.view.update_player()
                db.update_player(player['familly_name'], player['first_name'], player['rank'], player['id'])
                # for player in players:
                print(player)

            if choice_select == "2":
                player_id = self.view.erase_player_by_id()
                db.erase_data_player_by_id(player_id)
                print(player_id)


    def select_all_players(self):
        db.select_all_players()


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








