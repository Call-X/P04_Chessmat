from Controls.control_player import PlayerControl
from Views.round_viewer import RoundView

class RoundControl:
    def __call__(self):
        print("Creat the Round's options")

        self.view = RoundView
        self.player_control = PlayerControl()
