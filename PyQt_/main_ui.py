# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_1.setObjectName("page_1")
        self.pushButton_1 = QtWidgets.QPushButton(self.page_1)
        self.pushButton_1.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.pushButton_1.setText("")
        self.pushButton_1.setObjectName("pushButton_1")
        self.label_1_design1 = QtWidgets.QLabel(self.page_1)
        self.label_1_design1.setGeometry(QtCore.QRect(0, 750, 1200, 50))
        self.label_1_design1.setStyleSheet("background-color: rgb(94, 94, 94);")
        self.label_1_design1.setText("")
        self.label_1_design1.setObjectName("label_1_design1")
        self.label_message = QtWidgets.QLabel(self.page_1)
        self.label_message.setGeometry(QtCore.QRect(520, 610, 200, 50))
        self.label_message.setStyleSheet("font: 12pt \"Arial\";")
        self.label_message.setAlignment(QtCore.Qt.AlignCenter)
        self.label_message.setObjectName("label_message")
        self.label_1_design2 = QtWidgets.QLabel(self.page_1)
        self.label_1_design2.setGeometry(QtCore.QRect(0, 740, 1200, 5))
        self.label_1_design2.setStyleSheet("background-color: rgb(94, 94, 94);")
        self.label_1_design2.setText("")
        self.label_1_design2.setObjectName("label_1_design2")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2.setGeometry(QtCore.QRect(1080, 20, 100, 80))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(20, 20, 1050, 760))
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_message.setText(_translate("MainWindow", "화면을 클릭해주세요"))
        self.pushButton_2.setText(_translate("MainWindow", "Home"))
        self.label.setText(_translate("MainWindow", "fwewwefwefwefwefwefwef"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
