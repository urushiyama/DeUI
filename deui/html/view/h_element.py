from .element import Element


class Heading(Element):
    """
    Represents section headings.
    """

    def __init__(self, *args, level=1, **kwargs):
        self.level = level
        super().__init__(*args, **kwargs)

    def __str__(self):
        return "h{level}".format(level=self.level)
