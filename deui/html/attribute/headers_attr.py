from .attribute_builder import AttributeBuilder


class Headers(AttributeBuilder):
    """
    Represents 'headers' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["headers"]
