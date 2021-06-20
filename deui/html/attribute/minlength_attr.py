from .attribute_builder import AttributeBuilder


class MinimumLength(AttributeBuilder):
    """
    Represents 'minlength' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["minlength"]
