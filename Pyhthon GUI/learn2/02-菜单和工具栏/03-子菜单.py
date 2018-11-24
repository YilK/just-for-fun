# 子菜单是嵌套在菜单里面的二级或者三级等的菜单。

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QMenu, qApp
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """创建一个GUI"""

        # 基本设置
        self.setWindowIcon(QIcon('b.jpg'))
        self.setWindowTitle("YilK")
        self.setGeometry(300, 300, 400, 400)
        self.statusBar().showMessage('准备就绪')

        # 创建一个菜单栏
        menubar = self.menuBar()
        # 添加菜单
        fileMenu = menubar.addMenu('File')

        impMenu = QMenu('Import', self)  # 创建菜单
        impAct = QAction('Import mail', self)  # 创建一个动作
        impMenu.addAction(impAct)  # 将动作加入菜单

        newAct = QAction('New', self)  # 创建动作

        fileMenu.addAction(newAct)  # 添加动作
        fileMenu.addMenu(impMenu)  # 添加菜单

        # 退出动作
        exitAct = QAction(QIcon('exit.jpg'), 'EXIT', self)
        exitAct.setStatusTip("Exit application")  # 设置状态栏信息
        exitAct.setShortcut("Ctrl+Q")  # 设置快捷键
        exitAct.triggered.connect(qApp.quit)

        fileMenu.addAction(exitAct)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
