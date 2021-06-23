import logging
import threading
import weakref
from logging import getLogger, NullHandler

from .helper.iter_utils import align_iterables
from .root import Root

logger = getLogger(__name__)
logger.addHandler(NullHandler())


class App:
    def __init__(self):
        self.root_widget = Root
        self.root_view = None
        self.__stopped = False
        self.is_rendering = False
        self.__need_update = False
        self.view_constructor = None
        self.thread = threading.Thread(target=self.lifecycle)

    def __enter__(self):
        return self

    def __exit__(self, error_type, value, traceback):
        pass

    def __str__(self):
        return "App"

    def body(self, view_constructor):
        self.view_constructor = view_constructor

    def render(self):
        self.is_rendering = True
        with self.root_widget() as new_tree:
            self.view_constructor()
        App.update_tree(self.root_view, new_tree, root=self.root_widget)
        logger.info("finished updating view tree")
        logger.debug("###OLD TREE" + "#"*18)
        if self.root_view is not None:
            self.root_view.dump_tree()
        else:
            logger.debug("(None)")
        logger.debug("###NEW TREE" + "#"*18)
        if new_tree is not None:
            new_tree.dump_tree()
        else:
            logger.debug("(None)")
        logger.debug("#"*30)
        if self.root_view is not None:
            self.root_view.remove()
        logger.info("finish remove old tree")
        self.root_view = new_tree
        self.root_view.render()
        logger.info("finish render tree")
        self.is_rendering = False
        self.need_update = False

    @classmethod
    def update_tree(cls, old_tree, new_tree, root=Root):
        if new_tree is None:
            return
        if (old_tree is None
                or new_tree.widget_type is not old_tree.widget_type):
            logger.debug("building new tree")
            if old_tree is not None:
                logger.debug("changed widget type {} -> {}".format(old_tree.widget_type, new_tree.widget_type))
            new_tree.build(root=root)
            logger.debug("finish build tree")
            return
        new_tree.widget = old_tree.widget
        new_tree.widget.owner_view = weakref.ref(new_tree)
        if new_tree.hashcode != old_tree.hashcode:
            logger.debug("update widget parameters")
            new_tree.widget.update(*new_tree.args, **new_tree.kwargs)
            new_tree.need_update = True
        for old_subtree, new_subtree in align_iterables(old_tree.children, new_tree.children, key='id'):
            App.update_tree(old_subtree, new_subtree, root=root)

    @property
    def need_update(self):
        if self.__need_update:
            return True
        return False

    @need_update.setter
    def need_update(self, value):
        self.__need_update = value

    def start(self):
        self.thread.start()

    def lifecycle(self):
        while not self.__stopped:
            if self.need_update:
                self.pre_render()
                logger.debug("render start from lifecycle")
                self.render()
                self.post_render()
        self.before_exit()
        return

    def pre_render(self):
        pass

    def post_render(self):
        pass

    def before_exit(self):
        pass

    def stop(self):
        self.__stopped = True
        self.thread.join()
