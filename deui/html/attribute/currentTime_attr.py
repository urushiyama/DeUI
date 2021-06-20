from .attribute_builder import AttributeBuilder


class CurrentTime(AttributeBuilder):
    """
    Represents 'currentTime' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["currentTime"]
