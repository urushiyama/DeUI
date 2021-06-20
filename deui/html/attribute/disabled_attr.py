from .attribute_builder import AttributeBuilder


class Disabled(AttributeBuilder):
    """
    Represents 'disabled' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["disabled"]
