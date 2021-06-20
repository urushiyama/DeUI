from .attribute_builder import AttributeBuilder


class FormMethod(AttributeBuilder):
    """
    Represents 'formmethod' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["formmethod"]
