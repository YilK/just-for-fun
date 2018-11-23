import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon


class Example(QWidget):
    def __init__(self):
        super().__init__()  # 初始化父类

        self.initUI()

    def initUI(self):
        """创建一个GUI"""

        # 创建一个退出按钮
        qbtn = QPushButton('Quit', self)  # 第二个参数是按钮的父级组件
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        '''
        点击按钮之后，信号会被捕捉并给出既定的反应。
        QCoreApplication包含了事件的主循环，它能添加和删除所有的事件，
        instance()创建了一个它的实例。QCoreApplication是在QApplication里创建的。 
        点击事件和能终止进程并退出应用的quit函数绑定在了一起。
        在发送者和接受者之间建立了通讯，发送者就是按钮，接受者就是应用对象。
        '''
        qbtn.resize(qbtn.sizeHint())  # 设置按钮的大小，resize()方法必须要提供参数
        qbtn.move(50, 50)  # 移动按钮

        # 设置图标
        self.setWindowIcon(QIcon('a.jpg'))

        self.setGeometry(300, 300, 250, 150)  # 设置窗口的位置及大小
        self.setWindowTitle('YilK')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
