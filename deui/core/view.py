import textwrap
import weakref
from logging import getLogger, NullHandler

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class View:
    owner = None

    @classmethod
    def get_context_with(cls, context):
        def _get_context():
            return context

        return _get_context

    @classmethod
    def get_context(cls):
        return cls.get_context_with(None)()

    def __init__(self, widget_type, *args, **kwargs):
        # different widget type -> rebuild subtree
        self.widget_type = widget_type
        # different hashcode -> update current widget's parameters
        frozen_kwargs = frozenset({
                                      k: (v if v.__hash__ else frozenset(v))
                                      for k, v in kwargs.items()}.items())
        self.hashcode = hash(args) ^ hash(frozen_kwargs)
        # use id for calculate minimal diffs
        if 'id' in kwargs:
            self.id = kwargs['id']
        else:
            self.id = hash(self.widget_type)
        self.args = args
        self.kwargs = kwargs
        self.get_initial_widget = None
        self.get_outer_context = None

        self.need_update = False
        self.widget = None
        self.children = list()
        self.context = View.get_context()
        if self.context is not None:
            self.context.children.append(self)
            self.parent = self.context
        self.owner = View.owner
        if self.owner is not None:
            self.owner.root_views.append(self)

    def __enter__(self):
        self.pre_enter_context()
        self.get_outer_context = View.get_context
        View.get_context = View.get_context_with(self)
        self.post_enter_context()
        return self  # temporally, should return something wrapped for use

    def __exit__(self, error_type, value, traceback):
        self.pre_exit_context()
        View.get_context = self.get_outer_context
        self.post_exit_context()

    @property
    def has_updated_children(self):
        if self.need_update:
            return True
        return any(child.has_updated_children for child in self.children)

    def render(self):
        if self.widget is not None:
            # widget decide if its children also should be rendered or not
            self.widget.draw()
        self.need_update = False

    def build(self, root):
        """
        Initialize widgets in view.
        """
        self.need_update = True
        if callable(self.get_initial_widget):
            self.widget = self.get_initial_widget()
            if self.widget is not None:
                self.widget.owner_view = weakref.ref(self)
        if not hasattr(self, 'children'):
            return
        for child_view in self.children:
            child_view.build(root=root)
        return

    def remove(self):
        if self.owner is not None:
            # if view is related to view component, remove entire view component
            del self.owner.root_views
        else:
            for child_view in self.children:
                child_view.remove()
            if hasattr(self, 'parent') and (self.parent is not None):
                self.parent.children.remove(self)
                self.parent = None
            self.context = None
            self.get_outer_context = None
            if hasattr(self, 'widget') and self.widget is not None:
                self.widget.deinit()
                self.widget = None

    def pre_enter_context(self):
        pass

    def post_enter_context(self):
        pass

    def pre_exit_context(self):
        pass

    def post_exit_context(self):
        pass

    def dump_tree(self, level=0):
        logger.debug(textwrap.dedent("""
            {level}- [{updated}|{c_updated}] {name}: {hashcode}
            {level}    ID: view={view}, widget={widget}, widget owner={owner}
            """).strip().format(
            level=" " * level * 2,
            updated="*" if self.need_update else " ",
            c_updated="*" if self.has_updated_children else " ",
            name=self.widget_type,
            hashcode=self.hashcode,
            view=id(self),
            widget=id(self.widget),
            owner=id(self.widget.owner_view()) if self.widget.owner_view() is not None else "None"))
        for child_view in self.children:
            child_view.dump_tree(level=level + 1)
