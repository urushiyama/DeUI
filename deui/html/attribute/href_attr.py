from .attribute_builder import AttributeBuilder


class HypertextReference(AttributeBuilder):
    """
    Represents 'href' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["href"]
