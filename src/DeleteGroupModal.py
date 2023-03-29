from PyQt5 import QtWidgets

from db.Repository import Repository
from ui.DeleteGroupModal import Ui_MainWindow as dgm


class DeleteGroupModal(QtWidgets.QMainWindow):
    def __init__(self, callbackRegenrate: callable):
        super(DeleteGroupModal, self).__init__()
        self.callbackRegenrate = callbackRegenrate
        self.dgm = dgm()
        self.dgm.setupUi(self)

        self.repo = Repository()

        groups = self.repo.getAllGroup()

        for group in groups:
            self.dgm.comboBox.addItem(group.name, group.uid)

        self.dgm.pushButton.clicked.connect(self.delGroup)

    def delGroup(self):
        uidGroup = self.dgm.comboBox.currentData()
        self.repo.delGroup(uidGroup)
        self.callbackRegenrate()
        self.hide()