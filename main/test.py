import requests

res = requests.get('https://dl.softmgr.qq.com/original/im/QQ9.4.1.27572.exe', stream=True)
fileSize = res.headers['Content-Length']
chunk_size = 1024
chunk_t = 0
txt = '■'
with open("E:\Projects\pythonProject\SoftwareDownloader\QQ9.4.1.27572.exe", "wb") as f:
    for chunk in res.iter_content(chunk_size=chunk_size):

        jindu = "%.2f"%((chunk_t/float(fileSize)*100))
        print("已下载{}{}".format(txt*round(float(jindu)), jindu))
        chunk_t += chunk_size
