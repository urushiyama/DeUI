from .element import Element

from ..attribute.composite import Common, HasFixedSize
from ..attribute import (
    AttributeRenderer,
    Allow, Name, ReferrerPolicy,
    Sandbox, Source, SourceDocument
)


class InlineFrame(Element):
    """
    Represents inline frame.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        *HasFixedSize(),
        Allow(),
        Name(),
        ReferrerPolicy(),
        Sandbox(),
        Source(),
        SourceDocument()
    )

    def __str__(self):
        return "iframe"
