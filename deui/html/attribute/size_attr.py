from .attribute_builder import AttributeBuilder


class Size(AttributeBuilder):
    """
    Represents 'size' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["size"]
