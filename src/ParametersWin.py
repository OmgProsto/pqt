from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from db.Repository import Repository
from src.CreateParamModal import CreateParamModal
from ui.ParametersWin import Ui_MainWindow as pw

class ParametersWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(ParametersWin, self).__init__()

        self.pw = pw()
        self.pw.setupUi(self)

        self.repo = Repository()

        kinds = self.repo.getAllKinds()

        for kind in kinds:
            self.pw.comboBox.addItem(kind.name, kind.uid)

        self.generateTable()

        self.pw.comboBox.activated.connect(self.generateTable)

        self.pw.pushButton.clicked.connect(self.showCreateModal)


    def generateTable(self):
        self.pw.tableWidget.setRowCount(0)
        uidKind = self.pw.comboBox.currentData()

        parameters = self.repo.getAllParams()
        self.pw.tableWidget.setRowCount(len(parameters))
        curRow = 0
        for param in parameters:

            if param.kindUid != uidKind:
                continue

            self.pw.tableWidget.setItem(curRow, 0, QTableWidgetItem(param.name))
            self.pw.tableWidget.setItem(curRow, 1, QTableWidgetItem("Да" if param.is_critical else "Нет"))
            curRow += 1

    def showCreateModal(self):
        self.createKindModal = CreateParamModal(self.generateTable)
        self.createKindModal.show()




