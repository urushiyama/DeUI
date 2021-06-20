from .attribute_builder import AttributeBuilder


class Accept(AttributeBuilder):
    """
    Represents 'accept' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = [
            'accept'
            ]
