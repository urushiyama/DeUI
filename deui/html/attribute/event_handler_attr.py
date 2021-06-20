from .attribute_builder import AttributeBuilder


class EventHandler(AttributeBuilder):
    """
    Represents event handlers.
    """
    def __init__(self):
        super().__init__()
        self.attributes = [
            "onabort", "onautocomplete", "onautocompleteerror",
            "onblur", "oncancel", "oncanplay", "oncanplaythrough",
            "onchange", "onclick", "onclose", "oncontextmenu",
            "oncuechange", "ondblclick", "ondrag", "ondragend",
            "ondragenter", "ondragexit", "ondragleave", "ondragover",
            "ondragstart", "ondrop", "ondurationchange", "onemptied",
            "onended", "onerror", "onfocus", "oninput", "oninvalid",
            "onkeydown", "onkeypress", "onkeyup", "onload",
            "onloadeddata", "onloadedmetadata", "onloadstart",
            "onmousedown", "onmouseenter", "onmouseleave",
            "onmousemove", "onmouseout", "onmouseover", "onmouseup",
            "onmousewheel", "onpause", "onplay", "onplaying",
            "onprogress", "onratechange", "onreset", "onresize",
            "onscroll", "onseeked", "onseeking", "onselect",
            "onshow", "onsort", "onstalled", "onsubmit", "onsuspend",
            "ontimeupdate", "ontoggle", "onvolumechange", "onwaiting"]
