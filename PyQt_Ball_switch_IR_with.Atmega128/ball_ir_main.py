from ball_ir import *
from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import threading
from time import sleep

ser = serial.Serial(
	port='COM5', # 아두이노 연결 COM 포트
	baudrate=9600, 
	parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)

def read_thread(ui): # 스레드
    sw_cnt = 0
    ir_cnt = 0
    while True:
        # data = (sw_state * 10 + ir_state)
        data = ser.read_all().decode() # 시리얼 통신에 있는 값 모두 읽어오기
        if data:
            print(data) # 확인용, 받아온 데이터 출력
            sleep(0.2)
            if(int(data) / 10 == 1):
                sw_cnt += 1
            if(int(data) % 10 == 1):
                ir_cnt += 1

            ui.value_sw.setText(str(sw_cnt)) # 라벨에 출력
            ui.value_ir.setText(str(ir_cnt))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    th = threading.Thread(target=read_thread, args=(ui,)) # 스레드 설정, read_thread함수에 인자로 ui를 넘겨준다
    th.daemon = True
    th.start()

    MainWindow.show()
    sys.exit(app.exec_())