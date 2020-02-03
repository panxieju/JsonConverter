# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CodeWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CodeWindow(object):
    def setupUi(self, CodeWindow):
        CodeWindow.setObjectName("CodeWindow")
        CodeWindow.resize(1200, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons/JSON格式化.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CodeWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(CodeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setStyleSheet("font: 12pt \"Consolas\";")
        self.plainTextEdit.setTabStopWidth(40)
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        CodeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CodeWindow)
        QtCore.QMetaObject.connectSlotsByName(CodeWindow)

    def retranslateUi(self, CodeWindow):
        _translate = QtCore.QCoreApplication.translate
        CodeWindow.setWindowTitle(_translate("CodeWindow", "Code Preview"))
        self.pushButton.setText(_translate("CodeWindow", "Copy"))
        self.pushButton_2.setText(_translate("CodeWindow", "Save"))
import resource_rc
