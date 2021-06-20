from .element import Element

from ..attribute.composite import Common
from ..attribute import AttributeRenderer, Open


class Details(Element):
    """
    Represents disclosure with expandable information.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Open()
    )

    def __str__(self):
        return "details"
