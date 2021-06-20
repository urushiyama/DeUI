from .attribute_builder import AttributeBuilder


class Minimum(AttributeBuilder):
    """
    Represents 'minimum' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["minimum"]
