import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
