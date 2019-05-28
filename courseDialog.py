# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'courseDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.courseDialog = QtWidgets.QDialogButtonBox(Dialog)
        self.courseDialog.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.courseDialog.setOrientation(QtCore.Qt.Horizontal)
        self.courseDialog.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.courseDialog.setObjectName("courseDialog")
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
        self.codeInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.codeInput.setObjectName("codeInput")
        self.verticalLayout.addWidget(self.codeInput)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.registeredStudentsInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.registeredStudentsInput.setObjectName("registeredStudentsInput")
        self.verticalLayout.addWidget(self.registeredStudentsInput)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.titleInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.titleInput.setObjectName("titleInput")
        self.verticalLayout.addWidget(self.titleInput)

        self.retranslateUi(Dialog)
        # self.courseDialog.accepted.connect(self.accept)
        # self.courseDialog.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Course Code"))
        self.label_2.setText(_translate("Dialog", "Number of Students"))
        self.label_3.setText(_translate("Dialog", "Course Title"))




# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
