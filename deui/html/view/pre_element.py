from .element import Element


class Preformatted(Element):
    """
    Represents preformatted text.
    """

    def __str__(self):
        return "pre"
