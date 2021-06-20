from .element import Element

from ..attribute.composite import Common
from ..attribute import AttributeRenderer, Span


class ColumnGroup(Element):
    """
    Defines group of columns within table.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Span()
    )

    def __str__(self):
        return "colgroup"
