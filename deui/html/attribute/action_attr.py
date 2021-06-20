from .attribute_builder import AttributeBuilder


class Action(AttributeBuilder):
    """
    Represents 'action' attribute.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["action"]
