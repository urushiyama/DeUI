from .attribute_builder import AttributeBuilder


class Autocomplete(AttributeBuilder):
    """
    Represents 'autocomplete' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["autocomplete"]
