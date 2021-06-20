from .attribute_builder import AttributeBuilder


class Autoplay(AttributeBuilder):
    """
    Represents 'autoplay' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["autoplay"]
