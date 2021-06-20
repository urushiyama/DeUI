from .attribute_builder import AttributeBuilder


class Label(AttributeBuilder):
    """
    Represents 'label' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["label"]
