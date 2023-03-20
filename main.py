import sys
from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow as mw
from KindWindow import Ui_MainWindow as kw

class MainWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        
        self.mw = mw()
        
        self.mw.setupUi(self)
        
        self.mw.pushButton.clicked.connect(self.kindButtonClicked)
        
    def kindButtonClicked(self):
    	self.kindWin = KindWin()
    	self.kindWin.show()

class KindWin(QtWidgets.QMainWindow):
	def __init__(self):
		super(KindWin, self).__init__()

		self.kw = kw()
		self.kw.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWin()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
