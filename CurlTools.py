import datetime
import json
import os
import sys
import requests
from PyQt5.QtCore import pyqtSignal

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QListWidgetItem

from CurlWindowUi import Ui_CurlWindow
from utils.common import genMd5, timestamp


class CurTools(QMainWindow, Ui_CurlWindow):
    logs = []
    md5s = set()
    logFile = 'curl.log'
    getResponse = pyqtSignal(str)

    def __init__(self, parent=None):
        super(CurTools, self).__init__(parent=parent)
        self.setupUi(self)
        self.comboBox.addItems(['GET', 'POST'])
        self.pushButton.clicked.connect(self.curl)
        self.pushButton_2.clicked.connect(self.analyze)
        self.pushButton_2.setEnabled(False)
        self.listWidget.setVisible(False)
        self.listWidget.itemDoubleClicked.connect(self.openLog)
        try:
            f = open(self.logFile, 'r', encoding='utf-8')
            self.logs = json.load(f)
            f.close()
            self.updateLog()
        except:
            self.logs = []

        self.textEdit.setText('')
        self.textEdit_3.textChanged.connect(self.updateStatus)
        self.comboBox.currentIndexChanged.connect(self.changeMethod)

    def changeMethod(self):
        if self.comboBox.currentText() == 'GET':
            self.textEdit.setText('')
        else:
            self.textEdit.setText('{"Content-Type":"application/json"}')

    def updateStatus(self):
        text = self.textEdit_3.toPlainText()
        if text:
            self.pushButton_2.setEnabled(True)
        else:
            self.pushButton_2.setEnabled(False)

    def openLog(self, item):
        index = self.listWidget.currentRow()
        log = self.logs[index]
        self.lineEdit.setText(log['url'])
        self.textEdit.setText(log['headers'])
        self.textEdit_2.setText(log['body'])
        self.textEdit_3.setText(log['response'])
        m = log['method']
        if m == 'POST':
            self.comboBox.setCurrentIndex(1)
        else:
            self.comboBox.setCurrentIndex(0)

    def curl(self):
        headers = None
        data = None
        url = self.lineEdit.text().strip()
        if not url:
            QMessageBox.warning(self,'Error','Need Api address')
            return
        paramText = self.textEdit_2.toPlainText()
        if paramText:
            try:
                data = json.loads(paramText, encoding='urf-8')
            except:
                data = None

        headerText = self.textEdit.toPlainText().strip()
        try:
            headers = json.loads(headerText, encoding='utf-8')
        except:
            headers = None
        method = self.comboBox.currentText().strip()
        if method == 'GET':
            try:
                if data:
                    response = requests.get(url, headers=headers, params=data, timeout=30)
                else:
                    response = requests.get(url, headers=headers, timeout=30)
            except:
                QMessageBox.warning(self, "Error","Sorry, cannot access this url.")
                return
        elif method == 'POST':
            dataText = self.textEdit_2.toPlainText()
            try:
                data = json.loads(dataText, encoding='utf-8')
                response = requests.post(url, headers=headers, json=data, timeout=30)
            except:
                reply = QMessageBox.warning(self, 'Error', 'Not JSON', QMessageBox.Ok)
                return

        if response:
            print(response.text)
            try:
                text = response.content.decode('utf-8')
            except:
                text = response.text
            self.textEdit_3.setPlainText(text)
            md5 = genMd5(url + self.comboBox.currentText())
            log = {
                'url': url,
                'method': self.comboBox.currentText(),
                'headers': self.textEdit.toPlainText(),
                'body': self.textEdit_2.toPlainText(),
                'response': self.textEdit_3.toPlainText(),
                'time': timestamp(),
                'md5': md5
            }
            if md5 not in self.md5s:
                self.md5s.add(md5)
            else:
                for item in self.logs:
                    if item['md5'] == md5:
                        self.logs.remove(item)
            self.logs.append(log)
            self.updateLog()

    def updateLog(self):
        self.logs.sort(key=lambda l: l['time'])
        self.logs.reverse()
        self.listWidget.clear()
        if self.logs:
            self.listWidget.setVisible(True)
            for log in self.logs:
                self.md5s.add(log['md5'])
                item = QListWidgetItem()
                item.setText(log['url'])
                self.listWidget.addItem(item)
            f = open(self.logFile,'w', encoding='utf-8')
            json.dump(self.logs,f)
            f.flush()
            f.close()
        else:
            self.listWidget.setVisible(False)

    def analyze(self):
        text = self.textEdit_3.toPlainText()
        self.getResponse.emit(text)

        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CurTools()
    win.show()
    sys.exit(app.exec_())
