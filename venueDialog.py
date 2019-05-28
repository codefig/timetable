# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hallDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Venue_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.hallDialog = QtWidgets.QDialogButtonBox(Dialog)
        self.hallDialog.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.hallDialog.setOrientation(QtCore.Qt.Horizontal)
        self.hallDialog.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.hallDialog.setObjectName("hallDialog")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 401, 241))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 411, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.hallNameInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.hallNameInput.setObjectName("hallNameInput")
        self.verticalLayout.addWidget(self.hallNameInput)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.hallCapacityInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.hallCapacityInput.setObjectName("hallCapacityInput")
        self.verticalLayout.addWidget(self.hallCapacityInput)
     
  

        self.retranslateUi(Dialog)
        # self.hallDialog.accepted.connect(self.accept)
        # self.hallDialog.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CBT Halls"))
        self.label.setText(_translate("Dialog", "Hall Name"))
        self.label_2.setText(_translate("Dialog", "Hall Capacity"))
