from .element import Element


class NoScript(Element):
    """
    Wraps HTML elements when script cannot be executed.
    """

    def __str__(self):
        return "noscript"
