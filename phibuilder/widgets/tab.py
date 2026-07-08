"""M3TabWidget — wrapper phibuilder pour QTabWidget."""
from PySide6.QtWidgets import QTabWidget
from phibuilder.theme import Theme


class M3TabWidget(QTabWidget):
    def __init__(self, theme: Theme | None = None, parent=None):
        super().__init__(parent)
        self._theme = theme
        self._update_style()

    def _update_style(self):
        if self._theme is None:
            return
        c = self._theme.colors
        self.setStyleSheet(
            f"M3TabWidget::pane {{ border: 1px solid {c.outline}; "
            f"border-radius: 4px; background: {c.surface}; }}"
            f"M3TabBar::tab {{ padding: 6px 16px; font-size: 13px; "
            f"border: none; border-bottom: 2px solid transparent; "
            f"color: {c.on_surface}; }}"
            f"M3TabBar::tab:selected {{ color: {c.primary}; "
            f"border-bottom: 2px solid {c.primary}; font-weight: bold; }}"
        )
