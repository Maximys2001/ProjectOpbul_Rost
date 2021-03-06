# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Algorithm_RDP.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1250, 732)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Pictures/RDP_str.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../../Pictures/RDP_str.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("../../Pictures/RDP_str.png"), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../../Pictures/RDP_str.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("../../Pictures/RDP_str.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../../Pictures/RDP_str.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("../../Pictures/RDP_str.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("../../Pictures/RDP_str.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(233, 255, 240);\n"
"background-color: rgb(40, 127, 140);\n"
"background-color: rgb(71, 147, 170);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 150, 601, 571))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_vvedite_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_vvedite_2.setMaximumSize(QtCore.QSize(1000, 50))
        self.label_vvedite_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(149, 160, 255, 255), stop:1 rgba(164, 231, 174, 255));\n"
"")
        self.label_vvedite_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_vvedite_2.setObjectName("label_vvedite_2")
        self.verticalLayout.addWidget(self.label_vvedite_2)
        self.MplWidget = MplWidget(self.verticalLayoutWidget)
        self.MplWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.MplWidget.setObjectName("MplWidget")
        self.verticalLayout.addWidget(self.MplWidget)
        self.Button_generate = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Button_generate.setStyleSheet("\n"
"background-color: rgb(198, 221, 255);")
        self.Button_generate.setObjectName("Button_generate")
        self.verticalLayout.addWidget(self.Button_generate)
        self.Button_save = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Button_save.setStyleSheet("\n"
"background-color: rgb(198, 221, 255);")
        self.Button_save.setObjectName("Button_save")
        self.verticalLayout.addWidget(self.Button_save)
        self.Button_clear = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Button_clear.setStyleSheet("\n"
"background-color: rgb(198, 221, 255);")
        self.Button_clear.setObjectName("Button_clear")
        self.verticalLayout.addWidget(self.Button_clear)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 33, 600, 101))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.line_x = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.line_x.setSizeIncrement(QtCore.QSize(4, 4))
        self.line_x.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 0, 255);\n"
"border-color: rgb(0, 170, 255);")
        self.line_x.setObjectName("line_x")
        self.verticalLayout_8.addWidget(self.line_x)
        self.label_x = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_x.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_x.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(149, 160, 255, 255), stop:1 rgba(164, 231, 174, 255));\n"
"")
        self.label_x.setAlignment(QtCore.Qt.AlignCenter)
        self.label_x.setObjectName("label_x")
        self.verticalLayout_8.addWidget(self.label_x)
        self.horizontalLayout.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.line_y = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.line_y.setSizeIncrement(QtCore.QSize(5, 5))
        self.line_y.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"gridline-color: rgb(255, 0, 255);\n"
"border-color: rgb(0, 170, 255);")
        self.line_y.setObjectName("line_y")
        self.verticalLayout_9.addWidget(self.line_y)
        self.label_y = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_y.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_y.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(149, 160, 255, 255), stop:1 rgba(164, 231, 174, 255));\n"
"")
        self.label_y.setAlignment(QtCore.Qt.AlignCenter)
        self.label_y.setObjectName("label_y")
        self.verticalLayout_9.addWidget(self.label_y)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton.setStyleSheet("\n"
"background-color: rgb(198, 221, 255);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.label_vvedite = QtWidgets.QLabel(self.centralwidget)
        self.label_vvedite.setGeometry(QtCore.QRect(170, 10, 281, 21))
        self.label_vvedite.setMaximumSize(QtCore.QSize(1000, 50))
        self.label_vvedite.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(149, 160, 255, 255), stop:1 rgba(164, 231, 174, 255));\n"
"")
        self.label_vvedite.setAlignment(QtCore.Qt.AlignCenter)
        self.label_vvedite.setObjectName("label_vvedite")
        self.line_e = QtWidgets.QLineEdit(self.centralwidget)
        self.line_e.setGeometry(QtCore.QRect(750, 60, 219, 31))
        self.line_e.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_e.setObjectName("line_e")
        self.label_e = QtWidgets.QLabel(self.centralwidget)
        self.label_e.setGeometry(QtCore.QRect(750, 30, 121, 21))
        self.label_e.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(149, 160, 255, 255), stop:1 rgba(164, 231, 174, 255));\n"
"")
        self.label_e.setAlignment(QtCore.Qt.AlignCenter)
        self.label_e.setObjectName("label_e")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Algorithm Ramer-Douglas-Peucker "))
        self.label_vvedite_2.setText(_translate("MainWindow", "?????????????????? ???????????????? ???????????? ?? ?????????????? ?????? ?? ?????????????? ??????????????"))
        self.Button_generate.setText(_translate("MainWindow", "??????????????????"))
        self.Button_save.setText(_translate("MainWindow", "??????????????????"))
        self.Button_clear.setText(_translate("MainWindow", "????????????????"))
        self.label_x.setText(_translate("MainWindow", "x"))
        self.label_y.setText(_translate("MainWindow", " ??"))
        self.pushButton.setText(_translate("MainWindow", "???????????????? ?????????????? ??????????????????"))
        self.label_vvedite.setText(_translate("MainWindow", "?????????????? ?????????????? ??????????????????"))
        self.label_e.setText(_translate("MainWindow", "Epsilon:"))
from mplwidget import MplWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
