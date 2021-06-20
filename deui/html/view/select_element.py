from .element import Element

from ..attribute.composite import Common
from ..attribute import (
    AttributeRenderer,
    Autocomplete, Disabled, Form,
    Multiple, Name, Required, Size
)


class Select(Element):
    """
    Represents select box.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Autocomplete(),
        Disabled(),
        Form(),
        Multiple(),
        Name(),
        Required(),
        Size()
    )

    def __str__(self):
        return "select"
