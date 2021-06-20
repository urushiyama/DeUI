from .attribute_builder import AttributeBuilder


class FormAction(AttributeBuilder):
    """
    Represents 'formaction' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["formaction"]
