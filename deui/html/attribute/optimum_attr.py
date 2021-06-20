from .attribute_builder import AttributeBuilder


class Optimum(AttributeBuilder):
    """
    Represents 'optimum' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["optimum"]
