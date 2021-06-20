from .attribute_builder import AttributeBuilder


class Required(AttributeBuilder):
    """
    Represents 'required' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["required"]
