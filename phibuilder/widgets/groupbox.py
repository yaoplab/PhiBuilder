"""M3GroupBox — wrapper phibuilder pour QGroupBox."""
from PySide6.QtWidgets import QGroupBox
from phibuilder.theme import Theme


class M3GroupBox(QGroupBox):
    def __init__(self, title="", theme: Theme | None = None, parent=None):
        super().__init__(title, parent)
        self._theme = theme
        self._update_style()

    def _update_style(self):
        if self._theme is None:
            return
        c = self._theme.colors
        self.setStyleSheet(
            f"M3GroupBox {{ font-weight: bold; font-size: 13px; "
            f"border: 1px solid {c.outline_variant}; border-radius: 4px; "
            f"margin-top: 8px; padding: 12px 8px 8px; color: {c.on_surface}; }}"
            f"M3GroupBox::title {{ subcontrol-origin: margin; "
            f"subcontrol-position: top left; padding: 0 6px; color: {c.primary}; }}"
        )
