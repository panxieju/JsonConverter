import json
import os

from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from ComparatorUi import Ui_Comparator
from utils.Config import Config
from utils.comparator import compare


class CompareTool(QMainWindow, Ui_Comparator):

    def __init__(self, parent=None):
        super(CompareTool, self).__init__(parent=parent)
        self.setupUi(self)

        self.textEdit.textChanged.connect(self.compare)
        self.textEdit_2.textChanged.connect(self.compare)
        self.pushButton_2.clicked.connect(self.openDest)

    def openDest(self):
        try:
            config = Config.readConfig()
            lastOpenDir = config['lastOpenDir']
        except:
            lastOpenDir = './'
        file, type = QFileDialog.getOpenFileName(self, 'Open a JSon file', lastOpenDir)
        if file:
            dir = os.path.dirname(file)
            Config.writeConfig({'lastOpenDir': dir})
            try:
                f = open(file, 'r', encoding='utf-8')
                text = f.read()
                data = json.load(f)
                self.textEdit_2.setPlainText(text)
                f.close()
            except:
                QMessageBox.warning(self, 'Error', 'Not JSon')

    def setSource(self, text):
        self.textEdit.setPlainText(text)

    def compare(self):
        text1 = self.textEdit.toPlainText()
        text2 = self.textEdit_2.toPlainText()
        if not text1 or not text2:
            return

        data1 = json.loads(text1, encoding='utf-8')
        data2 = json.loads(text2, encoding='utf-8')
        isSame, err = compare(data1, data2)
        if isSame:
            self.textBrowser.setVisible(False)
            self.statusBar.showMessage('Same JSon')
        else:
            promote = 'Note：\n\tThis comparator only compares the keys and the type of values, ignors all the real value\n\n'
            self.textBrowser.setText(promote + err)
            self.textBrowser.setVisible(True)
            self.statusBar.showMessage('Not same JSon')
