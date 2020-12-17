import requests

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
        print(data)


if __name__ == '__main__':
    QiHu('qq').getInfo()