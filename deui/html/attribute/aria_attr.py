import html

from .attribute_builder import AttributeBuilder


class ARIA(AttributeBuilder):
    """
    Represents ARIA control attributes.

    For keyword arguments, 'aria_*' is also recognized as 'aria-*'.
    """
    def build_attributes(self, html_widget):
        result = ""

        if html_widget.kwargs is None:
            return result

        attributes = [k for k in html_widget.kwargs.keys() if k.startswith("aria_")]

        for attribute in attributes:
            value = html_widget.kwargs[attribute]
            if value != "":
                result += " {attribute}=\"{value}\"".format(
                    attribute=attribute.replace("_", "-"), value=html.escape(value))

        return result
