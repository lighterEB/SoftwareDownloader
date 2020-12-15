# -*- coding: utf-8 -*-

# 主窗口及功能



from PyQt5 import QtCore, QtGui, QtWidgets
import func
import DownloadWin
import requests

# 主窗口
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1196, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1196, 640))
        MainWindow.setMaximumSize(QtCore.QSize(1196, 640))
        self.tipLabel = QtWidgets.QLabel(MainWindow)
        self.tipLabel.setGeometry(QtCore.QRect(1000, 590, 141, 31))
        self.tipLabel.setText("")
        self.tipLabel.setObjectName("tipLabel")
        self.tableWidget = QtWidgets.QTableWidget(MainWindow)
        self.tableWidget.setGeometry(QtCore.QRect(20, 90, 1156, 490))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setColumnWidth(0,275)
        self.tableWidget.setColumnWidth(1,120)
        self.tableWidget.setColumnWidth(2,80)
        self.tableWidget.setColumnWidth(3,100)
        self.tableWidget.setColumnWidth(4,450)
        self.tableWidget.setColumnWidth(5,50)
        self.tableWidget.setColumnWidth(6,60)
        self.tableWidget.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)
        self.tableWidget.setShowGrid(False)
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
        self.searchButton.setIcon(QtGui.QIcon("../src/images/btn_search.png"))
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

# 驱动主窗口和功能
class MainWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)
        # 绑定搜索按钮信号槽
        self.searchButton.clicked.connect(self.searchAppInfo)
    data = {}
    # 查询软件相关信息功能返回字典
    def searchAppInfo(self):
        # 获取输入搜索关键字
        entryText = self.lineEdit.text()
        if entryText == '':
            return
        # 得到处理后的信息字典
        self.infoBox = func.Tencent(entryText).getInfo()

        # 创建表格控件中的行数
        # infoBox[1][0] = 查询到的软件总数
        self.tableWidget.setRowCount(int(self.infoBox[1][0]))

        # 遍历查询到的软件信息
        for key, item in self.infoBox[0].items():
            # item[2] == osbit(系统位数)
            # 如果等于2就是64位
            if item[2] == '2':
                item[0] += '64位'

            # 每个单元格放入相应项目
            version = QtWidgets.QTableWidgetItem(item[1])
            fileSize = QtWidgets.QTableWidgetItem(str("%.2f" % (int(item[3]) / (1024 * 1024))) + "M")
            publishDate = QtWidgets.QTableWidgetItem(item[4])
            desc = QtWidgets.QTableWidgetItem(item[5])
            rank = QtWidgets.QTableWidgetItem(str(int(item[6]) / 10) + "分")
            logo = item[9]
            self.downloadButton = QtWidgets.QPushButton()
            self.downloadButton.setText("下载")
            photo = QtGui.QPixmap()
            photo.loadFromData(requests.get("http://pc3.gtimg.com/softmgr/logo/48/{}".format(logo)).content)
            self.headWidget = QtWidgets.QWidget()
            self.imgLabel = QtWidgets.QLabel()
            self.imgLabel.setPixmap(photo)
            self.textLabel = QtWidgets.QLabel()
            self.textLabel.setText(item[0])
            self.vercalLayout = QtWidgets.QHBoxLayout(self.headWidget)
            self.vercalLayout.addWidget(self.imgLabel)
            self.vercalLayout.addWidget(self.textLabel)
            self.tableWidget.setCellWidget(key, 0, self.headWidget)
            #self.tableWidget.setItem(key, 0, name)
            self.tableWidget.setRowHeight(key, 68)
            self.tableWidget.setItem(key, 1, version)
            self.tableWidget.setItem(key, 2, fileSize)
            self.tableWidget.setItem(key, 3, publishDate)
            self.tableWidget.setItem(key, 4, desc)
            self.tableWidget.setItem(key, 5, rank)
            self.tableWidget.setCellWidget(key, 6, self.downloadButton)
            self.downloadButton.clicked.connect(self.download)

        return self.infoBox[0]
    # 下载信号槽
    def download(self):
        MainWin.data = {}
        row = self.tableWidget.currentRow()
        fileName = QtWidgets.QFileDialog.getSaveFileName(self, "", self.infoBox[0][row][8])
        MainWin.data[row] = fileName
        if fileName[0] != '':
            self.downloadWin = DownloadWin.Form()
            self.downloadWin.setWindowModality(QtCore.Qt.ApplicationModal)
            self.downloadWin.setWindowTitle("下载")
            self.downloadWin.dirPath.setText(fileName[0])
            self.downloadWin.dirPath.setReadOnly(True)
            self.downloadWin.mySignal.connect(self.terminal)
            self.thread = DownloadThread()
            self.thread.signal.connect(self.flushValue)
            self.thread.start()
            self.downloadWin.show()
    # 中断下载
    def terminal(self):
        self.thread.terminate()
    # 刷新下载进度条
    def flushValue(self, value):
        self.downloadWin.progressBar.setValue(value)
        if value == 100:
            self.downloadWin.pushButton.setText("打开文件")
            self.downloadWin.pushButton.setDisabled(False)


# 下载线程类
class DownloadThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(int)
    def run(self):
        import time
        
