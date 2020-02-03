# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ComparatorUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Comparator(object):
    def setupUi(self, Comparator):
        Comparator.setObjectName("Comparator")
        Comparator.resize(1513, 821)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons/JSON格式化.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Comparator.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Comparator)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setStyleSheet("font: 11pt \"Consolas\";")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons/open 打开文件.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 32))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setStyleSheet("font: 11pt \"Consolas\";")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit.setTabStopWidth(40)
        self.textEdit_2.setTabStopWidth(40)
        self.verticalLayout_2.addWidget(self.textEdit_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setStyleSheet("border-color: rgb(216, 216, 216);\n"
"font: 12pt \"Consolas\";\n"
"background-color: rgb(216, 216, 216);")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setTabStopWidth(40)
        self.horizontalLayout_3.addWidget(self.textBrowser)
        Comparator.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(Comparator)
        self.statusBar.setObjectName("statusBar")
        Comparator.setStatusBar(self.statusBar)

        self.retranslateUi(Comparator)
        QtCore.QMetaObject.connectSlotsByName(Comparator)

    def retranslateUi(self, Comparator):
        _translate = QtCore.QCoreApplication.translate
        Comparator.setWindowTitle(_translate("Comparator", "JSon Comparator"))
import resource_rc
