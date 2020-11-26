from PyQt5 import QtCore, QtGui, QtWidgets
from RGB_LED_control import *
import serial

ser = serial.Serial(
	port='COM5', 
	baudrate=9600, 
	parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)

def send_value(self):
    r = self.textEdit_r.toPlainText()
    g = self.textEdit_g.toPlainText()
    b = self.textEdit_b.toPlainText()
    message = 'S'+'{0:>3}{1:>3}{2:>3}'.format(r, g, b)+'F'
    print(message)
    print(type(message))
    ser.write(bytes(message.encode()))

def signals(self):
    self.pushButton.clicked.connect(self.send_value)

Ui_MainWindow.signals = signals
Ui_MainWindow.send_value = send_value

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    ui.send_value()

    MainWindow.show()
    sys.exit(app.exec_())
