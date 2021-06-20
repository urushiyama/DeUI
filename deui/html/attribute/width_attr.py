from .attribute_builder import AttributeBuilder


class Width(AttributeBuilder):
    """
    Represents 'width' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["width"]
