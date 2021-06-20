from .element import Element

from ..attribute.composite import Common
from ..attribute import AttributeRenderer, DateTime


class Time(Element):
    """
    Represents a specific period in time.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        DateTime()
    )

    def __str__(self):
        return "time"
