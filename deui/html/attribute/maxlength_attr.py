from .attribute_builder import AttributeBuilder


class MaximumLength(AttributeBuilder):
    """
    Represents 'maxlength' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["maxlength"]
