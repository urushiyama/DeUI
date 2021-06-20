from .attribute_builder import AttributeBuilder


class Step(AttributeBuilder):
    """
    Represents 'step' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["step"]
