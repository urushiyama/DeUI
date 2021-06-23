import weakref
from logging import getLogger, NullHandler

from .view import View

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class Widget:
    def __new__(cls, *args, **kwargs):
        view = View(cls, *args, **kwargs)
        widget = super().__new__(cls)
        widget.update(*args, **kwargs)

        def get_initial_widget():
            widget.owner_view = weakref.ref(view)
            widget.update(*args, **kwargs)
            return widget

        view.get_initial_widget = get_initial_widget
        return view

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.owner_view = None

    def draw(self):
        self.draw_began()
        if self.owner_view() is not None and hasattr(self.owner_view(), 'children'):
            for child_view in self.owner_view().children:
                child_view.render()
        self.draw_ended()

    def draw_began(self):
        logger.debug("<{widget}>".format(widget=str(self)))

    def draw_ended(self):
        logger.debug("</{widget}>".format(widget=str(self)))

    def update(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        for k, v in kwargs.items():
            logger.debug("{} = {}".format(k, v))
            setattr(self, k, v)

    def deinit(self):
        pass
