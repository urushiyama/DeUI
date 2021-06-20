from .attribute_builder import AttributeBuilder


class Global(AttributeBuilder):
    """
    Represents global attributes.
    """
    def __init__(self):
        super().__init__()
        self.attributes = [
            'accesskey', 'autocapitalize', 'autofocus',
            'class', 'clazz', 'contentditable', 'dir', 'draggable',
            'enterkeyhint', 'hidden', 'id', 'inputmode',
            'is', 'itemid', 'itemprop', 'itemref', 'itemscope',
            'itemtype', 'lang', 'nonce', 'part', 'slot',
            'spellcheck', 'style', 'tabindex', 'title', 'translate'
            ]
