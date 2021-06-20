from .attribute_builder import AttributeBuilder


class Height(AttributeBuilder):
    """
    Represents 'height' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["height"]
