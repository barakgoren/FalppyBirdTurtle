# ------ 5 --------
# topWidth = 9
# topY = 385
# botWidth = 15
# botY = 50

class Position:
    def __init__(self, top_width, top_y, bot_width, bot_y):
        self._top_width = top_width
        self._top_y = top_y
        self._bot_width = bot_width
        self._bot_y = bot_y

    def get_top_width(self):
        return self._top_width

    def set_top_width(self, value):
        self._top_width = value

    def get_top_y(self):
        return self._top_y

    def set_top_y(self, value):
        self._top_y = value

    def get_bot_width(self):
        return self._bot_width

    def set_bot_width(self, value):
        self._bot_width = value

    def get_bot_y(self):
        return self._bot_y

    def set_bot_y(self, value):
        self._bot_y = value

