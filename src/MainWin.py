from PyQt5 import QtWidgets

from src.KindWin import KindWin
from ui.MainWindow import Ui_MainWindow as mw


class MainWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()

        self.mw = mw()

        self.mw.setupUi(self)

        self.mw.pushButton.clicked.connect(self.kindButtonClicked)

    def kindButtonClicked(self):
        self.kindWin = KindWin()
        self.kindWin.show()
