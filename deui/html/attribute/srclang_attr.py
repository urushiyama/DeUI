from .attribute_builder import AttributeBuilder


class SourceLanguage(AttributeBuilder):
    """
    Represents 'srclang' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["srclang"]
