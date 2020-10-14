from graph_1 import *
from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import threading
import pyqtgraph as pg
from PyQt5.QtCore import pyqtSignal

temp_list=[0]
humi_list=[0]
receive_temp = 0
receive_humi = 0

ser = serial.Serial( # 아두이노와 연결된 Serial 설정
	port='COM6', 
	baudrate=9600, 
	parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)

class draw_graph(QtWidgets.QMainWindow, Ui_MainWindow):
	global temp_list, humi_list
	global receive_temp, receive_humi
	uiUpdateDelegate = pyqtSignal(int)

	def __init__(self, parent=None): # 설정 함수
		QtWidgets.QMainWindow.__init__(self, parent=parent)
		self.setupUi(self)
		self.uiUpdateDelegate.connect(self.uiUpdater) # 인터럽트 함수
		self.graphicsView.setBackground('#FFFFFF') # 배경 색깔
		self.graphicsView.showGrid(x=True, y=True) # 그리드
		self.graphicsView.setRange(xRange=[2, 20])
	
	def uiUpdater(self):
		self.graphicsView.clear() # 그래프 지우기
		self.graphicsView.plot(temp_list, pen=pg.mkPen('r', width=2), # 온도
			style=QtCore.Qt.DashLine, symbol=('o'), symbolBrush='r')
		self.graphicsView.plot(humi_list, pen=pg.mkPen('b', width=3), # 습도
			style=QtCore.Qt.DashLine, symbol='x', symbolBrush='b')

def read_thread(ui):
	global temp_list, humi_list # 글로벌 변수로 설정
	global now_temp, now_humi
	cnt = 0
	while True:
		data = ser.readline().decode('utf-8')  
		if data:
			print(data)
			temp = float(data[5:9]) # 온도 슬라이싱
			now_temp = temp
			humi = float(data[17:21]) # 습도 슬라이싱
			now_humi = humi

			ui.value_temp.setText(str(now_temp))
			ui.value_humi.setText(str(now_humi))

			temp_list.append(temp) # 리스트에 더하기
			humi_list.append(humi)
			
			cnt=cnt+1
			if(cnt>20): # 30개 데이터 자르기
				temp_list.pop(0)
				humi_list.pop(0)
				cnt=21

			ui.uiUpdateDelegate.emit(1) # updater 호출

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    ui = draw_graph()
    ui.show()

    th = threading.Thread(target=read_thread, args=(ui,)) # 스레드 설정, read_thread함수에 인자로 ui를 넘겨준다
    th.daemon = True;
    th.start()

    sys.exit(app.exec_())