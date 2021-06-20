from .attribute_builder import AttributeBuilder


class HypertextReferenceLanguage(AttributeBuilder):
    """
    Represents 'hreflang' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["hreflang"]
