# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\fwdbui.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 154)
        self.addButton = QtWidgets.QPushButton(Dialog)
        self.addButton.setGeometry(QtCore.QRect(10, 110, 371, 23))
        self.addButton.setObjectName("addButton")
        self.facilityBox = QtWidgets.QComboBox(Dialog)
        self.facilityBox.setGeometry(QtCore.QRect(10, 70, 371, 22))
        self.facilityBox.setObjectName("facilityBox")
        self.ipEdit = QtWidgets.QLineEdit(Dialog)
        self.ipEdit.setGeometry(QtCore.QRect(10, 30, 371, 20))
        self.ipEdit.setObjectName("ipEdit")
        self.ipLabel = QtWidgets.QLabel(Dialog)
        self.ipLabel.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.ipLabel.setObjectName("ipLabel")
        self.ipLabel_2 = QtWidgets.QLabel(Dialog)
        self.ipLabel_2.setGeometry(QtCore.QRect(10, 50, 231, 16))
        self.ipLabel_2.setObjectName("ipLabel_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add a firewall to the database by IP"))
        self.addButton.setText(_translate("Dialog", "Add to DB"))
        self.ipEdit.setPlaceholderText(_translate("Dialog", "IP Address"))
        self.ipLabel.setText(_translate("Dialog", "Enter the IP address for a firewall"))
        self.ipLabel_2.setText(_translate("Dialog", "Select the facility where the firewall is installed"))

