from .. import (
    HypertextReference, HypertextReferenceLanguage, Media, ReferrerPolicy, Relation
)


class Linkable:
    """
    This class always returns a tuple of attributes for linkable elements when this is instantiated.
    """
    def __new__(cls):
        return (
            HypertextReference(),
            HypertextReferenceLanguage(),
            Media(),
            ReferrerPolicy(),
            Relation()
        )
