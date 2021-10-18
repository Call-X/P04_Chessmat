from Models.round import Round
from Models.match import Match


class RoundView:
    input = {}

    def __init__(self):
        self.round = round
        self.round_number = "round_number"
        self.round_name = "round_name"

    def create_round(self):
        while True:
            self.round_number = input("Enter the number of the round: ")
            self.round_name = input("Enter the name of the round: ")
            return Round(self.round_name, self.round_number)

