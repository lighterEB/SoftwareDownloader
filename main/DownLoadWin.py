# -*- coding: utf-8 -*-

#


from PyQt5 import QtCore, QtGui, QtWidgets


# 下载窗口
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(360, 126)
        Form.setMinimumSize(QtCore.QSize(360, 126))
        Form.setMaximumSize(QtCore.QSize(360, 126))
        Form.setWindowIcon(QtGui.QIcon(QtGui.QPixmap("./src/images/ico.png")))
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 100, 75, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setDisabled(True)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 10, 341, 83))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.widget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.dirPath = QtWidgets.QLineEdit(self.widget)
        self.dirPath.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.dirPath)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "正在下载"))
        self.label.setText(_translate("Form", "文件存放路径："))


# 驱动下载窗口
class Form(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(Form, self).__init__()
        self.setupUi(self)

    mySignal = QtCore.pyqtSignal(str)

    def sendEditContent(self):
        content = "1"
        self.mySignal.emit(content)

    # 重写关闭事件
    def closeEvent(self, envent):
        self.sendEditContent()
