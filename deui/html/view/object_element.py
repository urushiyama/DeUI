from .element import Element

from ..attribute.composite import Common, HasFixedSize
from ..attribute import (
    AttributeRenderer,
    Data, Form, Name, Type, UseMap
)


class Object(Element):
    """
    Embeds external resource.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        *HasFixedSize(),
        Data(),
        Form(),
        Name(),
        Type(),
        UseMap()
    )

    def __str__(self):
        return "object"
