from .attribute_builder import AttributeBuilder


class Pattern(AttributeBuilder):
    """
    Represents 'pattern' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["pattern"]
