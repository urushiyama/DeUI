from .element import Element

from ..attribute.composite import Common
from ..attribute import (
    AttributeRenderer,
    Autocomplete, Columns,
    DirectionName, Disabled, Form,
    MaximumLength, MinimumLength,
    Name, Placeholder, ReadOnly,
    Required, Rows, Wrap
)


class TextArea(Element):
    """
    Represents multi-line plain-text editing control.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Autocomplete(),
        Columns(),
        DirectionName(),
        Disabled(),
        Form(),
        MaximumLength(),
        MinimumLength(),
        Name(),
        Placeholder(),
        ReadOnly(),
        Required(),
        Rows(),
        Wrap()
    )

    def __str__(self):
        return "textarea"
