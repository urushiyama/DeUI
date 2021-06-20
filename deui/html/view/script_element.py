from .element import Element

from ..attribute.composite import Common
from ..attribute import (
    AttributeRenderer,
    Asynchronous, CharacterSet, CrossOrigin,
    Defer, Integrity, ReferrerPolicy, Source, Type
)


class Script(Element):
    """
    Embeds code or data.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Asynchronous(),
        CharacterSet(),
        CrossOrigin(),
        Defer(),
        Integrity(),
        ReferrerPolicy(),
        Source(),
        Type()
    )

    def __str__(self):
        return "script"
