from .element import Element

from ..attribute.composite import Common
from ..attribute import AttributeRenderer, Start, Reversed, Type


class OrderedList(Element):
    """
    Wraps ordered list.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Start(),
        Reversed(),
        Type()
    )

    def __str__(self):
        return "ol"
