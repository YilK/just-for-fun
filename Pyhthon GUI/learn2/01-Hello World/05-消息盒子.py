'''
默认情况下，我们点击标题栏的×按钮，QWidget就会关闭。但是有时候，我们修改默认行为。
比如，如果我们打开的是一个文本编辑器，并且做了一些修改，我们就会想在关闭按钮的时候让用
户进一步确认操作。
'''

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication,QPushButton
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        """创建一个GUI"""

        # 设置窗口的位置及大小
        self.setGeometry(300, 300, 250, 150)
        # 设置窗口的标题
        self.setWindowTitle('YilK')
        # 设置窗口的图标
        self.setWindowIcon(QIcon('a.jpg'))


        #添加一个退出按钮
        btn=QPushButton('Quit',self)
        btn.move(152,120)#移动按钮
        btn.setToolTip('退出')
        btn.clicked.connect(QCoreApplication.instance().quit)

        # 显示窗口
        self.show()

    def closeEvent(self, event):
        """替换默认的事件处理"""
        '''
        如果关闭QWidget，就会产生一个QCloseEvent。
        改变控件的默认行为，就是替换掉默认的事件处理。
        '''
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        '''
        创建了一个消息框，上面有两个按钮：YES,NO
        第一个字符串：消息框的标题栏
        第二个字符串：显示在对话框的内容
        第三个参数：消息框的按钮
        最后一个参数：默认选中的按钮
        '''
        # 判断返回值
        if reply == QMessageBox.Yes:  # 如果是YES，关闭组件和应用
            event.accept()
        else:  # 忽略关闭组件和应用
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
