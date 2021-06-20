from .element import Element

from ..attribute.composite import Common
from ..attribute import AttributeRenderer, Cite


class Quote(Element):
    """
    Represents inline quote.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Cite()
    )

    def __str__(self):
        return "q"
