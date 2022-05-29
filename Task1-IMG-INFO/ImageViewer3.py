# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageViewer3.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1104, 841)
        MainWindow.setStyleSheet("background-color:rgb(85, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Image = QtWidgets.QLabel(self.centralwidget)
        self.Image.setGeometry(QtCore.QRect(20, 0, 731, 471))
        self.Image.setText("")
        self.Image.setAlignment(QtCore.Qt.AlignCenter)
        self.Image.setObjectName("Image")
        self.Browse = QtWidgets.QPushButton(self.centralwidget)
        self.Browse.setGeometry(QtCore.QRect(800, 170, 181, 51))
        self.Browse.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.Browse.setObjectName("Browse")
        self.Info = QtWidgets.QLabel(self.centralwidget)
        self.Info.setGeometry(QtCore.QRect(10, 530, 781, 241))
        self.Info.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.Info.setText("")
        self.Info.setObjectName("Info")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1104, 26))
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
        self.Browse.setText(_translate("MainWindow", "Browse Image"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

