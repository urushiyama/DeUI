from .attribute_builder import AttributeBuilder


class Color(AttributeBuilder):
    """
    Represents 'color' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["color"]
