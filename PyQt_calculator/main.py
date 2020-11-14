from cal_ui import *
from PyQt5.QtWidgets import *

def signals(self):
    self.button_cal.clicked.connect(self.calc)
    
def calc(self):
    a = self.input1.text()
    b = self.input2.text()
    operator = self.comboBox.currentText()

    try:
        c=eval(a + operator + b) 
        self.result.setText(str(c))
    except:
        QMessageBox.critical(None, 'Error', 'Invalid inputs!', QMessageBox.Ok)

Ui_MainWindow.signals = signals
Ui_MainWindow.calc = calc

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    MainWindow.show()
    sys.exit(app.exec_())