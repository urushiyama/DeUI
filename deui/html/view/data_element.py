from .element import Element

from ..attribute.composite import Common
from ..attribute import AttributeRenderer, Value


class Data(Element):
    """
    Provides machine-readable data.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Value()
    )

    def __str__(self):
        return "data"
