from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
import threading

from ui import *


def signals(self):
    self.btn_start_1.clicked.connect(self.list_set) # 클릭하면 시작

    self.btn_start_2.clicked.connect(self.flag_set)
    self.btn_back_2.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(0)) # 뒤로
    self.btn_add_2.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(2)) # 세트 추가
    self.btn_1_2.clicked.connect(lambda : self.delete_set(0))
    self.btn_2_2.clicked.connect(lambda : self.delete_set(1))
    self.btn_3_2.clicked.connect(lambda : self.delete_set(2))
    self.btn_4_2.clicked.connect(lambda : self.delete_set(3))
    self.btn_5_2.clicked.connect(lambda : self.delete_set(4))

    self.btn_save_3.clicked.connect(self.save_set) # 세트 저장
    self.btn_back_3.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(1)) # 뒤로

    self.btn_back_5.clicked.connect(self.list_set) # 뒤로


def list_set(self): # 세트 목록
    print(self.set_list)
    for row in range(5):
        if row < len(self.set_list):
            self.table_list[row][0].setText(self.set_list[row][0])
            con = "너비 : {0:10} | {1} s\n봉 사용 : {2:10} | 무릎 사용 {3}".format(
                self.set_list[row][2], self.set_list[row][1], 
                "가로 " if self.set_list[row][3] else " "+"세로" if self.set_list[row][4] else "", "O" if self.set_list[row][5] else "X"
            )
            self.table_list[row][1].setText(con)
        else:
            self.table_list[row][0].setText("")
            self.table_list[row][1].setText("")
    self.stackedWidget.setCurrentIndex(1)


def save_set(self): # 세트 추가
    if len(self.set_list) < 5:
        radio_value = None
        if self.radio_1_3.isChecked(): radio_value = "좁게"
        elif self.radio_2_3.isChecked(): radio_value = "보통"
        elif self.radio_3_3.isChecked(): radio_value = "넓게"
        
        if self.text_name_3.toPlainText() and self.text_time_3.toPlainText() and radio_value:
            self.set_list.append([self.text_name_3.toPlainText(), int(self.text_time_3.toPlainText()), radio_value,
                self.check_ga_3.isChecked(), self.check_se_3.isChecked(), self.check_mu_3.isChecked()])

            self.text_name_3.clear()
            self.text_time_3.clear()
            self.radio_1_3.setChecked(False)
            self.radio_2_3.setChecked(False)
            self.radio_3_3.setChecked(False)
            self.check_ga_3.setChecked(False)
            self.check_se_3.setChecked(False)
            self.check_mu_3.setChecked(False)

            self.list_set()
    else:
        self.stackedWidget.setCurrentIndex(1)


def delete_set(self, num: int): # 세트 삭제
    if len(self.set_list) > num:
        self.set_list.pop(num)
        self.list_set()


def flag_set(self):
    self.flag = True


def start_set(self):
    while True:
        if self.flag:
            check_list = []
            for i, v in enumerate(self.table_list):
                if v[2].isChecked(): check_list.append(i)
            print("check list : ", check_list)

            self.stackedWidget.setCurrentIndex(3)

            for check in check_list:
                self.label_name_4.setText(self.set_list[check][0]) # 이름
                self.label_set_4.setText("") # 세트
                self.label_cnt_4.setText("") # 횟수
                self.label_time_4.setText("1") # 초
                print(check)
                sleep(2)

            self.flag = False
            self.end_set()


def end_set(self):
    for row in range(5):
        if row < len(self.res_list):
            self.table_list[row][3].setText("{0:20} {1}세트  {2}회  총 진행시간 {3}s".format(self.set_list[row][0], self.res_list[row][0], self.res_list[row][1], self.res_list[row][2]))
        else:
            self.table_list[row][3].setText("")
    
    self.stackedWidget.setCurrentIndex(4)


Ui_Form.signals = signals
Ui_Form.list_set = list_set
Ui_Form.save_set = save_set
Ui_Form.delete_set = delete_set
Ui_Form.flag_set = flag_set
Ui_Form.start_set = start_set
Ui_Form.end_set = end_set


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    ui.signals()

    ui.table_list = [
        [ui.label_name_1_2, ui.label_con1_1_2, ui.checkBox_1_2, ui.label_1_5],
        [ui.label_name_2_2, ui.label_con1_2_2, ui.checkBox_2_2, ui.label_2_5],
        [ui.label_name_3_2, ui.label_con1_3_2, ui.checkBox_3_2, ui.label_3_5],
        [ui.label_name_4_2, ui.label_con1_4_2, ui.checkBox_4_2, ui.label_4_5],
        [ui.label_name_5_2, ui.label_con1_5_2, ui.checkBox_5_2, ui.label_5_5]
    ]
    ui.set_list = [['등', 60, '보통', False, False, True], ['어깨', 30, '보통', True, True, False]]
    ui.res_list = [[2, 2, 60], [5, 1, 300]]
    ui.flag = False

    ui.label_start_1.setPixmap(QtGui.QPixmap("exercise.jpg"))
    ui.stackedWidget.setCurrentIndex(0)

    th = threading.Thread(target=start_set, args=(ui,)) # 스레드 설정
    th.daemon = True
    th.start()
    
    Form.show()
    sys.exit(app.exec_())