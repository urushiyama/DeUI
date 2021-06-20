from .element import Element

from ..attribute.composite import Common
from ..attribute import AttributeRenderer, Value


class ListItem(Element):
    """
    Represents list item.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Value()
    )

    def __str__(self):
        return "li"
