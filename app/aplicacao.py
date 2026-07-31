import estilos
from estilos import Cores
import sys
from tela_login import TelaLogin
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

class Aplicacao:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.configurar_tema()

        self.janela = TelaLogin()

        def configurar_tema(self) -> None:
            self.app.setStyleSheet("Fusion")
            self.app.setPalette(estilos)

            paleta = self.app.palette()
            paleta.setColor(paleta.Window, Cores.FUNDO)
            paleta.setColor(paleta.WindowText, Cores.TEXTO)
            self.app.setPalette(paleta)

            self.janela.show()


