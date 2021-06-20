from .attribute_builder import AttributeBuilder


class DateTime(AttributeBuilder):
    """
    Represents 'datetime' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["datetime"]
