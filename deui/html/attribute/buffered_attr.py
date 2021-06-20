from .attribute_builder import AttributeBuilder


class Buffered(AttributeBuilder):
    """
    Represents 'buffered' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["buffered"]
