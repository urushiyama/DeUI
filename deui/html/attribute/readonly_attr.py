from .attribute_builder import AttributeBuilder


class ReadOnly(AttributeBuilder):
    """
    Represents 'readonly' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["readonly"]
