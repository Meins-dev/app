from dataclasses import dataclass
from PySide6.QtCore import Signal, Qt, QRectF
from PySide6.QtGui import QPixmap, QPainter, QPainterPath, QColor
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QFrame,
    QSizePolicy,
)
from .logo import PainelImagem
from .autenticador import AuthService
from .usuarios import Usuario, ErroAutenticacao

LARGURA = 760
ALTURA = 420


class FormularioLogin(QWidget):

    login_signal = Signal(str, str)
    senha_esquecida = Signal()

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Digite seu usuário")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Digite sua senha")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Entrar")
        self.login_button.clicked.connect(self.tentar_login)

        self.senha_button = QPushButton("Esqueceu a senha?")
        self.senha_button.clicked.connect(
            self.senha_esquecida.emit
        )
        self.senha_button.setObjectName("senha_button")

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Usuário"))
        layout.addWidget(self.username_input)

        layout.addWidget(QLabel("Senha"))
        layout.addWidget(self.password_input)

        layout.addWidget(self.login_button)
        layout.addWidget(self.senha_button)

        self.setLayout(layout)

    def tentar_login(self):

        login = self.username_input.text().strip()
        senha = self.password_input.text()

        self.login_signal.emit(login, senha)

    def limpar_senha(self):
        self.password_input.clear()


class TelaLogin(QWidget):

    autenticado = Signal(object)

    def __init__(self):
        super().__init__()

        self.autenticador = AuthService()

        self.setWindowTitle("Tela de Login")
        self.setFixedSize(LARGURA, ALTURA)

        # Main layout: vertical
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Top section: logo image and login form side by side
        top_layout = QHBoxLayout()
        self.painel_imagem = PainelImagem()
        self.formulario = FormularioLogin()
        top_layout.addWidget(self.painel_imagem)
        top_layout.addWidget(self.formulario)
        main_layout.addLayout(top_layout)

        # Horizontal line (initially hidden)
        self.line = QFrame()
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line.setVisible(False)
        main_layout.addWidget(self.line)

        # User photo label (initially hidden)
        self.photo_label = QLabel()
        self.photo_label.setFixedSize(150, 150)
        self.photo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.photo_label.setStyleSheet("background-color: #f0f0f0; border: 1px solid #ccc; border-radius: 75px;")
        self.photo_label.setVisible(False)
        main_layout.addWidget(self.photo_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Data labels container (initially hidden)
        self.data_container = QWidget()
        self.data_layout = QVBoxLayout()
        self.data_container.setLayout(self.data_layout)
        self.data_container.setVisible(False)
        main_layout.addWidget(self.data_container, alignment=Qt.AlignmentFlag.AlignCenter)

        # Initialize data labels (will be filled later)
        self.name_label = QLabel()
        self.age_label = QLabel()
        self.phone_label = QLabel()
        self.data_layout.addWidget(self.name_label)
        self.data_layout.addWidget(self.age_label)
        self.data_layout.addWidget(self.phone_label)

        # Style sheet for a modern look
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
                font-family: Arial, sans-serif;
            }
            QLabel {
                color: #333;
                font-size: 14px;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
                background-color: white;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #0078d7;
                background-color: #fafafa;
            }
            QPushButton {
                background-color: #0078d7;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-size: 14px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #005a9e;
            }
            QPushButton:pressed {
                background-color: #004578;
            }
            QPushButton#senha_button {
                background-color: transparent;
                color: #0078d7;
                text-decoration: underline;
                padding: 0;
            }
            QPushButton#senha_button:hover {
                color: #005a9e;
                background-color: transparent;
            }
            QFrame[frameShape=\"4\"] {
                color: #ccc;
                margin: 10px 0;
            }
        """)

        # Connect signals
        self.formulario.login_signal.connect(self.tentar_login)
        self.formulario.senha_esquecida.connect(self.mostrar_ajuda_senha)

    def tentar_login(self, login: str, senha: str):

        try:
            usuario = self.autenticador.autenticar(
                login,
                senha
            )

        except ErroAutenticacao as erro:

            QMessageBox.warning(
                self,
                "Erro de autenticação",
                str(erro)
            )

            self.formulario.limpar_senha()
            return

        QMessageBox.information(
            self,
            "Login realizado",
            f"Bem-vindo, {usuario.nome_exibicao}!"
        )

        # Show user data after successful login
        self.mostrar_dados_usuario(usuario)
        self.autenticado.emit(usuario)

    def mostrar_dados_usuario(self, usuario):
        """Display user photo and data after login."""
        # Show the hidden widgets
        self.line.setVisible(True)
        self.photo_label.setVisible(True)
        self.data_container.setVisible(True)

        # Set user photo (try to load from file, else use placeholder)
        photo_path = "user_photo.jpg"  # You can change this to a dynamic path based on user
        pixmap = QPixmap(photo_path)
        if pixmap.isNull():
            # Create a placeholder colored pixmap
            pixmap = QPixmap(150, 150)
            pixmap.fill(QColor("#0078d7"))
            # Add text overlay? For simplicity, just color.
        else:
            pixmap = pixmap.scaled(
                150, 150,
                Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                Qt.TransformationMode.SmoothTransformation
            )
            # Make it circular
            circular = QPixmap(150, 150)
            circular.fill(Qt.GlobalColor.transparent)
            painter = QPainter(circular)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            path = QPainterPath()
            path.addEllipse(0, 0, 150, 150)
            painter.setClipPath(path)
            painter.drawPixmap(0, 0, pixmap)
            painter.end()
            pixmap = circular

        self.photo_label.setPixmap(pixmap)

        # Set user data (example data - replace with actual user attributes)
        self.name_label.setText(f"<b>Nome:</b> {getattr(usuario, 'nome_exibicao', 'Nome não disponível')}")
        self.age_label.setText(f"<b>Idade:</b> {getattr(usuario, 'idade', '??')}")
        self.phone_label.setText(f"<b>Telefone:</b> {getattr(usuario, 'telefone', 'Não informado')}")

        # Enable text formatting for labels
        self.name_label.setTextFormat(Qt.TextFormat.RichText)
        self.age_label.setTextFormat(Qt.TextFormat.RichText)
        self.phone_label.setTextFormat(Qt.TextFormat.RichText)

    def mostrar_ajuda_senha(self):

        QMessageBox.information(
            self,
            "Faz o L",
            "Tem como não neguinho."
        )