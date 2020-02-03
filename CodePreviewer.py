from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox

from CodeWindowUi import Ui_CodeWindow


class CodePreviewer(QMainWindow, Ui_CodeWindow):

    def __init__(self, parent):
        super(CodePreviewer, self).__init__(parent=parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.copy)
        self.pushButton_2.clicked.connect(self.save)

    def copy(self):
        text = self.plainTextEdit.toPlainText()
        clipBoard = QtWidgets.QApplication.clipboard()
        clipBoard.setText(text)
        QMessageBox.information(self,'JsonAll', 'Copy Success!')

    def save(self):
        if self.language == 'java':
            ext = 'java'
            type = 'Java(*.java)'
        elif self.language == 'kotlin':
            ext = 'kt'
            type = "Kotlin(*.kt)"
        elif self.language == 'go':
            ext = 'go'
            type = 'Go(*.go)'
        filepath, type = QFileDialog.getSaveFileName(self,'保存','./demo.%s'% ext, type)
        if filepath:
            file = open(filepath,'w', encoding='utf-8')
            file.write(self.plainTextEdit.toPlainText())
            file.flush()
            file.close()
            QMessageBox.information(self,'JsonAll','Save Success!')

    def setCode(self, code):
        self.plainTextEdit.setPlainText(code)

    def setLanguage(self, language):
        self.language = language

