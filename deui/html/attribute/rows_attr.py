from .attribute_builder import AttributeBuilder


class Rows(AttributeBuilder):
    """
    Represents 'rows' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["rows"]
