"""M3Menu — wrapper phibuilder pour QMenu."""
from PySide6.QtWidgets import QMenu
from phibuilder.theme import Theme


class M3Menu(QMenu):
    def __init__(self, title="", theme: Theme | None = None, parent=None):
        super().__init__(title, parent)
        self._theme = theme
        self._update_style()

    def _update_style(self):
        if self._theme is None:
            return
        c = self._theme.colors
        self.setStyleSheet(
            f"M3Menu {{ background: {c.surface}; border: 1px solid {c.outline}; "
            f"border-radius: 4px; padding: 4px; }}"
            f"M3Menu::item {{ padding: 6px 24px; font-size: 13px; "
            f"color: {c.on_surface}; }}"
            f"M3Menu::item:selected {{ background: {c.primary_container}; "
            f"color: {c.on_primary_container}; }}"
            f"M3Menu::separator {{ height: 1px; background: {c.outline_variant}; "
            f"margin: 4px 8px; }}"
        )
