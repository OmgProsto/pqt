from PyQt5 import QtWidgets

from db.Repository import Repository
from ui.DeleteSampleWin import Ui_MainWindow as dsw


class DeleteSampleModal(QtWidgets.QMainWindow):
    def __init__(self, callbackRegenrate: callable):
        super(DeleteSampleModal, self).__init__()
        self.callbackRegenrate = callbackRegenrate
        self.dsw = dsw()
        self.dsw.setupUi(self)

        self.repo = Repository()

        samples = self.repo.getAllSample()

        for sample in samples:
            self.dsw.comboBox.addItem(sample.name, sample.uid)

        self.dsw.pushButton.clicked.connect(self.deleteSample)

    def deleteSample(self):
        uidSample = self.dsw.comboBox.currentData()
        self.repo.delSample(uidSample)
        self.callbackRegenrate()
        self.hide()