import math

from PyQt5 import QtWidgets

from db.Repository import Repository
from ui.GradeKindModal import Ui_MainWindow as gkm

class GradeKindWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(GradeKindWin, self).__init__()

        self.gkm = gkm()
        self.gkm.setupUi(self)

        self.repo = Repository()

        kinds = self.repo.getAllKinds()

        for kinds in kinds:
            self.gkm.comboBox.addItem(kinds.name, kinds.uid)

        self.generateGrade()
        self.gkm.comboBox.activated.connect(self.generateGrade)

    def generateGrade(self):
        self.gkm.label.setText("")
        uidKind = self.gkm.comboBox.currentData()
        samples = self.repo.getAllSamplesByKindUid(uidKind)

        allGrades = len(samples) * 5
        if allGrades == 0:
            self.gkm.label.setText("Оценка 0 / 100")
            return

        grades = 0

        for sample in samples:
            grades += sample.grade

        resultGrade = math.ceil(grades / allGrades * 100)

        if resultGrade > 80:
            self.gkm.label.setText("Оценка отлично")
        elif resultGrade > 60:
            self.gkm.label.setText("Оценка хорошо")
        elif resultGrade > 40:
            self.gkm.label.setText("Оценка удовлетворительно")
        else:
            self.gkm.label.setText("Оценка неудовлитворительно")


