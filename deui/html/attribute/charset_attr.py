from .attribute_builder import AttributeBuilder


class CharacterSet(AttributeBuilder):
    """
    Represents 'charset' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["charset"]
