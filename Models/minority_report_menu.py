class MinorityReportMenuInput:
    def __init__(self, option, handler):
        self.option = option
        self.handler = handler


class MinorityReportMenu:
    def __init__(self):
        self._entries = {}
        self.autokey = 1

    def _add_menu(self, key, option, handler):
        if key == "auto":
            key = str(self.autokey)
            self.autokey += 1
        self._entries[str(key)] = MinorityReportMenuInput(option, handler)

    def object(self):
        return self._entries.items()

    def __contains__(self, choice):
        return str(choice) in self._entries

    def __getitem__(self, choice):
        return self._entries[choice]