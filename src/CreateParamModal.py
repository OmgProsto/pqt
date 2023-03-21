import uuid

from PyQt5 import QtWidgets

from db.Repository import Repository, Parameter
from ui.CreateParamModal import Ui_MainWindow as cpm


class CreateParamModal(QtWidgets.QMainWindow):
    def __init__(self, callbackRegenrate: callable):
        super(CreateParamModal, self).__init__()
        self.callbackRegenrate = callbackRegenrate
        self.cpm = cpm()
        self.cpm.setupUi(self)

        self.cpm.pushButton.clicked.connect(self.createParma)

        repo = Repository()
        kinds = repo.getAllKinds()

        for kind in kinds:
            self.cpm.comboBox.addItem(kind.name, kind.uid)

    def createParma(self):
        repo = Repository()
        repo.createParam(Parameter(
            str(uuid.uuid4()),
            self.cpm.comboBox.currentData(),
            self.cpm.lineEdit.text(),
            self.cpm.radioButton.isChecked()
        ))
        self.callbackRegenrate()
        self.hide()