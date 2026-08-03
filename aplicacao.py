from app.estilos import estilos, Cores
import sys
from app.tela_login import TelaLogin
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QColor, QPalette

class Aplicacao:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.configurar_tema()
        self.janela = TelaLogin()

    def configurar_tema(self) -> None:
        self.app.setStyle("Fusion")

        paleta = QPalette()
        # Define as cores da paleta
        paleta.setColor(QPalette.Window, QColor(Cores.FUNDO))
        paleta.setColor(QPalette.WindowText, QColor(Cores.TEXTO))
        paleta.setColor(QPalette.Base, QColor(Cores.CARTAO))
        paleta.setColor(QPalette.AlternateBase, QColor(Cores.FUNDO))
        paleta.setColor(QPalette.ToolTipBase, QColor(Cores.TEXTO))
        paleta.setColor(QPalette.ToolTipText, QColor(Cores.TEXTO))
        paleta.setColor(QPalette.Text, QColor(Cores.TEXTO))
        paleta.setColor(QPalette.Button, QColor(Cores.PRIMARIA))
        paleta.setColor(QPalette.ButtonText, QColor(Cores.TEXTO))
        paleta.setColor(QPalette.BrightText, QColor(Cores.TEXTO_SECUNDARIO))
        paleta.setColor(QPalette.Link, QColor(Cores.PRIMARIA_HOVER))
        paleta.setColor(QPalette.Highlight, QColor(Cores.PRIMARIA_HOVER))
        paleta.setColor(QPalette.HighlightedText, QColor(Cores.TEXTO))
        self.app.setPalette(paleta)

        # Também aplica o stylesheet para estilização adicional
        self.app.setStyleSheet(estilos)

    def executar(self):
        self.janela.show()
        return self.app.exec()