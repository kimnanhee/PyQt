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
    try:
        r = int(self.textEdit_r.toPlainText())
        g = int(self.textEdit_g.toPlainText())
        b = int(self.textEdit_b.toPlainText())
    except:
        self.textEdit_r.setText("0")
        self.textEdit_g.setText("0")
        self.textEdit_b.setText("0")
        print("잘못된 입력입니다.")
    else:
        message = '\x02'+ '{0:03d}{1:03d}{2:03d}'.format(r, g, b)+'\x03'
        print(message)
        print(type(message))
        ser.write(bytes(message.encode()))
        print(ser.read(9), 'response')

def signals(self):
    self.textEdit_r.setText('0')
    self.textEdit_g.setText('0')
    self.textEdit_b.setText('0')
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
