from draw import *
from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import threading
from time import sleep

ser = serial.Serial(
	port='COM5', 
	baudrate=9600, 
	parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)

def read_thread(ui):
	while True:
		data = ser.readline().decode('utf-8')
		print(data) # 확인용 받아온 데이터 출력
		ui.label_temp.setText(data[7:11]) # 온도
		ui.label_gas.setText(data[19:22]) # 가스
		ui.label_fire.setText(data[31:34]) # 불꽃
		sleep(3)

def fan_control(): # fan 버튼이 눌리면 메시지 전송
	message = ''.join(['f', 'a', 'n', 'm'])
	ser.write(bytes(message.encode()))

def servo_control(): # servo 버튼이 눌리면 메시지 전송
	message = ''.join(['s', 'e', 'r', 'm'])
	ser.write(bytes(message.encode()))

def relay_control(): # relay 버튼이 눌리면 메시지 전송
	message = ''.join(['r', 'e', 'l', 'a'])
	ser.write(bytes(message.encode()))

def setting_control(self): # setting group box안의 redio button이 눌리면 호출
	if self.radioButton_auto.isChecked(): # auto 버튼이 눌리면 메시지 전송
		message = ''.join(['a', 'u', 't', 'o'])
		ser.write(bytes(message.encode()))
	elif self.radioButton_manual.isChecked(): # manual 버튼이 눌리면 메시지 전송
		message = ''.join(['m', 'a', 'n', 'u'])
		ser.write(bytes(message.encode()))
	
def signals(self): # 각 버튼이 눌렸을 때 함수 호출
	self.pushButton_fan.clicked.connect(fan_control)
	self.pushButton_servo.clicked.connect(servo_control)
	self.pushButton_relay.clicked.connect(relay_control)
	self.radioButton_auto.clicked.connect(self.setting_control)
	self.radioButton_manual.clicked.connect(self.setting_control)

Ui_MainWindow.signals = signals
Ui_MainWindow.setting_control = setting_control

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.signals()
    ui.setting_control()

    th = threading.Thread(target=read_thread, args=(ui,)) # 스레드 설정, read_thread함수에 인자로 ui를 넘겨준다
    th.daemon = True;
    th.start()

    MainWindow.show()
    sys.exit(app.exec_())