from .attribute_builder import AttributeBuilder


class Ping(AttributeBuilder):
    """
    Represents 'ping' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["ping"]
