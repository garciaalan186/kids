class Kid:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.not_me = not self

    def every_waking_moment(self):
        while self.parent.attention(self.not_me):
            self.parent.attention(self)
