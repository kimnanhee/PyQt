from laser_cds import *
from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import threading
from time import sleep
import pygame
pygame.init()
pygame.mixer.init()

ser = serial.Serial(
	port='COM5', # 아두이노 연결 COM 포트
	baudrate=9600, 
	parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)

def read_thread(ui): # 스레드
    sound = pygame.mixer.Sound('wav/sound.wav') # 소리 파일 경로
    while True:
        data = ser.readline().decode('utf-8') # 시리얼 통신에 있는 값 모두 읽어오기
        if data:
            print(data) # 확인용, 받아온 데이터 출력
            sleep(0.1)
            if int(data[0:4])<50:
                ui.label_circle.setStyleSheet('background-color: red; border-radius : 60px;')
                ui.label_text.setText("침입")
                sound.play() # 소리 재생
                sleep(1.5)
                ser.read_all().decode('utf-8')
            else:
                ui.label_circle.setStyleSheet('background-color: blue; border-radius : 60px;')
                ui.label_text.setText("침입 감지중")

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