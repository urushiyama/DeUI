from .attribute_builder import AttributeBuilder


class FormTarget(AttributeBuilder):
    """
    Represents 'formtarget' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["formtarget"]
