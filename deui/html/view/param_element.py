from .void_element import VoidElement

from ..attribute.composite import Common
from ..attribute import AttributeRenderer, Name, Value


class Parameter(VoidElement):
    """
    Represents parameter for object element.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Name(),
        Value()
    )

    def __str__(self):
        return "param"
