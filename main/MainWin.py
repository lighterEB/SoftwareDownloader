# -*- coding: utf-8 -*-

# 主窗口及功能



from PyQt5 import QtCore, QtGui, QtWidgets
import func
import DownloadWin
import requests
import time

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
        MainWindow.setAutoFillBackground(True)
        self.tipLabel = QtWidgets.QLabel(MainWindow)
        self.tipLabel.setGeometry(QtCore.QRect(1000, 590, 141, 31))
        self.tipLabel.setText("")
        self.tipLabel.setStyleSheet("font-family:'黑体'; font-size: 14px")
        self.tipLabel.setObjectName("tipLabel")
        self.tableWidget = QtWidgets.QTableWidget(MainWindow)
        self.tableWidget.setGeometry(QtCore.QRect(20, 90, 1156, 490))
        self.tableWidget.setObjectName("tableWidget")
        # 建立7列
        self.tableWidget.setColumnCount(7)
        # 每列宽度
        self.tableWidget.setColumnWidth(0, 275)
        self.tableWidget.setColumnWidth(1, 120)
        self.tableWidget.setColumnWidth(2, 80)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 450)
        self.tableWidget.setColumnWidth(5, 50)
        self.tableWidget.setColumnWidth(6, 60)
        self.tableWidget.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)
        # 取消垂直表头
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setHorizontalHeaderLabels(['名称', '版本', '大小', '发布日期', '描述', '评分', ''])
        # 设置水平表头无法点击
        self.tableWidget.horizontalHeader().setSectionsClickable(False)
        # 设置水平表头无法拖动
        self.tableWidget.horizontalHeader().setDisabled(True)
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
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setStyleSheet("border: 3px solid black;font-size: 20px")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.searchButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setMinimumSize(QtCore.QSize(0, 0))
        self.searchButton.setIcon(QtGui.QIcon("./src/images/btn_search.png"))
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: white; font-size:16px")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setStyleSheet("color: blue")
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
    data = {}
    entryText = ''
    selectBox = ''
    txt = ''
    row = -1
    infoBox = {}
    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)

        # 绑定搜索按钮信号槽
        self.searchButton.clicked.connect(self.searchAppInfo)
        self.lineEdit.returnPressed.connect(self.searchAppInfo)
    # 查询软件相关信息功能返回字典
    def searchAppInfo(self):
        # 获取选择控件文字
        MainWin.selectBox = self.comboBox.currentText()
        # 获取输入搜索关键字
        MainWin.entryText = self.lineEdit.text()
        if MainWin.entryText == '':
            return
        else:
            self.tableWidget.clearContents()
            self.searchThread = SearchThread()
            self.searchThread.signalInfo.connect(self.flushTableWidget)
            self.searchThread.signalTotal.connect(self.flushTipLabel)
            self.searchThread._signalIsRunning.connect(lambda: self.searchButton.setEnabled(True))
            self.searchButton.setEnabled(False)
            self.searchThread.start()
    def flushTableWidget(self, lst):
        MainWin.row += 1
        # 建立下载按钮控件
        k = []
        v = []
        for key, value in lst.items():
            k.append(key)
            v.append(value)
        if MainWin.row <= int(MainWin.txt):
            self.downloadButton = QtWidgets.QPushButton()
            # 设置下载按钮图片
            self.downloadButton.setIcon(QtGui.QIcon("./src/images/download.png"))
            self.downloadButton.setStyleSheet("background-color: #5A9BB3")

            # 创建窗口对象
            self.headWidget = QtWidgets.QWidget()
            # 创建图像标签对象
            self.imgLabel = QtWidgets.QLabel()
            # 将解析的logo片放入图像标签
            try:
                self.imgLabel.setScaledContents(True)
                self.imgLabel.setPixmap(v[6])
                # 创建文字标签
                self.textLabel = QtWidgets.QLabel()
                # 设置应用名称到文字标签
                self.textLabel.setText(k[0])
                # 创建水平布局，讲窗口对象放进此布局
                self.hLayout = QtWidgets.QHBoxLayout(self.headWidget)
                # 将图像标签放入窗口对象所在布局并设置居中
                self.hLayout.addWidget(self.imgLabel, 0, QtCore.Qt.AlignCenter)
                # 将文字标签放入窗口对象所在布局
                self.hLayout.addWidget(self.textLabel)
                # 将窗口对象添加到每行第一个单元格
                self.tableWidget.setCellWidget(MainWin.row, 0, self.headWidget)
                # 设置单元格高度
                self.tableWidget.setRowHeight(MainWin.row, 68)
                # 放置项目到对应单元格
                self.tableWidget.setItem(MainWin.row, 0, v[0])
                self.tableWidget.setItem(MainWin.row, 1, v[1])
                self.tableWidget.setItem(MainWin.row, 2, v[2])
                self.tableWidget.setItem(MainWin.row, 3, v[3])
                self.tableWidget.setItem(MainWin.row, 4, v[4])
                self.tableWidget.setItem(MainWin.row, 5, v[5])
                self.tableWidget.setCellWidget(MainWin.row, 6, self.downloadButton)
                # 给下载按钮建立信号槽
                self.downloadButton.clicked.connect(self.download)
            except:
                self.tableWidget.hideRow(MainWin.row)


    def flushTipLabel(self, txt):
        self.tableWidget.setRowCount(int(txt))
        self.tipLabel.setStyleSheet("color:white; font-size: 14px")
        self.tipLabel.setText("共找到{}款相关软件".format(txt))
        MainWin.txt = int(txt)


    # 下载信号槽
    def download(self):
        MainWin.data = {}
        rowLine = self.tableWidget.currentRow()
        if MainWin.selectBox == '腾讯':
            fileName = QtWidgets.QFileDialog.getSaveFileName(self, "", MainWin.infoBox[0][rowLine][8])
            MainWin.data['fileDir'] = fileName
            MainWin.data['url'] = MainWin.infoBox[0][rowLine][7]
        else:
            import re
            fileName = MainWin.infoBox[0][rowLine]['soft_download']
            fileName = re.findall(re.compile(r'/(.*?).exe'), fileName)
            fileName = QtWidgets.QFileDialog.getSaveFileName(self, "", fileName[0] + '.exe')
            MainWin.data['url'] = MainWin.infoBox[0][rowLine]['soft_download']
            MainWin.data['fileDir'] = fileName
        if fileName[0] != '':
            self.downloadWin = DownloadWin.Form()
            self.downloadWin.setWindowModality(QtCore.Qt.ApplicationModal)
            self.downloadWin.setWindowTitle("下载")
            self.downloadWin.dirPath.setText(fileName[0])
            self.downloadWin.dirPath.setReadOnly(True)
            self.downloadWin.pushButton.clicked.connect(self.openFile)
            self.downloadWin.mySignal.connect(self.terminate)
            self.downloadThread = DownloadThread()
            self.downloadThread.signal.connect(self.flushValue)
            self.downloadThread.start()
            self.downloadWin.show()
    # 中断下载
    def terminate(self):
        self.downloadThread.terminate()
    # 刷新下载进度条
    def flushValue(self, value):
        self.downloadWin.progressBar.setValue(round(value + 1))
        if round(value + 1) == 100:
            self.downloadWin.pushButton.setText("打开文件")
            self.downloadWin.pushButton.setDisabled(False)
    def openFile(self):
        import subprocess
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        item = str(MainWin.data['fileDir'][0])
        subprocess.Popen(item, shell=True, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, startupinfo=si)
        self.downloadThread.terminate()



# 下载线程类
class DownloadThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(float)
    def run(self):
        res = requests.get(MainWin.data['url'], stream=True)
        chunk_size = 1024
        fileSize = res.headers['Content-Length']
        chunk_temp = 0
        with open(MainWin.data['fileDir'][0], 'wb') as f:
            for chunk in res.iter_content(chunk_size=chunk_size):
                if chunk:
                    toDo = "%.5f" % (chunk_temp / float(fileSize)*100)
                    f.write(chunk)
                chunk_temp += chunk_size
                self.signal.emit(float(toDo))
        f.close()
        time.sleep(1)

        

class SearchThread(QtCore.QThread):
    signalTotal = QtCore.pyqtSignal(str)
    signalInfo = QtCore.pyqtSignal(dict)
    _signalIsRunning = QtCore.pyqtSignal()



    def run(self):
        if MainWin.selectBox == "腾讯":
            # 得到处理后的信息字典
            MainWin.infoBox = func.Tencent(MainWin.entryText).getInfo()

            # 创建表格控件中的行数
            # infoBox[1][0] = 查询到的软件总数
            self.signalTotal.emit(MainWin.infoBox[1][0])
            # 遍历查询到的软件信息
            for key, item in MainWin.infoBox[0].items():
                info = {}
                # item[2] == osbit(系统位数)
                # 如果等于2就是64位
                if item[2] == '2':
                    item[0] += '64位'

                # 设置单元格项目并且全部不可点击
                name = QtWidgets.QTableWidgetItem()
                name.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[0]] = name
                version = QtWidgets.QTableWidgetItem(item[1])
                version.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[1]] = version
                fileSize = QtWidgets.QTableWidgetItem(str("%.2f" % (int(item[3]) / (1024 * 1024))) + "M")
                fileSize.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[3]] = fileSize
                publishDate = QtWidgets.QTableWidgetItem(item[4])
                publishDate.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[4]] = publishDate
                desc = QtWidgets.QTableWidgetItem(item[5])
                desc.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[5]] = desc
                rank = QtWidgets.QTableWidgetItem(str(int(item[6]) / 10) + "分")
                rank.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[item[6]] = rank
                photo = QtGui.QPixmap()
                photo.loadFromData(requests.get("http://pc3.gtimg.com/softmgr/logo/48/{}".format(item[9].lower())).content)
                info['img'] = photo
                dUrl = item[7]
                info['url'] = dUrl
                self.signalInfo.emit(info)
            time.sleep(1)
            MainWin.row = -1
            self._signalIsRunning.emit()
        if MainWin.selectBox == "360":
            # 得到处理后的信息字典
            MainWin.infoBox = func.QiHu(MainWin.entryText).getInfo()
            self.signalTotal.emit(str(MainWin.infoBox[1]))
            for value in MainWin.infoBox[0].values():
                info = {}
                # 设置单元格项目并且全部不可点击
                name = QtWidgets.QTableWidgetItem()
                name.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[value['softname']] = name
                version = QtWidgets.QTableWidgetItem(value['version'])
                version.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[value['version']] = version
                fileSize = QtWidgets.QTableWidgetItem(value['size'])
                fileSize.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[value['size']] = fileSize
                publishDate = QtWidgets.QTableWidgetItem(value['date'])
                publishDate.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[value['date']] = publishDate
                desc = QtWidgets.QTableWidgetItem(value['desc'])
                desc.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[value['desc']] = desc
                rank = QtWidgets.QTableWidgetItem(str(value['poll']) + "分")
                rank.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
                info[value['poll']] = rank
                if 'https:' not in value['logo']:
                    logUrl = 'https:' + value['logo']
                else:
                    logUrl = value['logo']
                imgData = requests.get(logUrl).content
                photo = QtGui.QPixmap()
                photo.loadFromData(imgData)
                photo.scaled(32, 32, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                info['img'] = photo
                dUrl = value['soft_download']
                info['url'] = dUrl
                self.signalInfo.emit(info)
            time.sleep(1)
            MainWin.row = -1
            self._signalIsRunning.emit()