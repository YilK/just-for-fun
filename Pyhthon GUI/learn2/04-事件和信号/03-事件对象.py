# 事件对象是用python来描述一系列的事件自身属性的对象
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建一个网格布局
        grid = QGridLayout()
        grid.setSpacing(10)  # 设置网格之间的间隔

        x = 0
        y = 0
        self.text = 'x:{},y:{}'.format(x, y)

        # 创建一个标签
        self.label = QLabel(self.text)

        # 添加组件
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True)#鼠标追踪默认没有开启，当有鼠标点击事件发生后才会开启。
        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('YilK')
        self.show()

    def mouseMoveEvent(self, e):
        """重写事件处理函数"""

        x=e.x()
        y=e.y()

        text='x:{},y:{}'.format(x, y)
        self.label.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
