
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Mark(object):
    def setupUi(self, Mark):
        Mark.setObjectName("Mark")
        Mark.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Mark)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(
            "D:/CSE 3200/ruet2.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 460, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 460, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 170, 0);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(470, 10, 151, 51))
        self.textBrowser.setStyleSheet("background:transparent;\n"
                                       "color:black;\n"
                                       "font-size:20px;\n"
                                       "border-radius:none;")
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(640, 10, 141, 51))
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
                                         "color:black;\n"
                                         "font-size:20px;\n"
                                         "border-radius:none;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        Mark.setCentralWidget(self.centralwidget)

        self.retranslateUi(Mark)
        QtCore.QMetaObject.connectSlotsByName(Mark)

    def retranslateUi(self, Mark):
        _translate = QtCore.QCoreApplication.translate
        Mark.setWindowTitle(_translate("Mark", "MainWindow"))
        self.pushButton.setText(_translate("Mark", "Exit"))
        self.pushButton_2.setText(_translate("Mark", "RUN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Mark = QtWidgets.QMainWindow()
    ui = Ui_Mark()
    ui.setupUi(Mark)
    Mark.show()
    sys.exit(app.exec_())
