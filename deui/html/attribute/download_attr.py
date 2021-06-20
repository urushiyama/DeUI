from .attribute_builder import AttributeBuilder


class Download(AttributeBuilder):
    """
    Represents 'download' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["download"]
