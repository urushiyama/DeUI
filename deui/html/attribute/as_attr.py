from .attribute_builder import AttributeBuilder


class As(AttributeBuilder):
    """
    Represents 'as' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["as"]
