import html

from .attribute_builder import AttributeBuilder


class XMLNamespace(AttributeBuilder):
    """
    Represents 'xmlns:*' attribute.

    For keyword arguments, 'xmlns_*' is also recognized as 'xmlns:*'.
    """
    def build_attributes(self, html_widget):
        result = ""

        if html_widget.kwargs is None:
            return result

        attributes = [k for k in html_widget.kwargs.keys() if k.startswith("xmlns_")]

        for attribute in attributes:
            value = html_widget.kwargs[attribute]
            if value != "":
                result += " {attribute}=\"{value}\"".format(
                    attribute=attribute.replace("_", ":", 1), value=html.escape(value))

        return result
