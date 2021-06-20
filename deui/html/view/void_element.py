from ..engine import HTMLWidget


class VoidElement(HTMLWidget):
    """
    Represents element which has no child.
    """

    def __str__(self):
        return "element"

    def draw_began(self):
        self.representation += f"<{str(self)}{type(self).attribute_renderer.attributes(self)} />\n"

    def draw_ended(self):
        pass
