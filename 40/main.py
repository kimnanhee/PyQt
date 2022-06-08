from PyQt5 import QtCore, QtGui, QtWidgets
from ui import *

def signals(self):
    self.btn_start_1.clicked.connect(lambda  : self.stackedWidget.setCurrentIndex(1)) # 클릭하면 시작

    self.btn_start_2.clicked.connect(self.openpose_start)
    self.btn_back_2.clicked.connect(lambda  : self.stackedWidget.setCurrentIndex(0)) # 뒤로
    self.btn_add_2.clicked.connect(lambda  : self.stackedWidget.setCurrentIndex(2)) # 뒤로

    self.btn_save_3.clicked.connect(self.save_set) # 저장
    self.btn_back_3.clicked.connect(lambda  : self.stackedWidget.setCurrentIndex(1)) # 뒤로

    self.btn_back_5.clicked.connect(lambda  : self.stackedWidget.setCurrentIndex(1)) # 뒤로
    

def openpose_start(self):
    pass


def list_set():
    pass

def save_set():
    pass

def delete_set(num: id):
    pass

Ui_Form.signals = signals
Ui_Form.openpose_start = openpose_start
Ui_Form.save_set = save_set

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    ui.signals()

    ui.label_start_1.setPixmap(QtGui.QPixmap("exercise.jpg"))
    ui.stackedWidget.setCurrentIndex(0)
    
    Form.show()
    sys.exit(app.exec_())