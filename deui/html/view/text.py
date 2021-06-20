import html

from ..engine import HTMLWidget
from ...core.view import View


class Text(HTMLWidget, View):
    """
    Represents escaped text.
    """

    def __init__(self, value):
        self.widget = self
        self.view_context = self
        self.value = value
        super().__init__()

    def __str__(self):
        return self.value

    def draw_began(self):
        self.representation += f"{html.escape(self.value)}\n"

    def draw_ended(self):
        pass
