from .void_element import VoidElement

from ..attribute.composite import Common, HasFixedSize
from ..attribute import (
    AttributeRenderer,
    Alternative, CrossOrigin, Decoding, ReferrerPolicy, Sizes, Source, SourceSet, UseMap
)


class Image(VoidElement):
    """
    Represents image.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        *HasFixedSize(),
        Alternative(),
        CrossOrigin(),
        Decoding(),
        ReferrerPolicy(),
        Sizes(),
        Source(),
        SourceSet(),
        UseMap()
    )

    def __str__(self):
        return "img"
