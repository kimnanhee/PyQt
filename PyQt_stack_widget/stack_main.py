from stack import *
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
from time import sleep

def read_thread(ui):
	sleep(1)

def signals(self):
	self.btn_0.clicked.connect(lambda  : self.stackedWidget.setCurrentIndex(0))
	self.btn_1.clicked.connect(lambda  : self.stackedWidget.setCurrentIndex(1))
	self.btn_2.clicked.connect(lambda  : self.stackedWidget.setCurrentIndex(2))
	self.btn_3.clicked.connect(lambda  : self.stackedWidget.setCurrentIndex(3))

Ui_MainWindow.signals = signals

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()

    th = threading.Thread(target=read_thread, args=(ui,)) # 스레드 설정, read_thread함수에 인자로 ui를 넘겨준다
    th.daemon = True;
    th.start()

    MainWindow.show()
    sys.exit(app.exec_())