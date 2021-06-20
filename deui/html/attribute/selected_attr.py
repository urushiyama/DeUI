from .attribute_builder import AttributeBuilder


class Selected(AttributeBuilder):
    """
    Represents 'selected' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["selected"]
