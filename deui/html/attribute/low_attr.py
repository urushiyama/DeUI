from .attribute_builder import AttributeBuilder


class Low(AttributeBuilder):
    """
    Represents 'low' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["low"]
