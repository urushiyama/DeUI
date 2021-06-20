from .attribute_builder import AttributeBuilder


class Content(AttributeBuilder):
    """
    Represents 'content' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["content"]
