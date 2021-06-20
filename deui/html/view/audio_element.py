from .element import Element

from ..attribute.composite import Common
from ..attribute import (
    AttributeRenderer,
    Autoplay, Buffered, Controls, CrossOrigin,
    Loop, Muted, Preload, Source
)


class Audio(Element):
    """
    Embeds sound content.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Autoplay(),
        Buffered(),
        Controls(),
        CrossOrigin(),
        Loop(),
        Muted(),
        Preload(),
        Source()
    )

    def __str__(self):
        return "audio"
