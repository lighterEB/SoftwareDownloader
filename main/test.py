import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QPushButton, QWidget, QFileDialog
from PyQt5.QtCore import *
import MainWin
import func
import DownLoadWin

class Action(QMainWindow, MainWin.Ui_MainWindow, DownLoadWin.Ui_Form):
    def __init__(self):
        super(Action, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.printText)
    def printText(self):
        a = self.lineEdit.text()
        self.b = func.Func(a).getInfo()
        self.tableWidgets.setRowCount(int(self.b[1][0]))

        for key, item in self.b[0].items():
            if item[2] == '2':
                item[0] += '64位'
            name = QTableWidgetItem(item[0])
            version = QTableWidgetItem(item[1])
            fileSize = QTableWidgetItem(str("%.2f" % (int(item[3])/(1024*1024))) + "M")
            publishDate = QTableWidgetItem(item[4])
            desc = QTableWidgetItem(item[5])
            rank = QTableWidgetItem(str(int(item[6]) / 10) + "分")
            self.downloadButton = QPushButton()
            self.downloadButton.setText("下载")
            self.tableWidgets.setItem(key, 0, name)
            self.tableWidgets.setItem(key, 1, version)
            self.tableWidgets.setItem(key, 2, fileSize)
            self.tableWidgets.setItem(key, 3, publishDate)
            self.tableWidgets.setItem(key, 4, desc)
            self.tableWidgets.setItem(key, 5, rank)
            self.tableWidgets.setCellWidget(key, 6, self.downloadButton)
            self.downloadButton.clicked.connect(self.download)
        return self.b[0]

    def download(self):
        row = self.tableWidgets.currentRow()
        fileName = QFileDialog.getSaveFileName(self, "", self.b[0][row][8])
        print(type(fileName))
        print(self.b[0][row][8])
        self.form = DownLoadWin.Ui_Form()
        self.form.show()







if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = Action()
    mainWin.show()
    sys.exit(app.exec_())