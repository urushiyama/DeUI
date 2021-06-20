from .attribute_builder import AttributeBuilder


class Checked(AttributeBuilder):
    """
    Represents 'checked' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["checked"]
