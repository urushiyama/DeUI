from .attribute_builder import AttributeBuilder


class Muted(AttributeBuilder):
    """
    Represents 'muted' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["muted"]
