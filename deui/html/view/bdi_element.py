from .element import Element


class Bidirectional(Element):
    """
    Indicates that surrounded text is isolated from default directonality of text.
    """

    def __str__(self):
        return "bdi"
