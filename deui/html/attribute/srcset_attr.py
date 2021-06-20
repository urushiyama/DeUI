from .attribute_builder import AttributeBuilder


class SourceSet(AttributeBuilder):
    """
    Represents 'srcset' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["srcset"]
