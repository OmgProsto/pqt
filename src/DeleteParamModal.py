from PyQt5 import QtWidgets

from db.Repository import Repository

from ui.DeleteParamModal import Ui_MainWindow as dpm


class DeleteParamModal(QtWidgets.QMainWindow):
    def __init__(self, callbackRegenrate: callable):
        super(DeleteParamModal, self).__init__()
        self.callbackRegenrate = callbackRegenrate
        self.dpm = dpm()
        self.dpm.setupUi(self)

        self.repo = Repository()

        params = self.repo.getAllParams()

        for param in params:
            self.dpm.comboBox.addItem(param.name, param.uid)

        self.dpm.pushButton.clicked.connect(self.deleteParam)

    def deleteParam(self):
        uidParam = self.dpm.comboBox.currentData()
        self.repo.delParam(uidParam)
        self.callbackRegenrate()
        self.hide()