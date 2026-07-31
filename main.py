import sys
import aplicacao
from PySide6.QtWidgets import QApplication
from logo import PainelImagem
from tela_login import TelaLogin
from usuarios import Usuario, ErroAutenticacao,AuthService

def main():
    app = QApplication(sys.argv)

    janela = TelaLogin()
    janela.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()