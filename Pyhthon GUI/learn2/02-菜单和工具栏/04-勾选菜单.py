import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, qApp
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 基本设置
        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('YilK')
        self.setWindowIcon(QIcon('b.jpg'))
        self.statusBar().showMessage('准备就绪')

        # 创建菜单栏
        menubar = self.menuBar()
        # 添加菜单栏内容
        fileMenu = menubar.addMenu('File')

        impMenu = QMenu('Import', self)
        impAct = QAction('Import file', self)

        impMenu.addAction(impAct)

        fileMenu.addMenu(impMenu)

        # 添加退出动作
        exitAct = QAction(QIcon('exit.jpg'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('退出请求')
        exitAct.triggered.connect(qApp.quit)
        fileMenu.addAction(exitAct)

        # t添加View菜单
        viewMenu = menubar.addMenu('View')

        viewStatAct = QAction("View statusbar", self, checkable=True)  # checkable 创建一个能选中的菜单
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)  # 默认为选中
        viewStatAct.triggered.connect(self.toggleMenu)
        viewMenu.addAction(viewStatAct)
        self.show()

    def toggleMenu(self, state):
        if state:
            self.statusBar.show()
        else:
            self.statusBar.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
