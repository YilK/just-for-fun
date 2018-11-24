import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication, QPushButton, \
    QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        """创建一个GUI"""

        # 设置窗口的大小
        self.resize(400, 400)
        self.center()  # 移动窗口

        # 窗口图标
        self.setWindowIcon(QIcon('a.jpg'))
        # 窗口标题
        self.setWindowTitle('YilK')

        # 创建一个退出按钮
        qbtn = QPushButton('Quit', self)
        qbtn.setToolTip('退出')  # 设置提示框
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        print(qbtn.sizeHint())
        qbtn.move(400 - 93, 400 - 28)  # 移动退出按钮

        # 显示窗口
        self.show()

    def closeEvent(self, event):
        """替换默认的事件处理"""
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        """窗口居中"""
        qr = self.frameGeometry()  # 得到主窗口的大小（副本）
        print(qr)
        # 获取屏幕的分辨率，然后得到中心点的位置
        cp = QDesktopWidget().availableGeometry().center()
        print(cp)
        # 把副本窗口中心点的位置放到屏幕的中心点
        qr.moveCenter(cp)
        self.move(qr.topLeft())  # 把窗口的坐上角的坐标设置为qr的矩形左上角的坐标

        # 如果本来的窗口有moveCenter(),那就好了


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
