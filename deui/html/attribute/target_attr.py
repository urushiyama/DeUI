from .attribute_builder import AttributeBuilder


class Target(AttributeBuilder):
    """
    Represents 'target' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["target"]
