# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1176, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1176, 640))
        MainWindow.setMaximumSize(QtCore.QSize(1176, 640))
        self.tipLabel = QtWidgets.QLabel(MainWindow)
        self.tipLabel.setGeometry(QtCore.QRect(1000, 590, 141, 31))
        self.tipLabel.setText("")
        self.tipLabel.setObjectName("tipLabel")
        self.tableWidget = QtWidgets.QTableWidget(MainWindow)
        self.tableWidget.setGeometry(QtCore.QRect(20, 90, 1136, 490))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setColumnWidth(0,180)
        self.tableWidget.setColumnWidth(1,120)
        self.tableWidget.setColumnWidth(2,80)
        self.tableWidget.setColumnWidth(3,100)
        self.tableWidget.setColumnWidth(4,500)
        self.tableWidget.setColumnWidth(5,50)
        self.tableWidget.setColumnWidth(6,100)
        self.tableWidget.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setHorizontalHeaderLabels(['名称', '版本', '大小', '发布日期', '描述', '评分', ''])
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setGeometry(QtCore.QRect(500, 40, 651, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.searchButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setMinimumSize(QtCore.QSize(0, 0))
        self.searchButton.setText("")
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.horizontalLayout.setStretch(0, 2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pure Software Downloader"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "在这里输入你要找的软件"))
        self.label.setText(_translate("MainWindow", "软件库"))
        self.comboBox.setItemText(0, _translate("MainWindow", "腾讯"))
        self.comboBox.setItemText(1, _translate("MainWindow", "360"))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWin = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(mainWin)
    mainWin.show()
    sys.exit(app.exec_())