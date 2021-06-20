from .attribute_builder import AttributeBuilder


class ImageSizes(AttributeBuilder):
    """
    Represents 'imagesizes' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["imagesizes"]
