# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WrittenDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_writtenHallDialog(object):
    def setupUi(self, writtenHallDialog):
        writtenHallDialog.setObjectName("writtenHallDialog")
        writtenHallDialog.resize(400, 300)
        self.widget = QtWidgets.QWidget(writtenHallDialog)
        self.widget.setGeometry(QtCore.QRect(0, 10, 391, 281))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.nameInput = QtWidgets.QLineEdit(self.widget)
        self.nameInput.setObjectName("nameInput")
        self.verticalLayout.addWidget(self.nameInput)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lecturesInput = QtWidgets.QLineEdit(self.widget)
        self.lecturesInput.setObjectName("lecturesInput")
        self.verticalLayout.addWidget(self.lecturesInput)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.capOneInput = QtWidgets.QLineEdit(self.widget)
        self.capOneInput.setObjectName("capOneInput")
        self.verticalLayout.addWidget(self.capOneInput)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.capTwoInput = QtWidgets.QLineEdit(self.widget)
        self.capTwoInput.setObjectName("capTwoInput")
        self.verticalLayout.addWidget(self.capTwoInput)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(writtenHallDialog)
        self.buttonBox.accepted.connect(writtenHallDialog.accept)
        self.buttonBox.rejected.connect(writtenHallDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(writtenHallDialog)

    def retranslateUi(self, writtenHallDialog):
        _translate = QtCore.QCoreApplication.translate
        writtenHallDialog.setWindowTitle(_translate("writtenHallDialog", "Dialog"))
        self.label.setText(_translate("writtenHallDialog", "Hall Name "))
        self.label_2.setText(_translate("writtenHallDialog", "CAPACITY FOR LECTURES"))
        self.label_3.setText(_translate("writtenHallDialog", "CAPACITY FOR ONE EXAM"))
        self.label_4.setText(_translate("writtenHallDialog", "CAPACITY FOR TWO EXAMS"))





