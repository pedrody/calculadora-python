import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication
from display import Display
from info import Info
from styles import setupTheme
from buttons import ButtonsGrid

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Info
    info = Info('0.0 * 0.0 = 0.0')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    display.setPlaceholderText('0')
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
