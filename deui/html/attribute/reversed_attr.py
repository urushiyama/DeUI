from .attribute_builder import AttributeBuilder


class Reversed(AttributeBuilder):
    """
    Represents 'reversed' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["reversed"]
