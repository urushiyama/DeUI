from .attribute_builder import AttributeBuilder


class Method(AttributeBuilder):
    """
    Represents 'method' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["method"]
