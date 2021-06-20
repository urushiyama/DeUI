from .attribute_builder import AttributeBuilder


class Coordinates(AttributeBuilder):
    """
    Represents 'coords' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["coords"]
