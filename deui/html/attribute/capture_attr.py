from .attribute_builder import AttributeBuilder


class Capture(AttributeBuilder):
    """
    Represents 'capture' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["capture"]
