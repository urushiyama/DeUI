from .attribute_builder import AttributeBuilder


class EncodingType(AttributeBuilder):
    """
    Represents 'enctype' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["enctype"]
