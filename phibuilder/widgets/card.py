from enum import Enum
from PySide6.QtWidgets import QFrame, QVBoxLayout
from phibuilder.theme import Theme
from phibuilder.theme.shape import M3Shape

class CardVariant(str, Enum):
    ELEVATED = "elevated"; FILLED = "filled"; OUTLINED = "outlined"

class M3Card(QFrame):
    def __init__(self, theme: Theme | None = None, variant: CardVariant = CardVariant.ELEVATED,
                 shape: M3Shape = M3Shape.MD, elevation: int = 1, parent=None):
        super().__init__(parent)
        self._theme = theme; self._variant = variant; self._shape = shape
        self.setFrameShape(QFrame.NoFrame)
        self._layout = QVBoxLayout(self)
        self._layout.setContentsMargins(16, 16, 16, 16)
        self._update_style()
    def _update_style(self):
        c, r = self._theme.colors, self._shape.radius.top_left
        if self._variant == CardVariant.FILLED:
            bg, brd = c.surface_variant, "none"
        elif self._variant == CardVariant.OUTLINED:
            bg, brd = c.surface, f"1px solid {c.outline}"
        else:
            bg, brd = c.surface, "none"
        self.setStyleSheet(f"M3Card {{ background-color: {bg}; border: {brd}; border-radius: {r}px; }}")
    def set_variant(self, variant: CardVariant):
        self._variant = variant; self._update_style()
    def set_shape(self, shape: M3Shape):
        self._shape = shape; self._update_style()
    def content_layout(self) -> QVBoxLayout:
        return self._layout
