from .void_element import VoidElement

from ..attribute.composite import Common, Linkable
from ..attribute import (
    AttributeRenderer,
    Alternative, Coordinates,
    Download, Ping, Shape, Target
)


class Area(VoidElement):
    """
    Represents clickable area.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        *Linkable(),
        Alternative(),
        Coordinates(),
        Download(),
        Ping(),
        Shape(),
        Target()
    )

    def __str__(self):
        return "area"
