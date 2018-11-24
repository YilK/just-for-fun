'''
主窗口
QMainWindow提供了主窗口的功能，使用它能创建一些简单的状态栏、工具栏和菜单栏。
'''

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon


class Eample(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')
        '''
        QMainWindow类的statuBar() 创建状态栏
        showMessage() 在状态栏上显示信息
        '''
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("YilK")

        # 创建一个退出按钮
        qbtn = QPushButton('Quit', self)
        qbtn.setToolTip('退出')  # 创建提示框
        qbtn.clicked.connect(QCoreApplication.instance().quit)  # 点击后退出

        # 创建图标
        self.setWindowIcon(QIcon('a.jpg'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Eample()
    sys.exit(app.exec())
