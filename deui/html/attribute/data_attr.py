from .attribute_builder import AttributeBuilder


class Data(AttributeBuilder):
    """
    Represents 'data' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["data"]
