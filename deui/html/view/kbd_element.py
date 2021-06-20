from .element import Element


class Keyboard(Element):
    """
    Represents inline text that user input.
    """

    def __str__(self):
        return "kbd"
