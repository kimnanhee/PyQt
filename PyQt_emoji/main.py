from PyQt5 import QtCore, QtGui, QtWidgets
from emoji import *


word_dict = {
   "기쁨": ["😀", "😁", "😃", "😆", "😊", "😊", "😊", "😊", "😊", "😊"],
   "happy": ["😀", "😁", "😃", "😆", "😊"],
   "슬픔": ["😰", "😫", "😥", "😭", "😢"],
   "sad": ["😰", "😫", "😥", "😭", "😢"],
   "즐거움": ["🤩", "🤗", "😚", "😙", "😝"],
   "joy": ["🤩", "🤗", "😚", "😙", "😝"],
   "사랑": ["😻", "🥰", "😍", "😘", "❤"],
   "love": ["😻", "🥰", "😍", "😘", "❤"],
   "분노": ["😡", "🤬", "👿", "😠", "😤"],
   "angry": ["😡", "🤬", "👿", "😠", "😤"],
}

# 시그널
def signals(self):
    self.textEdit.textChanged.connect(self.check)

# 단어 체크
def check(self):
    word = self.textEdit.toPlainText()

    if word in word_dict:
        emo_list = word_dict[word]

        for i, v in enumerate(emo_list):
            self.button_list[i].setText(v)
    else:
        for button in self.button_list:
            button.setText("😶")

# 함수 등록
Ui_MainWindow.signals = signals
Ui_MainWindow.check = check

# 메인
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.button_list = [ui.btn_1, ui.btn_2, ui.btn_3, ui.btn_4, ui.btn_5, ui.btn_6, ui.btn_7, ui.btn_8, ui.btn_9, ui.btn_10]
    ui.signals()
    ui.check()

    MainWindow.show()
    sys.exit(app.exec_())
