from .element import Element

from ..attribute.composite import Common
from ..attribute import (
    AttributeRenderer,
    Disabled, Label
)


class OptionGroup(Element):
    """
    Wraps select box's options as a group.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Disabled(),
        Label()
    )

    def __str__(self):
        return "optgroup"
