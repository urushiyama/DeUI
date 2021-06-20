from .attribute_builder import AttributeBuilder


class Sizes(AttributeBuilder):
    """
    Represents 'sizes' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["sizes"]
