from PyQt5.QtWidgets import QTableWidgetItem

from db.Repository import Repository
from src.CreateGroupModal import CreateGroupModal
from ui.GroupWindow import Ui_MainWindow as gw

from PyQt5 import QtWidgets


class GroupWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(GroupWin, self).__init__()

        self.gw = gw()
        self.gw.setupUi(self)

        self.repo = Repository()

        kinds = self.repo.getAllKinds()

        for kind in kinds:
            self.gw.comboBox.addItem(kind.name, kind.uid)

        self.generateTable()

        self.gw.comboBox.activated.connect(self.generateTable)

        self.gw.pushButton.clicked.connect(self.showCreateModal)

    def generateTable(self):
        self.gw.tableWidget.setRowCount(0)
        uidKind = self.gw.comboBox.currentData()

        groups = self.repo.getAllGroup()

        self.gw.tableWidget.setRowCount(len(groups))
        curRow = 0
        for group in groups:

            if group.kindUid != uidKind:
                continue

            self.gw.tableWidget.setItem(curRow, 0, QTableWidgetItem(group.name))
            self.gw.tableWidget.setItem(curRow, 1, QTableWidgetItem("Да" if group.is_basic else "Нет"))
            curRow += 1

    def showCreateModal(self):
        self.createModal = CreateGroupModal(self.generateTable)
        self.createModal.show()

