from .attribute_builder import AttributeBuilder


class Integrity(AttributeBuilder):
    """
    Represents 'integrity' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["integrity"]
