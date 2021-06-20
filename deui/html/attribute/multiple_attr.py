from .attribute_builder import AttributeBuilder


class Multiple(AttributeBuilder):
    """
    Represents 'multiple' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["multiple"]
