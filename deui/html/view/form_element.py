from .element import Element

from ..attribute.composite import Common
from ..attribute import (
    AttributeRenderer,
    Accept, AcceptCharset,
    Action, Autocomplete, EncodingType,
    Method, Name, NoValidate, Target
)


class Form(Element):
    """
    Represents form.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        Accept(),
        AcceptCharset(),
        Action(),
        Autocomplete(),
        EncodingType(),
        Method(),
        Name(),
        NoValidate(),
        Target()
    )

    def __str__(self):
        return "form"
