from Views.player_viewer import PlayerView


class Player:

    def __init__(self, choice=None):
        self.choice = choice
        self.next = None
        self.view = PlayerView

    # def player_list(self):
    #     while True :
    #         self.player[ choice ].append



