from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QUrl, pyqtSlot
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtWebEngineCore
from PyQt5.QtWebEngineWidgets import QWebEngineSettings

class Ui_MainWindow(object):
    widget_List = []
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        MainWindow.setCentralWidget(self.centralwidget)

        self.widget_youtube = QtWidgets.QWidget(self.centralwidget)
        self.widget_List.append(self.widget_youtube)
        self.widget_youtube.setGeometry(QtCore.QRect(0, 0, 800, 800))
        self.widget_youtube.setObjectName("widget_youtube")

        self.webview=QtWebEngineWidgets.QWebEngineView(self.widget_youtube)
        self.webview.setUrl(QUrl("https://www.youtube.com/watch?v=9GxW-0VRu8M"))
        self.webview.setGeometry(0,0,800,800)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())