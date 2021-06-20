from .html_widget import HTMLWidget


class WebRoot(HTMLWidget):
        def __str__(self):
            return "Root"

        def draw_began(self):
            pass

        def draw_ended(self):
            pass
