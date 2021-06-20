from .attribute_builder import AttributeBuilder


class Kind(AttributeBuilder):
    """
    Represents 'kind' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["kind"]
