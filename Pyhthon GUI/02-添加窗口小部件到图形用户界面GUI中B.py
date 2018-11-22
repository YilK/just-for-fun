import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction


class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('hjk的第三个图形化界面')
        self.resize(400, 100)

        # 设置状态消息栏文本
        self.statusBar().showMessage('文本状态栏')

        # 创建一个菜单栏
        menu = self.menuBar()
        # 创建菜单
        file_menu = menu.addMenu('文件')
        # 创建一个行为
        new_action = QAction('新文件', self)
        # 添加一个行为到菜单
        file_menu.addAction(new_action)
        # 更新状态文本栏
        new_action.setStatusTip('新的文件')

        # 创建退出行为
        exit_action = QAction('退出', self)
        # 退出操作，在状态栏会显示这个消息
        exit_action.setStatusTip('点击退出应用程序')
        # 点击关闭程序
        exit_action.triggered.connect(self.close)
        # 设置退出快捷键
        exit_action.setShortcut('Ctrl+Q')
        # 添加退出行为到菜单上
        file_menu.addAction(exit_action)


if __name__ == '__main__':
    # 每个应用程序都必须实例化一个QApplication()
    app = QApplication(sys.argv)
    gui = Gui()
    gui.show()
    sys.exit(app.exec_())
