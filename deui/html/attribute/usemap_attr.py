from .attribute_builder import AttributeBuilder


class UseMap(AttributeBuilder):
    """
    Represents 'usemap' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["usemap"]
