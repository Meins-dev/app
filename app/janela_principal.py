from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QBitmap, QPainter, QColor
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QSizePolicy,
)
from .usuarios import Usuario

class JanelaPrincipal(QWidget):
    def __init__(self, usuario: Usuario):
        super().__init__()
        self.usuario = usuario
        self.setWindowTitle(f"Bem-vindo, {usuario.nome_exibicao}")
        self.resize(400, 300)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Horizontal line
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        layout.addWidget(line)

        # User photo
        self.photo_label = QLabel()
        self.photo_label.setFixedSize(150, 150)
        self.photo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.photo_label.setStyleSheet("border: none;")
        layout.addWidget(self.photo_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Data labels
        self.name_label = QLabel()
        self.age_label = QLabel()
        self.phone_label = QLabel()
        for label in (self.name_label, self.age_label, self.phone_label):
            label.setTextFormat(Qt.TextFormat.RichText)
            layout.addWidget(label)

        self.load_user_data()

    def load_user_data(self):
        # Load and display photo
        foto_nome = getattr(self.usuario, 'foto', None)
        pixmap = None
        if foto_nome:
            import os
            base_dir = os.path.dirname(os.path.abspath(__file__))
            # Use the directory as per user request: "imagen usuarios"
            foto_path = os.path.join(base_dir, '..', 'imagen usuarios', foto_nome)
            pixmap = QPixmap(foto_path)
        if pixmap is None or pixmap.isNull():
            from PySide6.QtGui import QColor
            pixmap = QPixmap(150, 150)
            pixmap.fill(QColor("#0078d7"))
        self.photo_label.setPixmap(pixmap)
        
        # Apply circular mask to make the image display as a circle
        mask = QBitmap(pixmap.size())
        mask.clear()  # Fill with 0 (transparent)
        painter = QPainter(mask)
        painter.setBrush(Qt.white)  # Draw with 1 (opaque)
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(0, 0, pixmap.width(), pixmap.height())
        painter.end()
        self.photo_label.setMask(mask)

        # Set text
        self.name_label.setText(f"<b>Nome:</b> {getattr(self.usuario, 'nome_exibicao', 'Nome não disponível')}")
        self.age_label.setText(f"<b>Idade:</b> {getattr(self.usuario, 'idade', '??')}")
        self.phone_label.setText(f"<b>Telefone:</b> {getattr(self.usuario, 'telefone', 'Não informado')}")