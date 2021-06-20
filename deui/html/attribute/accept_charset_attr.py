from .attribute_builder import AttributeBuilder


class AcceptCharset(AttributeBuilder):
    """
    Represents 'accept_charset' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["accept_charset"]
