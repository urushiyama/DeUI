from .void_element import VoidElement

from ..attribute.composite import Common
from ..attribute import AttributeRenderer, Span


class Column(VoidElement):
    """
    Defines column within table.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Span()
    )

    def __str__(self):
        return "col"
