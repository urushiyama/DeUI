from .attribute_builder import AttributeBuilder


class Relation(AttributeBuilder):
    """
    Represents 'rel' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["rel"]
