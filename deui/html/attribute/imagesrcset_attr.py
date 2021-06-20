from .attribute_builder import AttributeBuilder


class ImageSourceSet(AttributeBuilder):
    """
    Represents 'imagesrcset' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["imagesrcset"]
