from .void_element import VoidElement

from ..attribute.composite import Common
from ..attribute import (
    AttributeRenderer,
    CharacterSet, Content, HTTPEquivalent, Name
)


class Meta(VoidElement):
    """
    Represents metadata.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        CharacterSet(),
        Content(),
        HTTPEquivalent(),
        Name()
    )

    def __str__(self):
        return "meta"
