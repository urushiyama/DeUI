from .attribute_builder import AttributeBuilder


class Decoding(AttributeBuilder):
    """
    Represents 'decoding' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["decoding"]
