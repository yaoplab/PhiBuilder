from dataclasses import dataclass, field
from typing import Optional
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication

from phibuilder import PhiBuilder


THEMES_CONFIG = [
    ("blue",    "Bleu",       "#1565C0", False),
    ("dark",    "Dark",       "#212121", True),
    ("sobre",   "Sobre",      "#37474F", False),
    ("contrast","Contrasté",  "#0033A0", False),
]

_SEED_MAP = {k: s for k, _, s, _ in THEMES_CONFIG}
_IS_DARK_MAP = {k: d for k, _, _, d in THEMES_CONFIG}

_THEME_DESIGN = {
    "dark": dict(
        radius=6, radius_lg=10, radius_xl=14,
        field_pad_v=10, field_pad_h=14,
        btn_sm_pad_v=8, btn_sm_pad_h=18,
        btn_pad_v=10, btn_pad_h=22,
    ),
    "contrast": dict(
        radius=6, radius_lg=10, radius_xl=14,
        spacing=8, margin=20,
        field_pad_v=10, field_pad_h=16,
        label_pad_v=8,
        btn_pad_v=10, btn_pad_h=24,
        btn_sm_pad_v=8, btn_sm_pad_h=18,
        btn_border=2,
    ),
}


@dataclass
class Palette:
    primary: str = '#1565C0'
    on_primary: str = '#FFFFFF'
    primary_container: str = '#BBDEFB'
    secondary: str = '#00897B'
    on_secondary: str = '#FFFFFF'
    secondary_container: str = '#B2DFDB'
    tertiary: str = '#E65100'
    on_tertiary: str = '#FFFFFF'
    tertiary_container: str = '#FFCC80'
    error: str = '#C62828'
    on_error: str = '#FFFFFF'
    error_container: str = '#FFCDD2'
    surface: str = '#F5F7FA'
    surface_variant: str = '#E8EAF6'
    background: str = '#F5F7FA'
    outline: str = '#546E7A'
    outline_variant: str = '#B0BEC5'
    text_strong: str = '#1B1B1F'
    text_soft: str = '#455A64'
    text_disabled: str = '#90A4AE'
    success: str = '#2E7D32'
    card_bg: str = '#FFFFFF'
    card_hover: str = '#E3F2FD'
    header_bg: str = '#1565C0'
    header_text: str = '#FFFFFF'
    active: str = '#1565C0'
    inactive: str = '#90A4AE'
    border: str = '#B0BEC5'
    border_light: str = '#E0E0E0'
    button_primary: str = '#1565C0'
    button_danger: str = '#C62828'
    button_accent: str = '#00897B'
    button_success: str = '#2E7D32'
    text_secondary: str = '#546E7A'
    accent: str = '#00897B'
    danger: str = '#C62828'


@dataclass
class DesignTokens:
    radius: int = 4
    radius_lg: int = 8
    radius_xl: int = 12
    spacing: int = 6
    margin: int = 16
    field_pad_v: int = 8
    field_pad_h: int = 12
    label_pad_v: int = 6
    label_pad_h: int = 0
    btn_pad_v: int = 8
    btn_pad_h: int = 20
    btn_sm_pad_v: int = 6
    btn_sm_pad_h: int = 16
    btn_border: int = 1


_THEME_PALETTES = {
    "blue": Palette(
        primary='#1565C0', on_primary='#FFFFFF', primary_container='#BBDEFB',
        secondary='#00897B', on_secondary='#FFFFFF', secondary_container='#B2DFDB',
        tertiary='#E65100', on_tertiary='#FFFFFF', tertiary_container='#FFCC80',
        error='#C62828', on_error='#FFFFFF', error_container='#FFCDD2', success='#2E7D32',
        card_bg='#FFFFFF', card_hover='#E3F2FD',
        header_bg='#1565C0', header_text='#FFFFFF',
        active='#1565C0', inactive='#90A4AE',
        border='#B0BEC5', border_light='#E0E0E0',
        button_primary='#1565C0', button_danger='#C62828', button_accent='#00897B',
        button_success='#2E7D32', text_secondary='#546E7A',
        accent='#00897B', danger='#C62828',
    ),
    "dark": Palette(
        primary='#64B5F6', on_primary='#0D2137', primary_container='#1E3A5F',
        secondary='#81C784', on_secondary='#1B3A1B', secondary_container='#2E5C2E',
        tertiary='#FFB74D', on_tertiary='#3E2C00', tertiary_container='#5C4300',
        error='#EF9A9A', on_error='#5C1A1A', error_container='#7C2020', success='#81C784',
        surface='#1E1E1E', surface_variant='#2D2D2D',
        background='#121212', outline='#616161', outline_variant='#424242',
        text_strong='#E0E0E0', text_soft='#9E9E9E', text_disabled='#616161',
        card_bg='#252525', card_hover='#333333',
        header_bg='#1E3A5F', header_text='#64B5F6',
        active='#64B5F6', inactive='#616161',
        border='#424242', border_light='#383838',
        button_primary='#64B5F6', button_danger='#EF9A9A', button_accent='#81C784',
        button_success='#81C784', text_secondary='#9E9E9E',
        accent='#81C784', danger='#EF9A9A',
    ),
    "sobre": Palette(
        primary='#37474F', on_primary='#FFFFFF', primary_container='#CFD8DC',
        secondary='#546E7A', on_secondary='#FFFFFF', secondary_container='#B0BEC5',
        tertiary='#78909C', on_tertiary='#FFFFFF', tertiary_container='#CFD8DC',
        error='#BF360C', on_error='#FFFFFF', error_container='#FFCCBC', success='#33691E',
        surface='#FAFAFA', surface_variant='#EEEEEE',
        background='#FFFFFF', outline='#BDBDBD', outline_variant='#E0E0E0',
        text_strong='#212121', text_soft='#616161', text_disabled='#9E9E9E',
        card_bg='#FFFFFF', card_hover='#F5F5F5',
        header_bg='#37474F', header_text='#FFFFFF',
        active='#37474F', inactive='#BDBDBD',
        border='#E0E0E0', border_light='#EEEEEE',
        button_primary='#37474F', button_danger='#BF360C', button_accent='#546E7A',
        button_success='#33691E', text_secondary='#616161',
        accent='#546E7A', danger='#BF360C',
    ),
    "contrast": Palette(
        primary='#0033A0', on_primary='#FFFFFF', primary_container='#80B3FF',
        secondary='#005A9E', on_secondary='#FFFFFF', secondary_container='#80D0FF',
        tertiary='#C62828', on_tertiary='#FFFFFF', tertiary_container='#FFB3B3',
        error='#B71C1C', on_error='#FFFFFF', error_container='#FFCDD2', success='#1B5E20',
        surface='#FFFFFF', surface_variant='#D6E8FF',
        background='#FFFFFF', outline='#000000', outline_variant='#333333',
        text_strong='#000000', text_soft='#1A1A1A', text_disabled='#555555',
        card_bg='#FFFFFF', card_hover='#B3D4FF',
        header_bg='#0033A0', header_text='#FFFFFF',
        active='#0033A0', inactive='#666666',
        border='#000000', border_light='#333333',
        button_primary='#0033A0', button_danger='#B71C1C', button_accent='#005A9E',
        button_success='#1B5E20', text_secondary='#1A1A1A',
        accent='#005A9E', danger='#B71C1C',
    ),
}


@dataclass
class FontScale:
    base: int = 12
    small: int = 10
    title: int = 14
    header: int = 16
    button: int = 12
    multiplier: float = 1.0


@dataclass
class Theme:
    name: str
    label: str
    palette: Palette = field(default_factory=Palette)
    fonts: FontScale = field(default_factory=FontScale)
    design: DesignTokens = field(default_factory=DesignTokens)


_BUILTIN_THEMES: dict[str, Theme] = {}

def _init_themes():
    if _BUILTIN_THEMES:
        return
    for key, label, seed, is_dark in THEMES_CONFIG:
        pal = _THEME_PALETTES[key]
        dt_kwargs = _THEME_DESIGN.get(key, {})
        dt = DesignTokens(**dt_kwargs)
        _BUILTIN_THEMES[key] = Theme(key, label, pal, design=dt)


class ThemeManager:
    def __init__(self):
        _init_themes()
        self._themes = _BUILTIN_THEMES
        self._active: str = 'blue'
        self._theme: Theme = self._themes[self._active]
        self._app: Optional[QApplication] = None
        self._phibuilder: Optional[PhiBuilder] = None

    @property
    def theme(self) -> Theme:
        return self._theme

    @property
    def palette(self) -> Palette:
        return self._theme.palette

    @property
    def fonts(self) -> FontScale:
        return self._theme.fonts

    @property
    def design(self) -> DesignTokens:
        return self._theme.design

    @property
    def active_name(self) -> str:
        return self._active

    def names(self) -> list[tuple[str, str]]:
        return [(k, v.label) for k, v in self._themes.items()]

    def get_palette(self, name: str) -> Optional[Palette]:
        t = self._themes.get(name)
        return t.palette if t else None

    def set_active(self, name: str) -> bool:
        if name in self._themes:
            self._active = name
            self._theme = self._themes[name]
            self._sync_phibuilder()
            self._reapply()
            return True
        return False

    def font_size(self, base: int) -> int:
        return max(7, int(base * self._theme.fonts.multiplier))

    def font(self, base: int, weight=QFont.Normal, family='Segoe UI') -> QFont:
        return QFont(family, self.font_size(base), weight)

    def bind(self, app: QApplication) -> None:
        self._app = app
        self._phibuilder = PhiBuilder(
            seed_color=_SEED_MAP.get(self._active, "#1565C0"),
            is_dark=_IS_DARK_MAP.get(self._active, False),
        )
        self._reapply()

    def _sync_phibuilder(self):
        if self._phibuilder is None:
            return
        self._phibuilder.set_seed_color(_SEED_MAP.get(self._active, "#1565C0"))
        self._phibuilder.set_dark_mode(_IS_DARK_MAP.get(self._active, False))

    def _reapply(self):
        if self._app is None:
            return
        combined = ""
        if self._phibuilder is not None:
            combined += self._phibuilder.qss + "\n"
        combined += self._generate_global_qss()
        self._app.setStyleSheet(combined)

    def _generate_global_qss(self) -> str:
        p = self._theme.palette
        f = self._theme.fonts
        s = self.font_size
        d = self._theme.design
        return f"""
            QToolTip {{
                background: {p.surface_variant}; color: {p.text_strong};
                border: 1px solid {p.outline}; padding: {d.radius}px;
                font-size: {s(f.small)}px;
            }}
            QMenu {{
                background: {p.surface}; color: {p.text_strong};
                border: 1px solid {p.outline};
                font-size: {s(f.base)}px;
            }}
            QMenu::item:selected {{
                background: {p.primary_container}; color: {p.text_strong};
            }}
            QScrollBar:vertical {{
                background: {p.surface_variant}; width: 8px; margin: 0;
            }}
            QScrollBar::handle:vertical {{
                background: {p.outline}; border-radius: {d.radius}px; min-height: 30px;
            }}
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
                height: 0;
            }}
        """


class QssHelper:
    """Shared QSS fragment generators — single source of truth for both apps.

    Usage: p = theme_manager.palette; d = theme_manager.design; s = theme_manager.font_size
    """

    @staticmethod
    def top_bar(p, d) -> str:
        return (
            f"QFrame#top_bar {{ background: {p.surface}; border: 1px solid {p.outline_variant}; "
            f"border-radius: {d.radius_lg}px; }}"
        )

    @staticmethod
    def panel(p, d) -> str:
        return (
            f"QFrame#panel {{ background: {p.surface}; border: 1px solid {p.outline_variant}; "
            f"border-radius: {d.radius_lg}px; }}"
        )

    @staticmethod
    def panel_title(p, s, fs) -> str:
        return (
            f"QLabel#panel_title {{ color: {p.text_strong}; "
            f"font-size: {s(fs)}px; font-weight: bold; }}"
        )

    @staticmethod
    def push_button(p, d, s) -> str:
        return (
            f"QPushButton {{ background: {p.primary}; color: {p.on_primary}; border: none; "
            f"border-radius: {d.radius}px; padding: {d.btn_pad_v}px {d.btn_pad_h}px; "
            f"font-size: {s(12)}px; }}"
            f"QPushButton:hover {{ background: {p.primary_container}; border-color: {p.primary}; }}"
            f"QPushButton:pressed {{ background: {p.primary}; color: {p.on_primary}; }}"
        )

    @staticmethod
    def table(p, d, s) -> str:
        return (
            f"QTableWidget {{ background: {p.surface}; color: {p.text_strong}; "
            f"border: none; gridline-color: {p.outline_variant}; "
            f"font-size: {s(12)}px; }}"
            f"QTableWidget::item {{ padding: {d.btn_sm_pad_v}px {d.spacing}px; }}"
            f"QHeaderView::section {{ background: {p.surface_variant}; color: {p.text_strong}; "
            f"padding: {d.btn_sm_pad_v}px {d.spacing}px; font-weight: bold; border: none; }}"
        )

    @staticmethod
    def combobox(p, d) -> str:
        return (
            f"QComboBox {{ background: {p.surface}; color: {p.text_strong}; "
            f"border: 1px solid {p.outline_variant}; border-radius: {d.radius}px; "
            f"padding: {d.field_pad_v}px {d.field_pad_h}px; }}"
            f"QComboBox:hover {{ border-color: {p.primary}; }}"
            f"QComboBox::drop-down {{ border: none; width: 20px; }}"
        )

    @staticmethod
    def period_btn(p, d) -> str:
        return (
            f"QPushButton#period_btn {{ min-width: 89px; max-width: 89px; height: 34px; "
            f"font-size: 13px; font-weight: normal; "
            f"border: {d.btn_border*2}px solid transparent; border-radius: {d.radius}px; "
            f"padding: 0; background: {p.surface_variant}; color: {p.text_strong}; }}"
            f"QPushButton#period_btn:hover {{ background: {p.primary_container}; "
            f"border-color: {p.primary}; }}"
            f"QPushButton#period_btn:checked {{ background: {p.primary}; color: {p.on_primary}; "
            f"border: {d.btn_border*2}px solid {p.primary}; font-weight: bold; }}"
        )

    @staticmethod
    def input_field(p, d) -> str:
        return (
            f"QLineEdit, QTextEdit, QPlainTextEdit {{ background: {p.surface}; "
            f"color: {p.text_strong}; border: 1px solid {p.outline_variant}; "
            f"border-radius: {d.radius}px; padding: {d.field_pad_v}px {d.field_pad_h}px; }}"
            f"QLineEdit:focus, QTextEdit:focus {{ border-color: {p.primary}; }}"
        )

    @staticmethod
    def kpi_common(p, d, s) -> str:
        return (
            f"QFrame#kpi_card {{ background: {p.surface_variant}; border-radius: {d.radius_lg}px; "
            f"padding: {d.spacing}px; }}"
            f"QLabel#kpi_value {{ font-size: {s(24)}px; font-weight: bold; color: {p.primary}; }}"
            f"QLabel#kpi_label {{ font-size: {s(10)}px; color: {p.text_soft}; }}"
            f"QFrame#kpi_small {{ background: {p.surface_variant}; "
            f"border-radius: {d.radius_lg}px; padding: {d.spacing//3}px; }}"
        )

    @staticmethod
    def sidebar_frame(p, d) -> str:
        return (
            f"QFrame#sidebar {{ background: {p.surface}; border: none; "
            f"border-right: 1px solid {p.outline_variant}; }}"
        )

    @staticmethod
    def phi_btn(p, d) -> str:
        return (
            f"QPushButton#phi_btn {{ font-size: 18px; border: 1px solid {p.outline_variant}; "
            f"border-radius: {d.radius}px; background: {p.surface_variant}; color: {p.text_strong}; }}"
            f"QPushButton#phi_btn:checked {{ background: {p.primary}; color: {p.on_primary}; "
            f"border: {d.btn_border*2}px solid {p.primary}; }}"
        )

    @staticmethod
    def section_btn(p, d, s) -> str:
        return (
            f"QPushButton#section_btn {{ background: transparent; border: none; font-weight: bold; "
            f"text-align: left; padding: {d.spacing//3}px {d.spacing}px; "
            f"font-size: {s(12)}px; color: {p.text_strong}; }}"
        )

    @staticmethod
    def class_btn(p, d, s) -> str:
        return (
            f"QPushButton#class_btn {{ border: none; border-radius: {d.radius}px; "
            f"text-align: left; padding: {d.spacing//2}px {d.field_pad_h}px; "
            f"font-size: {s(10)}px; }}"
            f"QPushButton#class_btn:hover {{ background: {p.primary_container}; }}"
            f"QPushButton#class_btn:checked {{ font-weight: bold; }}"
        )


theme_manager = ThemeManager()
