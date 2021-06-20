from .void_element import VoidElement
from ..attribute.composite import Common, HasFixedSize
from ..attribute import (
    AttributeRenderer,
    Accept, Alternative, Autocomplete,
    Capture, Checked, DirectionName,
    Disabled, Form, FormAction, FormEncodingType,
    FormMethod, FormNoValidate, FormTarget, List,
    Maximum, MaximumLength, Minimum, MinimumLength,
    Multiple, Name, Pattern, Placeholder, ReadOnly,
    Required, Size, Source, Step, Type, UseMap, Value
)


class Input(VoidElement):
    """
    Represents interactive controls to accept data from user.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        *HasFixedSize(),
        Accept(),
        Alternative(),
        Autocomplete(),
        Capture(),
        Checked(),
        DirectionName(),
        Disabled(),
        Form(),
        FormAction(),
        FormEncodingType(),
        FormMethod(),
        FormNoValidate(),
        FormTarget(),
        List(),
        Maximum(),
        MaximumLength(),
        MinimumLength(),
        Minimum(),
        Multiple(),
        Name(),
        Pattern(),
        Placeholder(),
        ReadOnly(),
        Required(),
        Size(),
        Source(),
        Step(),
        Type(),
        UseMap(),
        Value()
    )

    def __str__(self):
        return "input"
