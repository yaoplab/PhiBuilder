"""M3TextEdit — wrapper phibuilder pour QTextEdit."""
from PySide6.QtWidgets import QTextEdit
from phibuilder.theme import Theme


class M3TextEdit(QTextEdit):
    def __init__(self, text="", theme: Theme | None = None, parent=None):
        super().__init__(text, parent)
        self._theme = theme
        self._update_style()

    def _update_style(self):
        if self._theme is None:
            return
        c = self._theme.colors
        self.setStyleSheet(
            f"M3TextEdit {{ padding: 8px; border: 1px solid {c.outline_variant}; "
            f"border-radius: 4px; font-size: 13px; "
            f"background: {c.surface}; color: {c.on_surface}; "
            f"selection-background-color: {c.primary_container}; }}"
        )
