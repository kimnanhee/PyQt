from button import *
import serial

L1_State=0
L2_State=0
L3_State=0

ser = serial.Serial(
	port='COM6', 
	baudrate=9600, 
	parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)

def Btn_1_control():
	global L1_State
	if(L1_State):
		message = ''.join(['\x02','L', '1', 'O', 'F', 'F', '\x03'])
		ser.write(bytes(message.encode()))
		L1_State = 0
	else:
		message = ''.join(['\x02','L', '1', 'O', 'N', '\x03'])
		ser.write(bytes(message.encode()))
		L1_State = 1

def Btn_2_control():
    global L2_State
    if(L2_State):
        message = ''.join(['\x02','L', '2', 'O', 'F', 'F', '\x03'])
        ser.write(bytes(message.encode()))
        L2_State = 0
    else:
        message = ''.join(['\x02','L', '2', 'O', 'N', '\x03'])
        ser.write(bytes(message.encode()))
        L2_State = 1

def Btn_3_control():
    global L3_State
    if(L3_State):
        message = ''.join(['\x02','L', '3', 'O', 'F', 'F', '\x03'])
        ser.write(bytes(message.encode()))
        L3_State = 0
    else:
        message = ''.join(['\x02','L', '3', 'O', 'N', '\x03'])
        ser.write(bytes(message.encode()))
        L3_State = 1

def signals(self):
	self.Btn_1.clicked.connect(Btn_1_control)
	self.Btn_2.clicked.connect(Btn_2_control)
	self.Btn_3.clicked.connect(Btn_3_control)

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