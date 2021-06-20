import html

from .attribute_builder import AttributeBuilder


class CustomData(AttributeBuilder):
    """
    Represents custom data attributes.

    For keyword arguments, 'data_*' is also recognized as 'data-*'.
    """
    def build_attributes(self, html_widget):
        result = ""

        if html_widget.kwargs is None:
            return result

        attributes = [k for k in html_widget.kwargs.keys() if k.startswith("data_")]

        for attribute in attributes:
            value = html_widget.kwargs[attribute]
            if value != "":
                result += " {attribute}=\"{value}\"".format(
                    attribute=attribute.replace("_", "-"), value=html.escape(value))

        return result
