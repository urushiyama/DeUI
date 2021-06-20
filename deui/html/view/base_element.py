from .void_element import VoidElement

from ..attribute.composite import Common
from ..attribute import (
    AttributeRenderer,
    HypertextReference, Target
)


class Base(VoidElement):
    """
    Specifies base of URL.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        HypertextReference(),
        Target()
    )

    def __str__(self):
        return "base"
