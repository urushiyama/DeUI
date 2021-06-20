from .attribute_builder import AttributeBuilder


class Controls(AttributeBuilder):
    """
    Represents 'controls' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["controls"]
