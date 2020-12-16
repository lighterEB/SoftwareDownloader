import requests
import re

class Tencent:
    def __init__(self, name):
        self.url = 'https://s.pcmgr.qq.com/tapi/web/searchcgi.php?type=search&callback=searchCallback&keyword=%s&page=1&pernum=30&more=0' % name
    # 获取信息
    def getInfo(self):
        res = requests.get(self.url)
        info = res.content.decode(encoding='utf-8')
        info = re.sub(r'\\', '', eval("'{}'".format(info)))
        print(info)
        # 总共找到的软件数量
        self.total = re.findall(re.compile(r'"total":(\d+)'), info)
        # 应用名
        dname = re.findall(re.compile(r'"SoftName":"(.*?)",'), info)
        # 软件版本
        version = re.findall(re.compile(r'versionname>(.*?)<'), info)
        # 系统位数
        osbit = re.findall(re.compile(r'osbit="(\d)"'), info)
        # 软件大小
        filesize = re.findall(re.compile(r'filesize>(.*?)<'), info)
        # 发布时间
        publishdate = re.findall(re.compile(r'publishdate>(.*?)<'), info)
        # 软件描述
        feature_old = re.findall(re.compile(r'feature>.*\n.*CDATA\[(.*)]]>'), info)
        feature_new = []
        for i in range(len(feature_old)):
            if i % 2 != 0:
                feature_new.append(feature_old[i])
        # 文件名
        filename = re.findall(re.compile(r'filename>(.*?)<'), info)
        # 软件评分
        point = re.findall(re.compile(r'point>(.*?)<'), info)
        # 下载地址
        durl = re.findall(re.compile(r'(http://.*)]]>'), info)
        # 图片
        logo = re.findall(re.compile(r'logo32>(.*?)<'), info)
        self.data = {}
        if self.total is not None:
            for j in range(int(self.total[0])):
                box = []
                for i in dname, version, osbit, filesize, publishdate, feature_new, point, durl, filename, logo:
                    box.append(i[j])
                self.data[j] = box

        return self.data, self.total

if __name__ == '__main__':
    a = Tencent('哔哩哔哩')
    print(a.getInfo())

    # # 得到处理后的信息字典
    # self.infoBox = func.Tencent(entryText).getInfo()
    #
    # # 创建表格控件中的行数
    # # infoBox[1][0] = 查询到的软件总数
    # self.tableWidget.setRowCount(int(self.infoBox[1][0]))
    #
    # # 遍历查询到的软件信息
    # for key, item in self.infoBox[0].items():
    #     # item[2] == osbit(系统位数)
    #     # 如果等于2就是64位
    #     if item[2] == '2':
    #         item[0] += '64位'
    #
    #     # 设置单元格项目并且全部不可点击
    #     name = QtWidgets.QTableWidgetItem()
    #     name.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
    #     version = QtWidgets.QTableWidgetItem(item[1])
    #     version.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
    #     fileSize = QtWidgets.QTableWidgetItem(str("%.2f" % (int(item[3]) / (1024 * 1024))) + "M")
    #     fileSize.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
    #     publishDate = QtWidgets.QTableWidgetItem(item[4])
    #     publishDate.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
    #     desc = QtWidgets.QTableWidgetItem(item[5])
    #     desc.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
    #     rank = QtWidgets.QTableWidgetItem(str(int(item[6]) / 10) + "分")
    #     rank.setFlags(QtCore.Qt.ItemFlags(int("000000", 2)))
    #     # 图标文件名
    #     logo = item[9]
    #     logo = logo.lower()
    #     # 建立下载按钮控件
    #     self.downloadButton = QtWidgets.QPushButton()
    #     # 设置下载按钮图片
    #     self.downloadButton.setIcon(QtGui.QIcon("../src/images/download.png"))
    #     # 解析应用logo图片
    #     photo = QtGui.QPixmap()
    #     photo.loadFromData(requests.get("http://pc3.gtimg.com/softmgr/logo/48/{}".format(logo)).content)
    # 创建窗口对象
    self.headWidget = QtWidgets.QWidget()
    # 创建图像标签对象
    self.imgLabel = QtWidgets.QLabel()
    # 将解析的logo片放入图像标签
    self.imgLabel.setPixmap(photo)
    # 创建文字标签
    self.textLabel = QtWidgets.QLabel()
    # 设置应用名称到文字标签
    self.textLabel.setText(item[0])
    # 创建水平布局，讲窗口对象放进此布局
    self.hLayout = QtWidgets.QHBoxLayout(self.headWidget)
    # 将图像标签放入窗口对象所在布局并设置居中
    self.hLayout.addWidget(self.imgLabel, 0, QtCore.Qt.AlignCenter)
    # 将文字标签放入窗口对象所在布局
    self.hLayout.addWidget(self.textLabel)
    # 将窗口对象添加到每行第一个单元格
    self.tableWidget.setCellWidget(key, 0, self.headWidget)
    # 设置单元格高度
    self.tableWidget.setRowHeight(key, 68)
    # 放置项目到对应单元格
    self.tableWidget.setItem(key, 0, name)
    self.tableWidget.setItem(key, 1, version)
    self.tableWidget.setItem(key, 2, fileSize)
    self.tableWidget.setItem(key, 3, publishDate)
    self.tableWidget.setItem(key, 4, desc)
    self.tableWidget.setItem(key, 5, rank)
    self.tableWidget.setCellWidget(key, 6, self.downloadButton)

    # 给下载按钮建立信号槽
    self.downloadButton.clicked.connect(self.download)
self.tipLabel.setText("共找到{}款相关软件".format(self.infoBox[1][0]))
return self.infoBox[0]