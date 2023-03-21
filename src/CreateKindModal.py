import uuid

from PyQt5 import QtWidgets

from db.Repository import Repository, Kind
from ui.CreateKindModalWin import Ui_MainWindow as ckmw


class CreateKindModal(QtWidgets.QMainWindow):
    def __init__(self, callbackRegenrate: callable):
        super(CreateKindModal, self).__init__()
        self.callbackRegenrate = callbackRegenrate
        self.ckmw = ckmw()
        self.ckmw.setupUi(self)

        self.ckmw.pushButton.clicked.connect(self.createKind)
        self.ckmw.pushButton_2.clicked.connect(lambda: self.hide())

    def createKind(self):
        repo = Repository()
        repo.createKind(Kind(
            str(uuid.uuid4()),
            self.ckmw.lineEdit.text(),
            self.ckmw.radioButton.isChecked()
        ))
        self.callbackRegenrate()
        self.hide()