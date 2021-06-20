from .attribute_builder import AttributeBuilder


class HTTPEquivalent(AttributeBuilder):
    """
    Represents 'http-equiv' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["http-equiv"]
