from .attribute_builder import AttributeBuilder


class FormNoValidate(AttributeBuilder):
    """
    Represents 'formnovalidate' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["formnovalidate"]
