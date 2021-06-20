from .element import Element

from ..attribute.composite import Common, Linkable
from ..attribute import (
    AttributeRenderer,
    Download, Ping, Target, Type
)


class Anchor(Element):
    """
    Represents anchor to other resource.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        *Linkable(),
        Download(),
        Ping(),
        Target(),
        Type()
    )

    def __str__(self):
        return "a"
