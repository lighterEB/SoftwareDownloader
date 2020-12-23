import requests
import re

# 腾讯软件库
class Tencent:
    def __init__(self, name):
        self.url = 'https://s.pcmgr.qq.com/tapi/web/searchcgi.php?type=search&callback=searchCallback&keyword=%s&page=1&pernum=30&more=0' % name
    # 获取信息
    def getInfo(self):
        res = requests.get(self.url)
        info = res.content.decode(encoding='utf-8')
        info = re.sub(r'\\', '', eval("'{}'".format(info)))
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
        dUrl_old = (re.findall(re.compile(r'(http[s]?://.*)]]'), info))
        dUrl = []
        for i in range(len(dUrl_old)):
            if len(dUrl) == 0:
                dUrl.append(dUrl_old[i])
            elif dUrl_old[i].split('/')[-1] != dUrl[-1].split('/')[-1]:
                dUrl.append(dUrl_old[i])
        # 图片
        logo = re.findall(re.compile(r'logo48>(.*?)<'), info)
        self.data = {}
        if self.total is not None:
            for j in range(int(self.total[0])):
                box = []
                for i in dname, version, osbit, filesize, publishdate, feature_new, point, dUrl, filename, logo:
                    box.append(i[j])
                    self.data[j] = box
        return self.data, self.total

# 360软件库
class QiHu:
    def __init__(self, name):
        self.url = "http://bapi.safe.360.cn/soft/search?keyword={}&page=1".format(name)

    # 获取信息
    def getInfo(self):
        res = requests.get(self.url)
        lst = res.json()['data']['list']
        total = res.json()['data']['total']
        data = {}
        for i in range(len(lst)):
            data[i] = lst[i]

        return data, total