# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Authorization.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication



class Ui_MainWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(222, 126)
        Dialog.setStyleSheet("background-color: rgb(71, 147, 170);\n"
"")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 401, 221))
        self.frame.setStyleSheet("background-color: rgb(238, 250, 253);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 250, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(206, 232, 226)")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 50, 250, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(206, 232, 226)")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 30, 290, 16))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 290, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 90, 100, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Авторизация"))
        self.label.setText(_translate("Dialog", "Введите почту или телефон"))
        self.label_4.setText(_translate("Dialog", "Введите пароль"))
        self.pushButton.setText(_translate("Dialog", " Вход"))
        self.pushButton_2.setText(_translate("Dialog", "Регистрация"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.resize(270, 140)
    MainWindow.show()
    sys.exit(app.exec_())