"""M3ProgressBar — wrapper phibuilder pour QProgressBar."""
from PySide6.QtWidgets import QProgressBar
from phibuilder.theme import Theme


class M3ProgressBar(QProgressBar):
    def __init__(self, theme: Theme | None = None, parent=None):
        super().__init__(parent)
        self._theme = theme
        self._update_style()

    def _update_style(self):
        if self._theme is None:
            return
        c = self._theme.colors
        self.setStyleSheet(
            f"M3ProgressBar {{ height: 4px; background: {c.surface_container_highest}; "
            f"border: none; border-radius: 2px; text-align: center; }}"
            f"M3ProgressBar::chunk {{ background: {c.primary}; border-radius: 2px; }}"
        )
