from main_ui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep

def signals(self):
    self.pushButton_1.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(1))
    self.pushButton_2.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(0))

Ui_MainWindow.signals = signals
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()

    MainWindow.show()
    sys.exit(app.exec_())