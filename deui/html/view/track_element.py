from .void_element import VoidElement

from ..attribute.composite import Common
from ..attribute import (
    AttributeRenderer,
    Default, Kind, Label, Source, SourceLanguage
)


class Track(VoidElement):
    """
    Specifies timed text track or time-based data to audio or video content.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Default(),
        Kind(),
        Label(),
        Source(),
        SourceLanguage()
    )

    def __str__(self):
        return "track"
