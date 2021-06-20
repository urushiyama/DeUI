from .element import Element

from ..attribute.composite import Common
from ..attribute import (
    AttributeRenderer,
    Form, High, Low, Maximum, Minimum,
    Optimum, Value
)


class Meter(Element):
    """
    Represents meter to display value in a certain range.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Form(),
        High(),
        Low(),
        Maximum(),
        Minimum(),
        Optimum(),
        Value()
    )

    def __str__(self):
        return "meter"
