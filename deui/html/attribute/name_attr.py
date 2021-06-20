from .attribute_builder import AttributeBuilder


class Name(AttributeBuilder):
    """
    Represents 'name' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["name"]
