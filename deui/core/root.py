from .widget import Widget


class Root(Widget):
    def __str__(self):
        return "Root"

    def draw_began(self):
        pass

    def draw_ended(self):
        pass
