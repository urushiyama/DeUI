from .void_element import VoidElement

from ..attribute.composite import Common, Linkable
from ..attribute import (
    AttributeRenderer,
    As, CrossOrigin, Disabled, ImageSizes, ImageSourceSet, Integrity, Sizes, Type
)


class Link(VoidElement):
    """
    Represents link to external resource.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        *Linkable(),
        As(),
        CrossOrigin(),
        Disabled(),
        ImageSizes(),
        ImageSourceSet(),
        Integrity(),
        Sizes(),
        Type(),
    )

    def __str__(self):
        return "link"
