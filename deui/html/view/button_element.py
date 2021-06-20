from .element import Element

from ..attribute.composite import Common
from ..attribute import (
    AttributeRenderer,
    Disabled, Form, FormAction, FormEncodingType,
    FormMethod, FormNoValidate, FormTarget,
    Name, Type, Value
)


class Button(Element):
    """
    Represents button.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Disabled(),
        Form(),
        FormAction(),
        FormEncodingType(),
        FormMethod(),
        FormNoValidate(),
        FormTarget(),
        Name(),
        Type(),
        Value()
    )

    def __str__(self):
        return "button"
