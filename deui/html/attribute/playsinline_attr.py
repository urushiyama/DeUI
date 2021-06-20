from .attribute_builder import AttributeBuilder


class PlaysInline(AttributeBuilder):
    """
    Represents 'playsinline' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["playsinline"]
