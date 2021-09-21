
from Controls.home_menu_control import HomeMenuControl


class ControlGame:
    def __init__(self):
        self.control = None

    def start(self):
        self.control = HomeMenuControl()
        while self.control:
            self.control = self.control()



















