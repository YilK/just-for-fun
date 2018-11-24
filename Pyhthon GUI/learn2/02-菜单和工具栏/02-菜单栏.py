import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """创建一个GUI"""
        exitAct = QAction(QIcon('exit.jpg'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        '''
        QAction 是菜单栏、工具栏或者快捷键的动作的组合。
        第一行创建一个图标，一个exit的标签
        第二行创建了一个快捷键组合
        第三行创建了一个状态栏，当鼠标悬停在菜单栏的时候能显示出当前的状态
        第四行 当执行这个指定的动作时，就触发了一个事件。这个事件跟QApplication的quit()行为相关联，
        所以这个动作就能终止这个应用。
        '''
        # 创建状态栏，并显示信息
        self.statusBar().showMessage('准备就绪')

        menubar = self.menuBar()  # 创建一个菜单栏
        fileMenu = menubar.addMenu('&File')  # 在菜单栏里再添加一个File菜单
        fileMenu.addAction(exitAct)  # 再File菜单中添加创建的QAction对象

        #添加窗口图标
        self.setWindowIcon(QIcon('b.jpg'))

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('YilK')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
