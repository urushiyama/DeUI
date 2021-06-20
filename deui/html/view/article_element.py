from .element import Element


class Article(Element):
    """
    Represents independent article part of document.
    """

    def __str__(self):
        return "article"
