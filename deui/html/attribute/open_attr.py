from .attribute_builder import AttributeBuilder


class Open(AttributeBuilder):
    """
    Represents 'open' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["open"]
