from .element import Element


class Variable(Element):
    """
    Represents name of a variable in mathematic expression or program.
    """

    def __str__(self):
        return "var"
