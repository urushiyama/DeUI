from .attribute_builder import AttributeBuilder


class Shape(AttributeBuilder):
    """
    Represents 'shape' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["shape"]
