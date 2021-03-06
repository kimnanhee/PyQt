# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\serial_test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 470, 360, 40))
        self.lineEdit.setStyleSheet("font: 10pt \"맑은 고딕\";")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_send = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_send.setGeometry(QtCore.QRect(400, 470, 120, 40))
        self.pushButton_send.setStyleSheet("font: 75 10pt \"맑은 고딕\";")
        self.pushButton_send.setObjectName("pushButton_send")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 150, 500, 300))
        self.textEdit.setStyleSheet("font: 10pt \"맑은 고딕\";")
        self.textEdit.setObjectName("textEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 90, 120, 40))
        self.comboBox.setStyleSheet("font: 10pt \"맑은 고딕\";")
        self.comboBox.setObjectName("comboBox")
        self.pushButton_connect = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_connect.setGeometry(QtCore.QRect(160, 90, 120, 40))
        self.pushButton_connect.setStyleSheet("font: 75 10pt \"맑은 고딕\";")
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.pushButton_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_clear.setGeometry(QtCore.QRect(400, 90, 120, 40))
        self.pushButton_clear.setStyleSheet("font: 75 10pt \"맑은 고딕\";")
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 500, 50))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 16pt \"맑은 고딕\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_send.setText(_translate("MainWindow", "Send"))
        self.pushButton_connect.setText(_translate("MainWindow", "Connect"))
        self.pushButton_clear.setText(_translate("MainWindow", "Clear"))
        self.label.setText(_translate("MainWindow", "Serial Test Program"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
