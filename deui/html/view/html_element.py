from ..engine import HTMLWidget

from ..attribute.composite import Common
from ..attribute import AttributeRenderer, XMLNamespace


class HTML(HTMLWidget):
    """
    Represents the root of HTML document.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        XMLNamespace()
    )

    def __str__(self):
        return "html"

    def draw_began(self):
        self.representation += ("<!DOCTYPE html>\n"
                                + f"<{str(self)}{type(self).attribute_renderer.attributes(self)}>\n")

    def draw_ended(self):
        self.representation += f"</{str(self)}>\n"
