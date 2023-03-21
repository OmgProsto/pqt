import uuid

from PyQt5 import QtWidgets

from db.Repository import Repository, Sample

from ui.CreateSampleModal import Ui_MainWindow as csm

class CreateSampleModal(QtWidgets.QMainWindow):
    def __init__(self, callbackRegenrate: callable):
        super(CreateSampleModal, self).__init__()
        self.callbackRegenrate = callbackRegenrate
        self.csm = csm()
        self.csm.setupUi(self)

        self.csm.pushButton.clicked.connect(self.createSample)

        repo = Repository()
        groups = repo.getAllGroup()

        for group in groups:
            self.csm.comboBox.addItem(group.name, group.uid)


    def createSample(self):
        repo = Repository()
        repo.createSample(Sample(
            str(uuid.uuid4()),
            self.csm.comboBox.currentData(),
            self.csm.lineEdit.text(),
            0
        ))
        self.callbackRegenrate()
        self.hide()