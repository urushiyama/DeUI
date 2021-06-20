from .element import Element

from ..attribute.composite import Common
from ..attribute import (
    AttributeRenderer,
    Disabled, Label, Selected, Value
)


class Option(Element):
    """
    Represents option for select box.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Disabled(),
        Label(),
        Selected(),
        Value()
    )

    def __str__(self):
        return "option"
