from .void_element import VoidElement


class HorizontalRule(VoidElement):
    """
    Represents thematic break between contents.
    """

    def __str__(self):
        return "hr"
