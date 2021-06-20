from ...core.widget import Widget
from ..attribute import AttributeRenderer
from ..attribute.composite import Common


class HTMLWidget(Widget):
    attribute_renderer = AttributeRenderer(*Common())

    def __init__(self, *args, **kwargs):
        """
        Warning! This method never be called in ordinal use.

        This is only for removing warnings in IDE.
        """
        super().__init__(*args, **kwargs)
        self.representation = ""

    def update(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        expanded_kwargs = dict()

        # Allow View(attr={"class":["foo", "bar"], "for":"id"})
        if "attr" in kwargs and isinstance(kwargs["attr"], dict):
            for k, v in kwargs["attr"].items():
                if k == "class":
                    k = "clazz"
                elif k == "for":
                    k = "forr"
                elif k == "async":
                    k = "asynk"
                expanded_kwargs[k] = v
            self.kwargs.update(expanded_kwargs)
            del self.kwargs["attr"]

        for k, v in kwargs.items():
            if isinstance(v, bool) and v:
                # Boolean attributes
                print(f"{k} = {k} ({v})")
                setattr(self, k, k)
            else:
                print(f"{k} = {v}")
                setattr(self, k, v)

    def draw(self):
        if (self.owner_view() is not None
                and not self.owner_view().has_updated_children):
            print("skip update {}".format(str(self)))
            return
        self.representation = ""
        if self.owner_view() is not None:
            for child_view in self.owner_view().children:
                child_view.render()
        self.draw_began()
        if self.owner_view() is not None:
            for child_view in self.owner_view().children:
                self.representation += child_view.widget.representation
        self.draw_ended()

    def draw_began(self):
        self.representation += f"<{str(self)}{type(self).attribute_renderer.attributes(self)}>\n"

    def draw_ended(self):
        self.representation += f"</{str(self)}>\n"
