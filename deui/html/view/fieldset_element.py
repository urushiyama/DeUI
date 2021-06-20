from .element import Element

from ..attribute.composite import Common
from ..attribute import AttributeRenderer, Disabled, Form, Name


class FieldSet(Element):
    """
    Represents group of controls.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Disabled(),
        Form(),
        Name()
    )

    def __str__(self):
        return "fieldset"
