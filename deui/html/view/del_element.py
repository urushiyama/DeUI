from .element import Element

from ..attribute.composite import Common
from ..attribute import AttributeRenderer, Cite, DateTime


class Deleted(Element):
    """
    Represents deleted content.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Cite(),
        DateTime()
    )

    def __str__(self):
        return "del"
