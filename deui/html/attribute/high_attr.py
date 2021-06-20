from .attribute_builder import AttributeBuilder


class High(AttributeBuilder):
    """
    Represents 'high' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["high"]
