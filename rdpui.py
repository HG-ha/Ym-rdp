# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rdp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.setEnabled(True)
        Dialog.resize(541, 491)
        Dialog.setAcceptDrops(False)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 541, 491))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 521, 101))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(70, 30, 113, 21))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 51, 21))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 60, 113, 21))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 51, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 30, 113, 21))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(190, 30, 51, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 60, 113, 21))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(190, 60, 51, 21))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(400, 30, 93, 51))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 160, 521, 321))
        self.groupBox_4.setObjectName("groupBox_4")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_4)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 501, 281))
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 541, 41))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 0, 41, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 0, 41, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(20, 0, 41, 41))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "一铭RDP"))
        Dialog.setToolTip(_translate("Dialog", "<html><head/><body><p>一铭的工具箱</p></body></html>"))
        Dialog.setWhatsThis(_translate("Dialog", "<html><head/><body><p>一铭RDP</p></body></html>"))
        self.groupBox.setStatusTip(_translate("Dialog", "主机名"))
        self.groupBox.setTitle(_translate("Dialog", "新增桌面"))
        # self.lineEdit.setToolTip(_translate("Dialog", "<html><head/><body><p>主机名</p></body></html>"))
        # self.lineEdit.setStatusTip(_translate("Dialog", "主机名"))
        self.label.setText(_translate("Dialog", "名称"))
        # self.lineEdit_2.setToolTip(_translate("Dialog", "<html><head/><body><p>主机名</p></body></html>"))
        # self.lineEdit_2.setStatusTip(_translate("Dialog", "主机名"))
        self.label_2.setText(_translate("Dialog", "地址"))
        # self.lineEdit_3.setToolTip(_translate("Dialog", "<html><head/><body><p>主机名</p></body></html>"))
        # self.lineEdit_3.setStatusTip(_translate("Dialog", "主机名"))
        self.label_3.setText(_translate("Dialog", "账号"))
        # self.lineEdit_4.setToolTip(_translate("Dialog", "<html><head/><body><p>主机名</p></body></html>"))
        # self.lineEdit_4.setStatusTip(_translate("Dialog", "主机名"))
        self.label_4.setText(_translate("Dialog", "密码"))
        self.pushButton.setText(_translate("Dialog", "添加"))
        self.groupBox_4.setTitle(_translate("Dialog", "桌面列表"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "名称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "地址"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "用户名"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "密码"))
        self.pushButton_2.setText(_translate("Dialog", "X"))
        self.pushButton_4.setText(_translate("Dialog", "—"))

