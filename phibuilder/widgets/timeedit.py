"""M3TimeEdit — wrapper phibuilder pour QTimeEdit."""
from PySide6.QtWidgets import QTimeEdit
from PySide6.QtCore import QTime
from phibuilder.theme import Theme


class M3TimeEdit(QTimeEdit):
    def __init__(self, time=None, theme: Theme | None = None, parent=None):
        super().__init__(time or QTime.currentTime(), parent)
        self._theme = theme
        self.setDisplayFormat("HH:mm")
        self._update_style()

    def _update_style(self):
        if self._theme is None:
            return
        c = self._theme.colors
        self.setStyleSheet(
            f"M3TimeEdit {{ padding: 8px; border: 1px solid {c.outline_variant}; "
            f"border-radius: 4px; font-size: 13px; "
            f"background: {c.surface}; color: {c.on_surface}; font-weight: bold; }}"
        )
