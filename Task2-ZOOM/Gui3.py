# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui3.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1152, 935)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("color: rgb(170, 85, 0);\n"
"background-color: rgb(30, 163, 200);\n"
"background-image: url(\"E:/Year3 Term1/Image processing/Task2/canvas.png\");")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 1191, 931))
        self.tabWidget.setStyleSheet("border-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"color: rgb(0, 0, 0);\n"
"gridline-color: rgb(255, 170, 255);\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.Image = QtWidgets.QLabel(self.tab_3)
        self.Image.setGeometry(QtCore.QRect(20, 70, 731, 511))
        self.Image.setText("")
        self.Image.setAlignment(QtCore.Qt.AlignCenter)
        self.Image.setObjectName("Image")
        self.Info = QtWidgets.QLabel(self.tab_3)
        self.Info.setGeometry(QtCore.QRect(800, 20, 291, 681))
        self.Info.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.Info.setText("")
        self.Info.setObjectName("Info")
        self.Browse = QtWidgets.QPushButton(self.tab_3)
        self.Browse.setGeometry(QtCore.QRect(160, 690, 271, 51))
        self.Browse.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 170, 255);")
        self.Browse.setObjectName("Browse")
        self.ZoomFactor = QtWidgets.QLineEdit(self.tab_3)
        self.ZoomFactor.setGeometry(QtCore.QRect(110, 760, 361, 41))
        self.ZoomFactor.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.ZoomFactor.setObjectName("ZoomFactor")
        self.KNNBtn = QtWidgets.QPushButton(self.tab_3)
        self.KNNBtn.setGeometry(QtCore.QRect(550, 760, 171, 41))
        self.KNNBtn.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 170, 255);")
        self.KNNBtn.setObjectName("KNNBtn")
        self.BilinearBtn = QtWidgets.QPushButton(self.tab_3)
        self.BilinearBtn.setGeometry(QtCore.QRect(770, 760, 171, 41))
        self.BilinearBtn.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 170, 255);")
        self.BilinearBtn.setObjectName("BilinearBtn")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.Tab2Label = QtWidgets.QLabel(self.tab_2)
        self.Tab2Label.setGeometry(QtCore.QRect(30, 50, 721, 521))
        self.Tab2Label.setStyleSheet("border-color: rgb(0, 255, 255);")
        self.Tab2Label.setText("")
        self.Tab2Label.setObjectName("Tab2Label")
        self.splitter = QtWidgets.QSplitter(self.tab_2)
        self.splitter.setGeometry(QtCore.QRect(810, 170, 221, 131))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.GenerateBtn = QtWidgets.QPushButton(self.splitter)
        self.GenerateBtn.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 255, 255);")
        self.GenerateBtn.setObjectName("GenerateBtn")
        self.ShowPixels = QtWidgets.QPushButton(self.splitter)
        self.ShowPixels.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(170, 255, 255);")
        self.ShowPixels.setObjectName("ShowPixels")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.ZoomLabel = QtWidgets.QLabel(self.tab)
        self.ZoomLabel.setGeometry(QtCore.QRect(20, 20, 1441, 851))
        self.ZoomLabel.setText("")
        self.ZoomLabel.setObjectName("ZoomLabel")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p>Zoom</p></body></html>"))
        self.Browse.setText(_translate("MainWindow", "Browse Image"))
        self.ZoomFactor.setText(_translate("MainWindow", "Click here and choose zoom factor"))
        self.KNNBtn.setText(_translate("MainWindow", "KNN"))
        self.BilinearBtn.setText(_translate("MainWindow", "Bilinear"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tab1"))
        self.GenerateBtn.setText(_translate("MainWindow", "Generate"))
        self.ShowPixels.setText(_translate("MainWindow", "Show Pixels"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Zoomed"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

