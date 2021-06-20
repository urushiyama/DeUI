from .element import Element

from ..attribute.composite import Common, HasFixedSize
from ..attribute import (
    AttributeRenderer
)


class Canvas(Element):
    """
    Represents canvas.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        *HasFixedSize()
    )

    def __str__(self):
        return "canvas"
