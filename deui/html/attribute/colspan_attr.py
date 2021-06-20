from .attribute_builder import AttributeBuilder


class ColumnSpan(AttributeBuilder):
    """
    Represents 'colspan' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["colspan"]
