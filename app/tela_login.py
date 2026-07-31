from dataclasses import dataclass
from logo import PainelImagem
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

        self.painel_imagem = PainelImagem()
        self.formulario = FormularioLogin()

        layout = QHBoxLayout()
        layout.addWidget(self.painel_imagem)
        layout.addWidget(self.formulario)

        self.setLayout(layout)

        self.formulario.login_signal.connect(
            self.tentar_login
        )

        self.formulario.senha_esquecida.connect(
            self.mostrar_ajuda_senha
        )

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

        self.autenticado.emit(usuario)

    def mostrar_ajuda_senha(self):

        QMessageBox.information(
            self,
            "Faz o L",
            "Tem como não neguinho."
        )