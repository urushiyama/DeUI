from ..engine import HTMLWidget


class Element(HTMLWidget):
    """
    Represents element which may have children.
    """

    def __str__(self):
        return "element"

    def draw_began(self):
        self.representation += f"<{str(self)}{type(self).attribute_renderer.attributes(self)}>\n"

    def draw_ended(self):
        self.representation += f"</{str(self)}>\n"
