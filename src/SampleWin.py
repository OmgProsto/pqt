from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from db.Repository import Repository
from src.CreateSampleModal import CreateSampleModal
from src.GradeSampleWin import GradeSampleWin
from ui.SampleWin import Ui_MainWindow as sw


class SampleWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(SampleWin, self).__init__()

        self.sw = sw()
        self.sw.setupUi(self)

        self.repo = Repository()

        groups = self.repo.getAllGroup()

        for group in groups:
            self.sw.comboBox.addItem(group.name, group.uid)

        self.generateTable()

        self.sw.comboBox.activated.connect(self.generateTable)

        self.sw.pushButton.clicked.connect(self.showCreateModal)

        self.sw.pushButton_2.clicked.connect(self.showGradeModal)

    def generateTable(self):
        self.sw.tableWidget.setRowCount(0)
        uidKind = self.sw.comboBox.currentData()

        samples = self.repo.getAllSample()
        self.sw.tableWidget.setRowCount(len(samples))
        curRow = 0
        for sample in samples:

            if sample.groupUid != uidKind:
                continue

            self.sw.tableWidget.setItem(curRow, 0, QTableWidgetItem(sample.name))
            self.sw.tableWidget.setItem(curRow, 1, QTableWidgetItem(str(sample.grade)))
            curRow += 1

    def showCreateModal(self):
        self.createKindModal = CreateSampleModal(self.generateTable)
        self.createKindModal.show()

    def showGradeModal(self):
        self.gradeSampleWin = GradeSampleWin(self.generateTable)
        self.gradeSampleWin.show()