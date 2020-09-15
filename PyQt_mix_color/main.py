'''
RGB값을 조절하는 horizonBar를 사용해서 버튼의 색깔바꾸기
'''
from ui import *
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
from time import sleep

def read_thread(ui):
	while True:
		R_value = ui.horizon_R.value() # horizon Bar의 값 가져오기
		G_value = ui.horizon_G.value()
		B_value = ui.horizon_B.value()
		ui.btn_color.setStyleSheet("background-color:rgb(%d, %d, %d);" % (R_value, G_value, B_value)) # 버튼 색깔 설정하기
		print(R_value, G_value, B_value)
		sleep(0.1)

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