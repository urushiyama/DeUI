from .element import Element

from ..attribute.composite import Common
from ..attribute import AttributeRenderer, For, Form, Name


class Output(Element):
    """
    Represents container
    which website or app can insert their output.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        For(),
        Form(),
        Name()
    )

    def __str__(self):
        return "output"
