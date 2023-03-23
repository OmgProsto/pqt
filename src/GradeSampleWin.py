from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QCheckBox

from db.Repository import Repository
from ui.GradeSampleWin import Ui_MainWindow as gsw


class GradeSampleWin(QtWidgets.QMainWindow):
    def __init__(self, generateTable: callable):
        super(GradeSampleWin, self).__init__()

        self.generateTableSample = generateTable
        self.gsw = gsw()
        self.gsw.setupUi(self)

        self.repo = Repository()

        samples = self.repo.getAllSample()

        for sample in samples:
            self.gsw.comboBox.addItem(sample.name, sample.uid)

        self.generateTable()
        self.gsw.comboBox.activated.connect(self.generateTable)

        self.gsw.pushButton.clicked.connect(self.save)

    def generateTable(self):
        self.gsw.tableWidget.setRowCount(0)
        uidSample = self.gsw.comboBox.currentData()

        parameters = self.repo.getParametersBySampleUid(uidSample)

        self.radioButtonsDict = {}

        self.gsw.tableWidget.setRowCount(len(parameters))
        curRow = 0
        for parameter in parameters:
            radio_button = QCheckBox()
            radio_button.setGeometry(10, 0, 20, 20)
            radio_button.setText('Да')

            self.radioButtonsDict[parameter.uid] = radio_button

            self.gsw.tableWidget.setItem(curRow, 0, QTableWidgetItem(parameter.name))
            self.gsw.tableWidget.setCellWidget(curRow, 1, radio_button)
            curRow += 1

    def save(self):

        currentAnswerYes = 0

        for key, value in self.radioButtonsDict.items():
            if self.repo.isParameterCritical(key) and value.isChecked() == False:
                self.repo.updateGradeSample(self.gsw.comboBox.currentData(), 2)
                self.generateTableSample()
                self.hide()
                return

            if value.isChecked():
                currentAnswerYes += 1

        persentYesAnswer = currentAnswerYes / len(self.radioButtonsDict) * 100

        if persentYesAnswer > 80:
            self.repo.updateGradeSample(self.gsw.comboBox.currentData(), 5)
        elif persentYesAnswer > 60:
            self.repo.updateGradeSample(self.gsw.comboBox.currentData(), 4)
        elif persentYesAnswer > 40:
            self.repo.updateGradeSample(self.gsw.comboBox.currentData(), 3)
        else:
            self.repo.updateGradeSample(self.gsw.comboBox.currentData(), 2)

        self.generateTableSample()

        self.hide()
