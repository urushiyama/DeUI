from .element import Element

from ..attribute.composite import Common
from ..attribute import (
    AttributeRenderer,
    ColumnSpan, Headers, RowSpan, Scope
)


class TableCell(Element):
    """
    Represents a cell of table.
    """

    attribute_renderer = AttributeRenderer(
        *Common(),
        ColumnSpan(),
        Headers(),
        RowSpan(),
        Scope()
    )

    def __init__(self, header=False):
        """
        Initialize a cell.

        Args:
            header (bool): if True, the cell should contain header;
            otherwise the cell should contain data.
        """
        self.header = header
        super().__init__()

    def __str__(self):
        return "th" if self.header else "td"
