# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\work1.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 20, 760, 400))
        self.graphicsView.setObjectName("graphicsView")
        self.label_temp = QtWidgets.QLabel(self.centralwidget)
        self.label_temp.setGeometry(QtCore.QRect(20, 430, 150, 40))
        self.label_temp.setStyleSheet("font: 12pt \"Arial\";")
        self.label_temp.setObjectName("label_temp")
        self.value_temp = QtWidgets.QLabel(self.centralwidget)
        self.value_temp.setGeometry(QtCore.QRect(170, 430, 100, 40))
        self.value_temp.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);")
        self.value_temp.setText("")
        self.value_temp.setObjectName("value_temp")
        self.label_humi = QtWidgets.QLabel(self.centralwidget)
        self.label_humi.setGeometry(QtCore.QRect(20, 480, 150, 40))
        self.label_humi.setStyleSheet("font: 12pt \"Arial\";")
        self.label_humi.setObjectName("label_humi")
        self.value_humi = QtWidgets.QLabel(self.centralwidget)
        self.value_humi.setGeometry(QtCore.QRect(170, 480, 100, 40))
        self.value_humi.setStyleSheet("font: 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);")
        self.value_humi.setText("")
        self.value_humi.setObjectName("value_humi")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.label_temp.setText(_translate("MainWindow", "Temperature"))
        self.label_humi.setText(_translate("MainWindow", "Humidity"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
