from .element import Element


class BidirectionalOverride(Element):
    """
    Overrides direction of text.
    """

    def __str__(self):
        return "bdo"
