import sys
from PyQt5 import QtWidgets

from src.MainWin import MainWin


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWin()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
