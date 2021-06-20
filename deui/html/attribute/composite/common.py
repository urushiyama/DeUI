from .. import (
    Global, EventHandler, ARIA, CustomData
)


class Common:
    """
    This class always returns a tuple of HTML common attributes when this is instantiated.

    HTML common attributes are as follows:
        Global attributes (e.g. 'class')
        Event handlers (e.g. 'onclicked')
        ARIA controls ('aria-*')
        Custom data attributes ('data-*')
    """
    def __new__(cls):
        return (
            Global(),
            EventHandler(),
            ARIA(),
            CustomData()
        )
