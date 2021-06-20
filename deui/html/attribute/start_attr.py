from .attribute_builder import AttributeBuilder


class Start(AttributeBuilder):
    """
    Represents 'start' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["start"]
