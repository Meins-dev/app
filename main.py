import sys
from PySide6.QtWidgets import QApplication
from app.tela_login import TelaLogin
from app.janela_principal import JanelaPrincipal

def main():
    app = QApplication(sys.argv)
    login = TelaLogin()
    # We'll keep a reference to the main window to prevent garbage collection
    main_window = None

    def on_autenticado(usuario):
        nonlocal main_window
        # Close login window (we don't need it anymore)
        login.close()
        # Create and show main window
        main_window = JanelaPrincipal(usuario)
        main_window.show()
        # Ensure the window is brought to front and receives focus
        main_window.raise_()
        main_window.activateWindow()

    login.autenticado.connect(on_autenticado)
    login.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()