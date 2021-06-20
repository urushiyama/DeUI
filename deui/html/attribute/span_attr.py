from .attribute_builder import AttributeBuilder


class Span(AttributeBuilder):
    """
    Represents 'span' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["span"]
