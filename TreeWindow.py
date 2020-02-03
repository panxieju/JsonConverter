from PyQt5.QtWidgets import QMainWindow

from TreeWindowUi import Ui_TreeWindow
from utils.type_discover import genTree


class TreeWindow(QMainWindow,Ui_TreeWindow):
    def __init__(self, parent=None):
        super(TreeWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.treeWidget.setHeaderHidden(True)

    def setData(self, data):
        genTree(self.treeWidget, data)


