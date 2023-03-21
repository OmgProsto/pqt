from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from db.Repository import Repository
from src.CreateKindModal import CreateKindModal
from ui.KindWindow import Ui_MainWindow as kw


class KindWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(KindWin, self).__init__()

        self.kw = kw()
        self.kw.setupUi(self)

        self.repo = Repository()

        self.generateTable()

        self.kw.pushButton.clicked.connect(self.showCreateModal)

    def showCreateModal(self):
        self.createKindModal = CreateKindModal(self.generateTable)
        self.createKindModal.show()

    def generateTable(self):
        kinds = self.repo.getAllKinds()
        self.kw.tableWidget.setRowCount(len(kinds))

        curRow = 0
        for kind in kinds:
            self.kw.tableWidget.setItem(curRow, 0, QTableWidgetItem(kind.name))
            self.kw.tableWidget.setItem(curRow, 1, QTableWidgetItem("Да" if kind.is_basic else "Нет"))
            curRow += 1