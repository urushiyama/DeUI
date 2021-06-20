from ..engine import HTMLWidget


class Joined(HTMLWidget):
    """
    This is a helper to join childrens without line breaks.
    """

    def __str__(self):
        return "element"

    def draw(self):
        if (self.owner_view() is not None
                and not self.owner_view().has_updated_children):
            print("skip update {}".format(str(self)))
            return
        if self.owner_view() is not None:
            for child_view in self.owner_view().children:
                child_view.render()
        self.representation = ""
        if self.owner_view() is not None:
            for child_view in self.owner_view().children:
                self.representation += child_view.widget.representation.rstrip('\n')
            self.representation += "\n"
