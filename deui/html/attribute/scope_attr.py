from .attribute_builder import AttributeBuilder


class Scope(AttributeBuilder):
    """
    Represents 'scope' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["scope"]
