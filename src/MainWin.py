from PyQt5 import QtWidgets

from src.GroupWin import GroupWin
from src.KindWin import KindWin
from src.ParametersWin import ParametersWin
from src.SampleWin import SampleWin
from ui.MainWindow import Ui_MainWindow as mw


class MainWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()

        self.mw = mw()

        self.mw.setupUi(self)

        self.mw.pushButton.clicked.connect(self.kindButtonClicked)
        self.mw.pushButton_2.clicked.connect(self.paramsButtonClicked)
        self.mw.pushButton_3.clicked.connect(self.groupButtonClicked)
        self.mw.pushButton_4.clicked.connect(self.sampleButtonClicked)

    def kindButtonClicked(self):
        self.kindWin = KindWin()
        self.kindWin.show()

    def paramsButtonClicked(self):
        self.paramsWin = ParametersWin()
        self.paramsWin.show()

    def groupButtonClicked(self):
        self.groupWin = GroupWin()
        self.groupWin.show()

    def sampleButtonClicked(self):
        self.sampleWin = SampleWin()
        self.sampleWin.show()