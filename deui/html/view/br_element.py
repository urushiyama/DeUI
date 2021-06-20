from .void_element import VoidElement


class Break(VoidElement):
    """
    Represents line break.
    """

    def __str__(self):
        return "br"
