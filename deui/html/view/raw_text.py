from ..engine import HTMLWidget
from ...core.view import View


class RawText(HTMLWidget, View):
    """
    Represents raw text which may contains HTML elements.
    You should not use this element for display user content.
    """

    def __init__(self, value):
        self.widget = self
        self.view_context = self
        self.value = value
        super().__init__()

    def __str__(self):
        return self.value

    def draw_began(self):
        self.representation += f"{self.value}\n"

    def draw_ended(self):
        pass
