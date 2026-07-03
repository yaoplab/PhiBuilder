import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QDialog,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
)


class FileViewer(QDialog):
    """Popup d'aperçu de fichier — image, texte, ou lien d'ouverture."""

    def __init__(self, path: str, parent=None):
        super().__init__(parent)
        self._path = path
        self.setWindowTitle(os.path.basename(path))
        self.setMinimumSize(610, 480)
        self._build()

    def _build(self):
        layout = QVBoxLayout(self)
        name = QLabel(os.path.basename(self._path))
        name.setStyleSheet("font-size: 16px; font-weight: bold; padding: 8px;")
        name.setAlignment(Qt.AlignCenter)
        layout.addWidget(name)

        ext = os.path.splitext(self._path)[1].lower()
        img_exts = {".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp"}
        text_exts = {".txt", ".csv", ".md", ".json", ".xml", ".html", ".log", ".py", ".sql"}

        if ext in img_exts:
            self._show_image(layout)
        elif ext in text_exts:
            self._show_text(layout)
        else:
            self._show_unsupported(layout)

        btn_row = QHBoxLayout()
        open_btn = QPushButton("Ouvrir avec l'application par défaut")
        open_btn.clicked.connect(self._open_external)
        btn_row.addWidget(open_btn)
        close_btn = QPushButton("Fermer")
        close_btn.clicked.connect(self.accept)
        btn_row.addWidget(close_btn)
        layout.addLayout(btn_row)

    def _show_image(self, layout):
        pix = QPixmap(self._path)
        if pix.isNull():
            layout.addWidget(QLabel("Impossible de charger l'image."))
            return
        scaled = pix.scaled(560, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        img = QLabel()
        img.setPixmap(scaled)
        img.setAlignment(Qt.AlignCenter)
        layout.addWidget(img, 1)

    def _show_text(self, layout):
        editor = QTextEdit()
        editor.setReadOnly(True)
        try:
            with open(self._path, "r", encoding="utf-8") as f:
                editor.setPlainText(f.read())
        except Exception:
            editor.setPlainText("(Impossible de lire le fichier)")
        layout.addWidget(editor, 1)

    def _show_unsupported(self, layout):
        msg = QLabel(
            "Aucun aperçu disponible pour ce type de fichier.\n"
            "Cliquez sur « Ouvrir » pour le visualiser dans l'application par défaut."
        )
        msg.setAlignment(Qt.AlignCenter)
        msg.setStyleSheet("font-size: 13px; color: #666; padding: 40px;")
        layout.addWidget(msg, 1)

    def _open_external(self):
        import subprocess

        try:
            subprocess.Popen(["explorer", self._path])
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Impossible d'ouvrir le fichier : {e}")
