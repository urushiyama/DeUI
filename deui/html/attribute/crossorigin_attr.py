from .attribute_builder import AttributeBuilder


class CrossOrigin(AttributeBuilder):
    """
    Represents 'crossorigin' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["crossorigin"]
