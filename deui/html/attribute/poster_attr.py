from .attribute_builder import AttributeBuilder


class Poster(AttributeBuilder):
    """
    Represents 'poster' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["poster"]
