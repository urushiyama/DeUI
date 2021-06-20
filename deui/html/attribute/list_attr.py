from .attribute_builder import AttributeBuilder


class List(AttributeBuilder):
    """
    Represents 'list' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["list"]
