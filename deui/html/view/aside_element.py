from .element import Element


class Aside(Element):
    """
    Represents document part which is not directly related to the main part.
    """

    def __str__(self):
        return "aside"
