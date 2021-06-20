from .attribute_builder import AttributeBuilder


class Wrap(AttributeBuilder):
    """
    Represents 'wrap' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["wrap"]
