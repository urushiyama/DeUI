from .element import Element

from ..attribute.composite import Common
from ..attribute import AttributeRenderer, Cite


class BlockQuote(Element):
    """
    Represents quoted content.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Cite()
    )

    def __str__(self):
        return "blockquote"
