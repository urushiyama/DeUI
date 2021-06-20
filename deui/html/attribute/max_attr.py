from .attribute_builder import AttributeBuilder


class Maximum(AttributeBuilder):
    """
    Represents 'max' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["max"]
