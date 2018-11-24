import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont,QIcon


class Example(QWidget):  # 继承QWidget

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        """创建一个GUI"""

        # 静态方法设置提示框的字体
        QToolTip.setFont(QFont('SansSerif', 10))

        # 创建提示框，使用富文本格式的内容
        self.setToolTip('This is a <b>QWidget</b> widget')

        # 创建一个按钮，并为其创建一个提示框
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        # 设置按钮的大小，sizeHint() 方法提供了一个默认的按钮大小
        btn.resize(btn.sizeHint())
        # 设置按钮的位置
        btn.move(50, 50)

        #设置图标
        self.setWindowIcon(QIcon('a.jpg'))


        self.setGeometry(300, 300, 300, 200)  # 窗口的位置及大小
        self.setWindowTitle('YilK')
        self.show()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())