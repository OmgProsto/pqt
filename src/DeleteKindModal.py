from PyQt5 import QtWidgets

from db.Repository import Repository
from ui.DeleteKindModal import Ui_MainWindow as dkw


class DeleteKindModal(QtWidgets.QMainWindow):
    def __init__(self, callbackRegenrate: callable):
        super(DeleteKindModal, self).__init__()
        self.callbackRegenrate = callbackRegenrate
        self.dkw = dkw()
        self.dkw.setupUi(self)

        self.repo = Repository()

        kinds = self.repo.getAllKinds()

        for kind in kinds:
            self.dkw.comboBox.addItem(kind.name, kind.uid)

        self.dkw.pushButton.clicked.connect(self.deleteKind)

    def deleteKind(self):
        uidKind = self.dkw.comboBox.currentData()
        self.repo.delKind(uidKind)
        self.callbackRegenrate()
        self.hide()