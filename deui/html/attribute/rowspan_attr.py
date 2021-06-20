from .attribute_builder import AttributeBuilder


class RowSpan(AttributeBuilder):
    """
    Represents 'rowspan' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["rowspan"]
