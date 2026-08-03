from dataclasses import dataclass
from pyautogui import size
from usuarios import AuthService, ErroAutenticacao
from PySide6.QtCore import Signal, Qt , QRectF
from PySide6.QtGui import QPixmap, QPainter, QPainterPath
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
)
tamanho = 300

class PainelImagem(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.logo_label = QLabel()

        pixmap = QPixmap("logo_gato.jpeg")

        tamanho = 200

        pixmap = pixmap.scaled(
            tamanho,
            tamanho,
            Qt.KeepAspectRatioByExpanding,
            Qt.SmoothTransformation
        )

        circular = QPixmap(tamanho, tamanho)
        circular.fill(Qt.transparent)

        painter = QPainter(circular)
        painter.setRenderHint(QPainter.Antialiasing)

        path = QPainterPath()
        path.addEllipse(0, 0, tamanho, tamanho)

        painter.setClipPath(path)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()

        self.logo_label.setPixmap(circular)
        self.logo_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.logo_label)
        self.setLayout(layout)
