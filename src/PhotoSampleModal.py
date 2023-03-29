from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap

from db.Repository import Repository
from ui.PhotoSampleModal import Ui_MainWindow as psm

class PhotoSampleModal(QtWidgets.QMainWindow):
    def __init__(self):
        super(PhotoSampleModal, self).__init__()
        self.psm = psm()
        self.psm.setupUi(self)

        self.repo = Repository()

        samples = self.repo.getAllSample()

        for sample in samples:
            self.psm.comboBox.addItem(sample.name, sample.uid)

        self.psm.comboBox.activated.connect(self.generateImg)

        self.generateImg()


    def generateImg(self):
        uidSample = self.psm.comboBox.currentData()
        pixmap = QPixmap('img/' + uidSample + '.png')

        self.psm.label.setPixmap(pixmap)