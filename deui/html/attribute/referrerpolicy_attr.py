from .attribute_builder import AttributeBuilder


class ReferrerPolicy(AttributeBuilder):
    """
    Represents 'referrerpolicy' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["referrerpolicy"]
