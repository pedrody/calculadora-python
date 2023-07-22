import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication
from display import Display

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Display
    display = Display()
    display.setPlaceholderText('0')
    window.addToVLayout(display)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
