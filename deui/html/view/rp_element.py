from .element import Element


class RubyParentheses(Element):
    """
    Wraps fallback parentheses for browsers that do not support ruby content.
    """

    def __str__(self):
        return "rp"
