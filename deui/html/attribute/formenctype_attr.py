from .attribute_builder import AttributeBuilder


class FormEncodingType(AttributeBuilder):
    """
    Represents 'formenctype' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["formenctype"]
