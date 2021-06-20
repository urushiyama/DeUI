from collections.abc import Iterable
import html

from ...core.helper import MetaSingleton


class AttributeBuilder(metaclass=MetaSingleton):
    """
    The base builder class for HTML attributes.
    """
    def __init__(self):
        self.attributes = list()

    def __eq__(self, other):
        if not isinstance(other, AttributeBuilder):
            return False
        return type(self) is type(other)

    def __hash__(self):
        return hash(type(self))

    def build_attributes(self, html_widget):
        """
        Build attributes list from keyword arguments that the passed widget has.

        Args:
            html_widget (HTMLWidget): a HTML widget class instance that has attributes to build.

        Return:
            (str): attributes list that can be embedded in HTML tag.
        """
        result = ""

        if html_widget.kwargs is None:
            return result

        for attribute in self.attributes:
            value = html_widget.kwargs.get(attribute)
            attr = attribute
            if attribute == "clazz":
                attr = "class"
            elif attribute == "forr":
                attr = "for"
            elif attribute == "asynk":
                attr = "async"
            attr = attr.replace("_", "-")
            if isinstance(value, str) and value != "":
                result += f" {attr}=\"{html.escape(value)}\""
            elif isinstance(value, Iterable):
                result += f" {attr}=\"{html.escape(' '.join(value))}\""

        return result
