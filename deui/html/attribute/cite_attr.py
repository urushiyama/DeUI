from .attribute_builder import AttributeBuilder


class Cite(AttributeBuilder):
    """
    Represents 'cite' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["cite"]
