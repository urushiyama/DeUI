from .attribute_builder import AttributeBuilder


class Default(AttributeBuilder):
    """
    Represents 'default' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["default"]
