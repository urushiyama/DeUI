from .void_element import VoidElement

from ..attribute.composite import Common
from ..attribute import (
    AttributeRenderer,
    Media, Sizes, Source as SourceAttr, SourceSet, Type
)


class Source(VoidElement):
    """
    Specifies media resource.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Media(),
        Sizes(),
        SourceAttr(),
        SourceSet(),
        Type()
    )

    def __str__(self):
        return "source"
