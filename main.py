import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication
from display import Display
from info import Info
from styles import setupTheme
from buttons import Button

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Info
    info = Info('0.0 * 0.0 = 0.0')
    window.addToVLayout(info)

    # Display
    display = Display()
    display.setPlaceholderText('0')
    window.addToVLayout(display)

    # Botão
    button = Button('Texto do botão')
    window.addToVLayout(button)

    button2 = Button('Texto do botão')
    window.addToVLayout(button2)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
