from .attribute_builder import AttributeBuilder


class Alternative(AttributeBuilder):
    """
    Represents 'alt' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["alt"]
