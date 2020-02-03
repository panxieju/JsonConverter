import json
import os

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QTreeWidgetItem, QFileDialog

from CodePreviewer import CodePreviewer
from CompareTool import CompareTool
from CurlTools import CurTools
from TreeWindow import TreeWindow
from TreeWindowUi import Ui_TreeWindow
from JsonConverterUi import Ui_MainWindow
from utils.Config import Config
from utils.formater import jsonFormater
from utils.go_converter import generateGoStruct
from utils.java_converter import generateJavaClass
from utils.kotlin_converter import generateKotlinClass
from utils.type_discover import genTree

class MainWindow(QMainWindow,Ui_MainWindow):
    isValidJson = False
    curlTool = 1

    def __init__(self):
        super(MainWindow, self).__init__(parent=None)
        self.clipBoard = QtWidgets.QApplication.clipboard()
        self.setupUi(self)
        self.setWindowTitle('JsonAll')
        self.defineButtons()
        self.textEdit.textChanged.connect(self.onTextChanged)
        #self.treeWidget.setHeaderHidden(True)
        #self.treeWidget.setVisible(False)

    def defineButtons(self):
        self.setButtons(False)
        self.actionClear.setEnabled(False)
        self.actionCopy.setEnabled(False)
        self.actionClear.triggered.connect(self.clear)
        self.actionPaste.triggered.connect(self.paste)
        self.actionFormat.triggered.connect(self.format)
        self.actionOpen.triggered.connect(self.openJson)
        self.actionTree.triggered.connect(self.showTree)
        self.actionJava.triggered.connect(self.convertToJava)
        self.actionKotlin.triggered.connect(self.convertToKotlin)
        self.actionGolang.triggered.connect(self.convertToGo)
        self.actionCopy.triggered.connect(self.copy)
        self.actionCurl.triggered.connect(self.curl)
        self.actionCompare.triggered.connect(self.compare)
        self.actionAbout.triggered.connect(self.about)

    def compare(self):
        self.compareTool =CompareTool()
        self.compareTool.setSource(self.textEdit.toPlainText())
        self.compareTool.show()

    def copy(self):
        text = self.textEdit.toPlainText()
        self.clipBoard.setText(text)
        self.statusbar.showMessage("Copy Suceess!")

    def curl(self):
        self.curlTool = CurTools(self)
        self.curlTool.getResponse.connect(self.pasteResponse)
        self.curlTool.show()

    @pyqtSlot(str)
    def pasteResponse(self, text):
        self.textEdit.setPlainText(text)

    def convertToJava(self):
        code, err = generateJavaClass(self.data)
        if err == 0:
            previewer = CodePreviewer(self)
            previewer.setCode(code)
            previewer.setLanguage('java')
            previewer.show()

    def convertToKotlin(self):
        code, err = generateKotlinClass(self.data)
        if err == 0:
            previewer = CodePreviewer(self)
            previewer.setCode(code)
            previewer.setLanguage('kotlin')
            previewer.show()

    def convertToGo(self):
        code, err = generateGoStruct(self.data)
        if err == 0:
            previewer = CodePreviewer(self)
            previewer.setCode(code)
            previewer.setLanguage('go')
            previewer.show()

    def showTree(self):
        treeWindow = TreeWindow(self)
        treeWindow.setData(self.data)
        treeWindow.show()

    def openJson(self):
        try:
            config = Config.readConfig()
            lastOpenDir = config['lastOpenDir']
        except:
            lastOpenDir = './'
        file, type = QFileDialog.getOpenFileName(self,'Open JSon file',lastOpenDir)
        if not file:
            return
        else:
            dir = os.path.dirname(file)
            Config.writeConfig({'lastOpenDir':dir})
            file = open(file,'r', encoding='utf-8')
            content = file.read()
            if content:
                self.textEdit.setText(content)

    def clear(self):
        self.textEdit.clear()
        self.setButtons(False)
        self.statusbar.clearMessage()
        self.actionClear.setEnabled(False)
        self.actionCopy.setEnabled(False)

    def paste(self):
        self.clearOutput()
        text = self.clipBoard.text()
        self.textEdit.setText(text)

    def clearOutput(self, fromTextEditChanged=False):
        if fromTextEditChanged:
            self.textEdit.clear()
        self.statusbar.clearMessage()
        #self.treeWidget.clear()

    def onTextChanged(self):
        text = self.textEdit.toPlainText()
        if text:
            self.check_input(text)
        else:
            self.statusbar.clearMessage()
            #self.treeWidget.clear()

    def check_input(self, text):
        self.actionClear.setEnabled(True)
        self.actionCopy.setEnabled(True)
        try:
            self.data = json.loads(text)
            self.setButtons(True)
            self.isValidJson = True
            self.statusbar.clearMessage()
        except:
            self.isValidJson = False
            self.statusbar.showMessage("Not JSon")
            self.setButtons(False)
            #self.treeWidget.clear()

    def setButtons(self, ena):
        self.actionFormat.setEnabled(ena)
        self.actionJava.setEnabled(ena)
        self.actionKotlin.setEnabled(ena)
        self.actionGolang.setEnabled(ena)
        self.actionTree.setEnabled(ena)
        self.actionCompare.setEnabled(ena)

    def format(self):
        text = self.textEdit.toPlainText()
        result = jsonFormater(text)
        self.textEdit.setText(result)

    def about(self):
        #genTree(self.treeWidget, self.data)
        QtGui.QDesktopServices.openUrl(QtCore.QUrl('http://www.nexttec.cn'))









