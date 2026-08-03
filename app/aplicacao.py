from .estilos import estilos, Cores
import sys
from .tela_login import TelaLogin
from PySide6.QtWidgets import QApplication

class Aplicacao:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.configurar_tema()
        self.janela = TelaLogin()

    def configurar_tema(self) -> None:
        self.app.setStyle("Fusion")

        paleta = self.app.palette()
        paleta.setColor(paleta.Window, Cores.FUNDO)
        paleta.setColor(paleta.WindowText, Cores.TEXTO)
        self.app.setPalette(paleta)

        self.app.setStyleSheet(estilos)

    def executar(self):
        self.janela.show()
        return self.app.exec()


