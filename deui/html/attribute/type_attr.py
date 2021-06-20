from .attribute_builder import AttributeBuilder


class Type(AttributeBuilder):
    """
    Represents 'type' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["type"]
