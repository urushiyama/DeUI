from .attribute_builder import AttributeBuilder


class Preload(AttributeBuilder):
    """
    Represents 'preload' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["preload"]
