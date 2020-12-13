# -*- coding: utf-8 -*-

"""第一个程序"""

from PyQt5 import QtWidgets # 导入PyQt5部件

import sys

app = QtWidgets.QApplication(sys.argv) # 建立application对象

first_window = QtWidgets.QWidget() # 建立窗体对象

first_window.resize(400, 300) # 设置窗体大小

first_window.setWindowTitle("我的第一个pyqt程序") # 设置窗体标题

first_window.show() # 显示窗体

sys.exit(app.exec()) # 运行程序