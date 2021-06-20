from .element import Element

from ..attribute.composite import Common
from ..attribute import AttributeRenderer, For, Form


class Label(Element):
    """
    Represents label of controls.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        For(),
        Form()
    )

    def __str__(self):
        return "label"
