from PyQt5 import QtWidgets

from src.KindWin import KindWin
from src.ParametersWin import ParametersWin
from ui.MainWindow import Ui_MainWindow as mw


class MainWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()

        self.mw = mw()

        self.mw.setupUi(self)

        self.mw.pushButton.clicked.connect(self.kindButtonClicked)
        self.mw.pushButton_2.clicked.connect(self.paramsButtonClicked)

    def kindButtonClicked(self):
        self.kindWin = KindWin()
        self.kindWin.show()

    def paramsButtonClicked(self):
        self.paramsWin = ParametersWin()
        self.paramsWin.show()