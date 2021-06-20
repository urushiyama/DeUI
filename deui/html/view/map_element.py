from .element import Element

from ..attribute.composite import Common
from ..attribute import AttributeRenderer, Name


class Map(Element):
    """
    Represents image map to define clickable link area.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Name()
    )

    def __str__(self):
        return "map"
