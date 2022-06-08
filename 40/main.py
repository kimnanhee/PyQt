from PyQt5 import QtCore, QtGui, QtWidgets
from ui import *


set_list = [['등', 60, '보통', False, False, True], ['어깨', 30, '보통', True, True, False]]


def signals(self):
    self.btn_start_1.clicked.connect(self.list_set) # 클릭하면 시작

    self.btn_start_2.clicked.connect(self.openpose_start)
    self.btn_back_2.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(0)) # 뒤로
    self.btn_add_2.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(2)) # 추가
    self.btn_1_2.clicked.connect(lambda: set_list.pop(0)) # 
    # self.btn_2_2.clicked.connect(self.delete_set(1)) # 
    # self.btn_3_2.clicked.connect(self.delete_set(2)) # 
    # self.btn_4_2.clicked.connect(self.delete_set(3)) # 
    # self.btn_5_2.clicked.connect(self.delete_set(4)) # 

    self.btn_save_3.clicked.connect(self.save_set) # 저장
    self.btn_back_3.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(1)) # 뒤로

    self.btn_back_5.clicked.connect(self.list_set) # 뒤로


def list_set(self):
    print(set_list)
    for row in range(5):
        if row < len(set_list):
            self.table_list[row][0].setText(set_list[row][0])
            con = "너비 : %10s | %d s\n봉 사용 : %10s | 무릎 사용 %s" % (set_list[row][2], set_list[row][1], "가로 " if set_list[row][3] else " "+"세로" if set_list[row][4] else "", "O" if set_list[row][5] else "X")
            self.table_list[row][1].setText(con)
        else:
            self.table_list[row][0].setText("")
            self.table_list[row][1].setText("")
    self.stackedWidget.setCurrentIndex(1)


def save_set(self):
    if len(set_list) < 5: # 세트 추가
        radio_value = None
        if self.radio_1_3.isChecked(): radio_value = "좁게"
        elif self.radio_2_3.isChecked(): radio_value = "보통"
        elif self.radio_3_3.isChecked(): radio_value = "넓게"
        
        if self.text_name_3.toPlainText() and self.text_time_3.toPlainText() and radio_value:
            set_list.append([self.text_name_3.toPlainText(), int(self.text_time_3.toPlainText()), radio_value,
                self.check_ga_3.isChecked(), self.check_se_3.isChecked(), self.check_mu_3.isChecked()])

            self.text_name_3.clear()
            self.text_time_3.clear()
            self.radio_1_3.setChecked(False)
            self.radio_2_3.setChecked(False)
            self.radio_3_3.setChecked(False)
            self.check_ga_3.setChecked(False)
            self.check_se_3.setChecked(False)
            self.check_mu_3.setChecked(False)

            list_set(self)
    else:
        self.stackedWidget.setCurrentIndex(1)


def delete_set(self, num: int):
    if len(set_list) > num:
        set_list.pop(num)
        list_set(self)


def openpose_start(self):
    pass

Ui_Form.signals = signals
Ui_Form.list_set = list_set
Ui_Form.save_set = save_set
Ui_Form.delete_set = delete_set
Ui_Form.openpose_start = openpose_start


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    ui.signals()

    ui.table_list = [
        [ui.label_name_1_2, ui.label_con1_1_2],
        [ui.label_name_2_2, ui.label_con1_2_2],
        [ui.label_name_3_2, ui.label_con1_3_2],
        [ui.label_name_4_2, ui.label_con1_4_2],
        [ui.label_name_5_2, ui.label_con1_5_2]
    ]

    ui.label_start_1.setPixmap(QtGui.QPixmap("exercise.jpg"))
    ui.stackedWidget.setCurrentIndex(0)
    
    Form.show()
    sys.exit(app.exec_())