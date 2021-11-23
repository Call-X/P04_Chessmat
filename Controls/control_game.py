from Data_base import DataBaseService
from Controls.home_menu_control import HomeMenuControl



class ControlGame:
    def __init__(self):
        self.control = None

    def load(self):
        db = DataBaseService()
        db.load()

    def start(self):
        self.control = HomeMenuControl()
        self.load()
        while self.control:
            self.control = self.control()



















