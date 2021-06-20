from .. import Height, Width


class HasFixedSize:
    """
    This class always returns a tuple of attributes to set fixed size when this is instantiated.
    """
    def __new__(cls):
        return (
            Height(),
            Width()
        )
