# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TreeWindowUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TreeWindow(object):
    def setupUi(self, TreeWindow):
        TreeWindow.setObjectName("TreeWindow")
        TreeWindow.resize(800, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons/JSON格式化.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TreeWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(TreeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.setStyleSheet("font: 12pt \"Consolas\";")
        self.horizontalLayout.addWidget(self.treeWidget)
        TreeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(TreeWindow)
        QtCore.QMetaObject.connectSlotsByName(TreeWindow)

    def retranslateUi(self, TreeWindow):
        _translate = QtCore.QCoreApplication.translate
        TreeWindow.setWindowTitle(_translate("TreeWindow", "Json Struct"))
import resource_rc
