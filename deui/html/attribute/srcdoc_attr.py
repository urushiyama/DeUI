from .attribute_builder import AttributeBuilder


class SourceDocument(AttributeBuilder):
    """
    Represents 'srcdoc' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["srcdoc"]
