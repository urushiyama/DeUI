from .attribute_builder import AttributeBuilder


class Media(AttributeBuilder):
    """
    Represents 'media' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["media"]
