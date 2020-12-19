import MainWin
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QIcon
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWin.MainWin()
    pelette = QPalette()
    pelette.setBrush(QPalette.Background, QBrush(QPixmap("./src/images/bkg.jpg")))
    mainWin.setPalette(pelette)
    mainWin.setWindowIcon(QIcon(QPixmap("./src/images/ico.png")))
    mainWin.show()
    sys.exit(app.exec_())