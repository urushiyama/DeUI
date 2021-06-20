from .element import Element

from ..attribute.composite import Common, HasFixedSize
from ..attribute import (
    AttributeRenderer,
    Autoplay, Buffered, Controls, CrossOrigin,
    CurrentTime, Loop, Muted, PlaysInline,
    Poster, Preload, Source
)


class Video(Element):
    """
    Embeds media player which supports video.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        *HasFixedSize(),
        Autoplay(),
        Buffered(),
        Controls(),
        CrossOrigin(),
        CurrentTime(),
        Loop(),
        Muted(),
        PlaysInline(),
        Poster(),
        Preload(),
        Source()
    )

    def __str__(self):
        return "video"
