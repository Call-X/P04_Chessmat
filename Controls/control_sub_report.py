from Controls.control_player import PlayerControl
from Controls.control_screen import ScreenControl
from Models.sub_report_menu import SubReportMenu
from Views.sub_report_menu_viewer import SubReportMenuView
# from Controls.home_menu_control import HomeMenuControl


class SubReportMenuControl:

    def __init__(self):

        self.menu = SubReportMenu()
        self.view = SubReportMenuView(self.menu)

    def __call__(self):
        print("Consulting the sub-report menu or want to quit")
        self.menu._add_menu("auto", "By id  ", PlayerControl()), "\n"
        self.menu._add_menu("auto", "By ranking ", PlayerControl()), "\n"
        # self.menu._add_menu("r", "return", HomeMenuControl())
        self.menu._add_menu("q", "quit", ScreenControl())

        user_choice = self.view.get_user_sub_choice()
        return user_choice.handler
