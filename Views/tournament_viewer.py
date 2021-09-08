class TournamentView:
    input = {}

    def __init__(self, tournament):
        self.tournament = tournament

    def new_tournament_display(self):
        print("{Welcome to the Tournament Menu}")
        for key, entry in self.tournament.object():
            print(f"{key}: {entry.option}")

    def get_new_tournament_indic(self):
        while True:
            self.new_tournament_display()
            choice = input(">>")
            if choice in self.tournament:
                return self.tournament[choice]
            break



