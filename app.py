import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFrame
from PyQt5.QtGui import QIcon


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Image Compressor by Qaswar02'
        self.left = 10
        self.top = 10
        self.width = 600
        self.height = 900
        self.setObjectName("mainwindow")
        with open("design.qss", "r") as f:
            stylesheet = f.read()
        self.setStyleSheet(stylesheet)
        self.initUI()
        self.setFixedSize(self.width, self.height)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # Main Window Start
        self.single_border = QFrame(self)
        self.single_border.setObjectName("border")
        self.single_border.move(47,150)

        self.dir_border = QFrame(self)
        self.dir_border.setObjectName("border")
        self.dir_border.move(47, 475)
        # Main Window End

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())