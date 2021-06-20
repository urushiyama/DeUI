from .element import Element

from ..attribute.composite import Common
from ..attribute import AttributeRenderer, Form, Maximum, Value


class Progress(Element):
    """
    Represents task's progress.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Form(),
        Maximum(),
        Value()
    )

    def __str__(self):
        return "progress"
