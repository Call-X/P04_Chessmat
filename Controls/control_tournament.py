from Views.tournament_viewer import TournamentView
from Views.player_viewer import PlayerView
from Controls.home_menu_control import HomeMenuControl
from Models.match import Match
from Models.player import Player
from Models.round import Round
from Data_base import db
from Models.tournament import Tournament
from datetime import datetime
from collections import OrderedDict


class TournamentControl:

    def __init__(self):
        self.tournament_menu = TournamentMenu()
        self.view = TournamentView(self.tournament_menu)
        self.player = PlayerView
        self.home_menu = HomeMenuControl()
        self.round = Round
        self.player = Player
        self.DatabaseService = db
        self.match = Match
        self.tournament = Tournament

    def __call__(self):
        print("{Tournament Management}")

        choice = self.view.choose_option_tournament()

        # Create a Tournament
        if choice == "1":
            tournament = self.view.get_new_tournament_information()
            db.insert_data_tournament(tournament)

            print("{°°°Tournament is created with succes°°°}")
            choice = self.view.choose_option_tournament()

        # Select Tournament
        if choice == "2":
            choice_select = self.view.select_options_tournament()

            if choice_select == "1":
                tournament_id = self.view.display_all_tournaments_and_choose_one(db.gb_tournaments)
                self.view.display_all_informations_for_one_tournament(db.gb_tournaments[int(tournament_id)])
                self.home_menu_control = self.home_menu()

            # Add a player to a tournament
            if choice_select == "2":
                tournament_id = self.view.display_all_tournaments_and_choose_one(db.gb_tournaments)
                player_id = self.view.display_all_players_and_choose_one(db.gb_players, db.gb_tournaments[int(tournament_id)])
                db.add_player_into_tournament(int(player_id), int(tournament_id))

                print("{°°°Player added with sucess°°°}")
                self.home_menu_control = self.home_menu()

        if choice == "3":
            self.home_menu_control = self.home_menu()

        if choice == "4":
            tournament_id = self.view.display_all_tournaments_and_choose_one(db.gb_tournaments)
            tournament = db.gb_tournaments[int(tournament_id)]
            self.launch_tournament(tournament)

    # For debug purpose
    def notify(self, txt_type, text):
        balise = ""
        if txt_type == 'ERROR':
            balise = " ! "
        elif txt_type == "SUCCESS":
            balise = ' ▼ '

        print('\n' + balise + text + balise + '\n')

    def launch_tournament(self, tournament):
        if tournament is None:
            return None
        if len(db.gb_tournaments[int(tournament.id)].players) < 4:
            self.notify("ERROR", 'This tournament contain only ' + str(len(db.gb_tournaments[int(tournament.id)].players)) +
                        ' players. Add more players please.')
            return None
        if (len(tournament.players) % 2) != 0:
            self.notify("ERROR", "Impossible to start a tournament with an odd number players"
                                 "( " + str(len(tournament.players)) + ' )')
            return None
        print('\n')
        print('Your are playing to the tournament named : ' + tournament.name)
        print('\n')
        print(' ---ROUND ONE : MATCHS--- ')
        print('\n')
        rounds = self.pairing(tournament)
        tournament.rounds = []
        if len(tournament.rounds) < 2:
            self.notify("ERROR", " All matchs of this tournaments :  " + tournament.name + " have been played.")
            self.notify("SUCCESS", "the tournament :" + tournament.name + " is over")
            return None
        self.notify('SUCCESS', str(len(tournament.rounds)) + " Rounds which figure in the tournament")
        return rounds, tournament

    def pairing(self, tournament):
        if len(tournament.round_list) == 0:
            players_sorted = OrderedDict(sorted(tournament.players.items(), key=lambda player: player[1].rank))
            length = len(players_sorted)
            median = length // 2

            now = datetime.now()
            round_name = 'Round ' + str(len(tournament.round_list) + 1)
            start_time = str(now.hour) + ':' + str(now.minute)
            round = Round(1, tournament.id, round_name, start_time)
            round_id = db.insert_data_rounds_in_tournament(round)
            new_round = Round(round_id, tournament.id, round_name, start_time)
            # tournament.add_round(tournament, new_round)
            for i in range(median):
                match = Match(i, new_round.id, players_sorted[i], players_sorted[i + median])
                match_id = db.insert_data_matchs(match)
                Round.add_match(round, match)
            self.view.display_round(round)
            self.view.update_score(round)
        return True


class TournamentMenuInput:
    def __init__(self, option, handler):
        self.option = option
        self.handler = handler


class TournamentMenu:
    def __init__(self):
        self._entries = {}
        self.autokey = 1

    def _add_menu(self, key, option, handler):
        if key == "auto":
            key = str(self.autokey)
            self.autokey += 1

        self._entries[str(key)] = TournamentMenuInput(option, handler)

    def object(self):
        return self._entries.items()

    def __contains__(self, choice):
        return str(choice) in self._entries

    def __getitem__(self, choice):
        return self._entries[choice]
