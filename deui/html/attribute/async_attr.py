from .attribute_builder import AttributeBuilder


class Asynchronous(AttributeBuilder):
    """
    Represents 'async' attribute.

    For keyword arguments, 'asynk' is also recognized as 'async'.
    """
    def __init__(self):
        super().__init__()
        self.attributes = ["async", "asynk"]
