from .attribute_builder import AttributeBuilder


class Value(AttributeBuilder):
    """
    Represents 'value' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["value"]
