from .attribute_builder import AttributeBuilder


class Sandbox(AttributeBuilder):
    """
    Represents 'sandbox' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["sandbox"]
