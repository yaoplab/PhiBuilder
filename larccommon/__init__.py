from larccommon.database import Database, DBMode
from larccommon.auth import OAuth2Manager, _deduce_role_superviseur, _load_active_term
from larccommon.session import Session, UserRole, ConnMode, AuthResult
from larccommon.config_loader import find_cfg
from larccommon.app_config import AppConfig
from larccommon.logger import log, set_log_to_file, get_log_path, set_log_filename
from larccommon.network import NetworkMode, detect_network
from larccommon.photos import get_photo_path, ensure_cached, get_uncached_ids
from larccommon.theme import ThemeManager, Theme, Palette, FontScale
from larccommon.event_helpers import event_icon, event_color
from larccommon.l10n import Translator, _

__all__ = [
    "Database", "DBMode", "OAuth2Manager", "_deduce_role_superviseur", "_load_active_term",
    "Session", "UserRole", "ConnMode", "AuthResult", "find_cfg", "AppConfig",
    "log", "set_log_to_file", "get_log_path", "set_log_filename",
    "NetworkMode", "detect_network",
    "get_photo_path", "ensure_cached", "get_uncached_ids",
    "ThemeManager", "Theme", "Palette", "FontScale",
    "event_icon", "event_color",
    "Translator", "_",
]
