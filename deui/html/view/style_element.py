from .element import Element

from ..attribute.composite import Common
from ..attribute import (
    AttributeRenderer,
    Media, Type
)


class Style(Element):
    """
    Embeds style information.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Media(),
        Type()
    )

    def __str__(self):
        return "style"
