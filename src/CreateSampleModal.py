import uuid

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog

from db.Repository import Repository, Sample

from ui.CreateSampleModal import Ui_MainWindow as csm


class CreateSampleModal(QtWidgets.QMainWindow):
    def __init__(self, callbackRegenrate: callable):
        super(CreateSampleModal, self).__init__()
        self.callbackRegenrate = callbackRegenrate
        self.csm = csm()
        self.csm.setupUi(self)

        self.csm.pushButton.clicked.connect(self.createSample)
        self.csm.pushButton_2.clicked.connect(self.loadImage)

        self.uuid = str(uuid.uuid4())

        repo = Repository()
        groups = repo.getAllGroup()

        for group in groups:
            self.csm.comboBox.addItem(group.name, group.uid)

    def loadImage(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выбрать изображение", "", "Изображения (*.png *.jpg *.bmp)")
        pixmap = QPixmap(file_path)
        pixmap.save('img/' + self.uuid + '.png')
        self.csm.label_3.setText("Загружено изображение " + file_path)

    def createSample(self):
        repo = Repository()
        repo.createSample(Sample(
            self.uuid,
            self.csm.comboBox.currentData(),
            self.csm.lineEdit.text(),
            0
        ))
        self.callbackRegenrate()
        self.hide()
