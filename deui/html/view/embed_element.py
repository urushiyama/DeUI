from .void_element import VoidElement

from ..attribute.composite import Common, HasFixedSize
from ..attribute import AttributeRenderer, Source, Type


class Embed(VoidElement):
    """
    Embeds external content.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        *HasFixedSize(),
        Source(),
        Type()
    )

    def __str__(self):
        return "embed"
