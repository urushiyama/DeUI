from .attribute_builder import AttributeBuilder


class Form(AttributeBuilder):
    """
    Represents 'form' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["form"]
