import uuid

from PyQt5 import QtWidgets

from db.Repository import Repository, Group
from ui.CreateGroupModal import Ui_MainWindow as cgm

class CreateGroupModal(QtWidgets.QMainWindow):
    def __init__(self, callbackRegenrate: callable):
        super(CreateGroupModal, self).__init__()
        self.callbackRegenrate = callbackRegenrate
        self.cgm = cgm()
        self.cgm.setupUi(self)

        self.cgm.pushButton.clicked.connect(self.createGroup)

        repo = Repository()
        kinds = repo.getAllKinds()

        for kind in kinds:
            self.cgm.comboBox.addItem(kind.name, kind.uid)


    def createGroup(self):
        repo = Repository()
        repo.createGroup(Group(
            str(uuid.uuid4()),
            self.cgm.comboBox.currentData(),
            self.cgm.lineEdit.text(),
            self.cgm.radioButton.isChecked()
        ))
        self.callbackRegenrate()
        self.hide()