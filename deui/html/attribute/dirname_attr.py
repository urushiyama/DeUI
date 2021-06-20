from .attribute_builder import AttributeBuilder


class DirectionName(AttributeBuilder):
    """
    Represents 'dirname' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["dirname"]
