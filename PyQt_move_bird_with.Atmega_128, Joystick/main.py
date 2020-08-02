from draw import *
from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import threading
from time import sleep
'''
ser = serial.Serial(
	port='COM4', # 아두이노 연결 COM 포트
	baudrate=9600, 
	parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)
'''

def read_thread(ui):
    while True:
        for i in range(1, 651, 5):
            ui.label_bird.move(i, 0)
            sleep(0.01)

        for i in range(1, 451, 5):
            ui.label_bird.move(650, i)
            sleep(0.01)

        for i in range(650, 0, -5):
            ui.label_bird.move(i, 450)
            sleep(0.01)


        for i in range(450, 0, -5):
            ui.label_bird.move(0, i)
            sleep(0.01)

    while False:
        data = ser.readline().decode('utf-8')
        print(data) # 확인용 받아온 데이터 출력
        ui.label_temp_value.setText(data[2:7]) # 아두이노에서 받는 온도값 파싱
        ui.label_humi_value.setText(data[11:16]) # 습도값 파싱
        sleep(3)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    th = threading.Thread(target=read_thread, args=(ui,)) # 스레드 설정, read_thread함수에 인자로 ui를 넘겨준다
    th.daemon = True;
    th.start()

    MainWindow.show()
    sys.exit(app.exec_())