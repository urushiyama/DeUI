from .attribute_builder import AttributeBuilder


class Loop(AttributeBuilder):
    """
    Represents 'loop' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["loop"]
