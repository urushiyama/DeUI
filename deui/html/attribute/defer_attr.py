from .attribute_builder import AttributeBuilder


class Defer(AttributeBuilder):
    """
    Represents 'defer' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["defer"]
