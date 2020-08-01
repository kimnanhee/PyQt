from TH import *
from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import threading
from time import sleep

ser = serial.Serial(
	port='COM4', 
	baudrate=9600, 
	parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)

def read_thread(ui):
	while True:
		data = ser.readline().decode('utf-8')
		print(data)
		ui.label_humi_value.setText(data[2:7])
		ui.label_temp_value.setText(data[11:16])
		sleep(3)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    th = threading.Thread(target=read_thread, args=(ui,))
    th.daemon = True;
    th.start()

    MainWindow.show()
    sys.exit(app.exec_())