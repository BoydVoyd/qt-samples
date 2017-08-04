# Copyright (C) 2015 The Qt Company Ltd.
# Contact: http://www.qt.io/licensing/
# **
# This file is part of the examples of the Qt Toolkit.
# **
# $QT_BEGIN_LICENSE:BSD$
# You may use this file under the terms of the BSD license as follows:
# **
# "Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in
#     the documentation and/or other materials provided with the
#     distribution.
#   * Neither the name of The Qt Company Ltd nor the names of its
#     contributors may be used to endorse or promote products derived
#     from this software without specific prior written permission.
# **
# **
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
# **
# $QT_END_LICENSE$
# this is an arbitrary change
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\maindialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 208)
        self.previousButton = QtWidgets.QPushButton(Dialog)
        self.previousButton.setGeometry(QtCore.QRect(310, 10, 75, 23))
        self.previousButton.setObjectName("previousButton")
        self.nextButton = QtWidgets.QPushButton(Dialog)
        self.nextButton.setGeometry(QtCore.QRect(310, 40, 75, 23))
        self.nextButton.setObjectName("nextButton")
        self.nameEdit = QtWidgets.QLineEdit(Dialog)
        self.nameEdit.setGeometry(QtCore.QRect(90, 10, 201, 20))
        self.nameEdit.setObjectName("nameEdit")
        self.addressEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.addressEdit.setGeometry(QtCore.QRect(90, 40, 201, 111))
        self.addressEdit.setObjectName("addressEdit")
        self.typeCombo = QtWidgets.QComboBox(Dialog)
        self.typeCombo.setGeometry(QtCore.QRect(90, 160, 201, 22))
        self.typeCombo.setObjectName("typeCombo")
        self.nameLabel = QtWidgets.QLabel(Dialog)
        self.nameLabel.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.nameLabel.setObjectName("nameLabel")
        self.editLabel = QtWidgets.QLabel(Dialog)
        self.editLabel.setGeometry(QtCore.QRect(10, 40, 47, 13))
        self.editLabel.setObjectName("editLabel")
        self.typeLabel = QtWidgets.QLabel(Dialog)
        self.typeLabel.setGeometry(QtCore.QRect(10, 160, 47, 13))
        self.typeLabel.setObjectName("typeLabel")
        self.nameLabel.setBuddy(self.nameEdit)
        self.editLabel.setBuddy(self.addressEdit)
        self.typeLabel.setBuddy(self.typeCombo)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.previousButton.setText(_translate("Dialog", "Previous"))
        self.nextButton.setText(_translate("Dialog", "Next"))
        self.nameLabel.setText(_translate("Dialog", "Na&me:"))
        self.editLabel.setText(_translate("Dialog", "&Address:"))
        self.typeLabel.setText(_translate("Dialog", "&Type"))

