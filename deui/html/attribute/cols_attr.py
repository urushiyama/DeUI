from .attribute_builder import AttributeBuilder


class Columns(AttributeBuilder):
    """
    Represents 'cols' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["cols"]
