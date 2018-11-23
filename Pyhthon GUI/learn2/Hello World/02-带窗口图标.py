import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):  # 继承了QWidget
    def __init__(self):
        super().__init__()  # 初始化父类
        self.initUI()

    def initUI(self):
        """创建一个GUI"""
        '''
        setGeometry():把窗口放到屏幕上并且设置窗口大小
        setWindowTitle():设置窗口的标题
        setWindowIcon():添加图标
        '''
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('YilK')
        self.setWindowIcon(QIcon('a.jpg'))  # 创建一个QIcon对象，然后接受一个路径作为参数显示图标

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
