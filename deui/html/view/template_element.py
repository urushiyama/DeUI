from .element import Element


class Template(Element):
    """
    Holds HTML template for post-processing.
    """

    def __str__(self):
        return "template"
