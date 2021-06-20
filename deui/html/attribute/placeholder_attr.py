from .attribute_builder import AttributeBuilder


class Placeholder(AttributeBuilder):
    """
    Represents 'placeholder' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["placeholder"]
