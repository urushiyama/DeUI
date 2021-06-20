from .attribute_builder import AttributeBuilder


class For(AttributeBuilder):
    """
    Represents 'for' attribute.

    For keyword arguments, 'forr' is also recognized as 'for'.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["for", "forr"]
