from .attribute_builder import AttributeBuilder


class NoValidate(AttributeBuilder):
    """
    Represents 'novalidate' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["novalidate"]
