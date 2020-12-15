import MainWin
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWin.MainWin()
    mainWin.show()
    sys.exit(app.exec_())