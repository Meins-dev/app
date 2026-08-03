from PySide6.QtGui import QPixmap, QPainter, QPainterPath
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
import os

class PainelImagem(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.logo_label = QLabel()

        # Build path relative to this file's directory
        base_dir = os.path.dirname(os.path.abspath(__file__))
        # Go up one level to app/, then into imagem tela_login (note: space and singular)
        img_path = os.path.join(base_dir, '..', 'imagem tela_login', 'logo_gato.jpeg')
        pixmap = QPixmap(img_path)

        if pixmap.isNull():
            # Create a fallback colored pixmap
            pixmap = QPixmap(200, 200)
            pixmap.fill(Qt.GlobalColor.darkBlue)

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