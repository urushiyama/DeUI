from .attribute_builder import AttributeBuilder


class Source(AttributeBuilder):
    """
    Represents 'src' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["src"]
