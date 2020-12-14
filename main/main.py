from func import Func
if __name__ == '__main__':
    print("软件查询（关键词）： ")
    id = Func(input())
    info = id.getInfo()
    for i in info.values():
        if i[2] == '2':
            i[0] += " 64位"
        print("名称: " + i[0])
        print("版本号: " + i[1])
        print("大小: " + str("%.2f" % (int(i[3])/(1024*1024))) + "M")
        print("发布日期: " + i[4])
        print("描述: " + i[5])
        print("评分: " + str(int(i[6]) / 10) + "分")
        print("下载地址: " + i[7])
    print("共找到{}款软件".format(int(id.total[0])))