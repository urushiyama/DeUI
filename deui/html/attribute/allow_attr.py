from .attribute_builder import AttributeBuilder


class Allow(AttributeBuilder):
    """
    Represents 'allow' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["allow"]
