import copy

from unsync import unsync

from ...core.app import App
from .web_root import WebRoot


class WebApp(App):
    def __init__(self):
        super().__init__()
        self.root_widget = WebRoot

    @unsync
    async def fetch_content(self):
        self.need_update = True
        while self.is_rendering or self.need_update:
            continue
        result = copy.copy(self.root_view.widget.representation)
        return result
