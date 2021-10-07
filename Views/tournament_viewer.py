from Models.tournament import Tournament


class TournamentView:
    input = {}

    def __init__(self, tournament):
        self.tournament = tournament

    def new_tournament_display(self):
        print("{Welcome to the Tournament Menu}")
        for key, entry in self.tournament.object():
            print(f"{key}: {entry.option}")

    def get_new_tournament_information(self):
        while True:
            self.tournament_name = input("Enter the name of this tournament: ")
            self.tournament_location = input("enter the localisaiton of this Tournament: ")
            self.tournament_start_date = input("Enter the start date of this Tournament (DD/MM/YYYY) : ")
            self.tournament_end_date = input("Enter the end date of this tournament (DD/MM/YYYY) : ")
            self.tournament_player_number = input("Enter the number of player : ")
            self.tournament_max_turn = input("Enter the number of turn : ")
            self.tournament_play_style = input("Enter the gamestyle of this Tournament (bullet / blitz / rush) : ")

            return Tournament(self.tournament_name, self.tournament_location, self.tournament_start_date,
                    self.tournament_end_date,  self.tournament_player_number, self.tournament_max_turn,
                    self.tournament_play_style)






            # self.new_tournament_display()
            # choice = input(">>")
            # if choice in self.tournament:
            #     return self.tournament[choice]
            # break



