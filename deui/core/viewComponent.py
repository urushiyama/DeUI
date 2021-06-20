import types

from .view import View


class ViewComponent:
    def __init__(self):
        self.__root_views = None
        self.outer_owner = View.owner
        self.g = self.owned_body()

    def __enter__(self):
        instance = None
        try:
            instance = next(self.g)
        except StopIteration:
            # body にyieldなし
            self.g = None
        finally:
            return instance

    def __exit__(self, error_type, value, traceback):
        if self.g is None:
            return None
        View.owner = self.outer_owner
        try:
            while True:
                next(self.g)
        except StopIteration:
            self.g = None

    def body(self):
        pass

    def owned_body(self):
        View.owner = self
        result = self.body()
        if not isinstance(result, types.GeneratorType):
            View.owner = self.outer_owner
        return result

    @property
    def root_views(self):
        if hasattr(self, '__root_views'):
            return self.__root_views
        self.__root_views = list()
        return self.__root_views

    @root_views.deleter
    def root_views(self):
        for view in self.__root_views:
            self.unset_owner(view)
            view.remove()
        self.__root_views.clear()

    def unset_owner(self, view):
        if view.owner is None:
            return
        if view.owner is not self:
            return
        view.owner = None
        if len(view.children) <= 0:
            return
        for child_view in view.children:
            self.unset_owner(child_view)
