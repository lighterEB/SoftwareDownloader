# -*- coding: utf-8 -*-

# 主窗口及功能



from PyQt5 import QtCore, QtGui, QtWidgets
import func
import DownloadWin

# 主窗口
class Ui_MainWindow(object):
    def __init__(self):
        self.widget = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 480)
        MainWindow.setMaximumSize(QtCore.QSize(1080, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setText("")
        self.pushButton.setObjectName("searchButton")
        self.pushButton.setIcon(QtGui.QIcon("../src/images/btn_search.png"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidgets = QtWidgets.QTableWidget(self.widget)
        self.tableWidgets.setColumnCount(7)
        self.tableWidgets.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)
        self.tableWidgets.setShowGrid(False)
        self.tableWidgets.verticalHeader().setVisible(False)
        self.tableWidgets.setObjectName("tableWidgets")
        self.tableWidgets.setHorizontalHeaderLabels(['名称', '版本', '大小', '发布日期', '描述', '评分', ''])
        self.verticalLayout.addWidget(self.tableWidgets)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
        self.pushButton.clicked.connect(self.searchAppInfo)
    data = {}
    # 查询软件相关信息功能返回字典
    def searchAppInfo(self):
        # 获取输入搜索关键字
        entryText = self.lineEdit.text()

        # 得到处理后的信息字典
        self.infoBox = func.Tencent(entryText).getInfo()

        # 创建表格控件中的行数
        # infoBox[1][0] = 查询到的软件总数
        self.tableWidgets.setRowCount(int(self.infoBox[1][0]))

        # 遍历查询到的软件信息
        for key, item in self.infoBox[0].items():
            # item[2] == osbit(系统位数)
            # 如果等于2就是64位
            if item[2] == '2':
                item[0] += '64位'

            # 每个单元格放入相应项目
            name = QtWidgets.QTableWidgetItem(item[0])
            version = QtWidgets.QTableWidgetItem(item[1])
            fileSize = QtWidgets.QTableWidgetItem(str("%.2f" % (int(item[3]) / (1024 * 1024))) + "M")
            publishDate = QtWidgets.QTableWidgetItem(item[4])
            desc = QtWidgets.QTableWidgetItem(item[5])
            rank = QtWidgets.QTableWidgetItem(str(int(item[6]) / 10) + "分")
            self.downloadButton = QtWidgets.QPushButton()
            self.downloadButton.setText("下载")
            self.tableWidgets.setItem(key, 0, name)
            self.tableWidgets.setItem(key, 1, version)
            self.tableWidgets.setItem(key, 2, fileSize)
            self.tableWidgets.setItem(key, 3, publishDate)
            self.tableWidgets.setItem(key, 4, desc)
            self.tableWidgets.setItem(key, 5, rank)
            self.tableWidgets.setCellWidget(key, 6, self.downloadButton)
            self.downloadButton.clicked.connect(self.download)

        return self.infoBox[0]
    # 下载信号槽
    def download(self):
        MainWin.data = {}
        row = self.tableWidgets.currentRow()
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
        for i in MainWin.data.
