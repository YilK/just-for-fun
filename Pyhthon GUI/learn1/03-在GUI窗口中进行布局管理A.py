import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, \
    QPushButton


class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('hjk的第三个图形化界面')
        self.resize(400, 600)
        self.add_menu_and_statu()  # 添加菜单栏和文本状态栏
        self.add_position_layout()  # 添加布局部件

    def add_menu_and_statu(self):
        """添加菜单栏和状态栏"""
        # 添加文本状态栏
        self.statusBar().showMessage('文本状态栏')

        # 创建一个菜单栏
        menu = self.menuBar()
        # 创建两个菜单
        file_menu = menu.addMenu('文件')
        file_menu.addSeparator()
        edit_menu = menu.addMenu('修改')
        # 创建一个行为
        new_action = QAction('新文件', self)
        # 添加一个行为到菜单
        file_menu.addAction(new_action)
        # 更新状态文本栏
        new_action.setStatusTip('打开新的文件')

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

    def add_position_layout(self):
        """添加布局部件"""

        # 获取菜单栏的高度
        mabar_height = self.menuBar().height()
        print(mabar_height)
        # 第一个标签
        label_1 = QLabel('第一个标签', self)
        label_1.move(10, mabar_height)
        # 第二个标签
        label_2 = QLabel('第二个标签', self)
        label_2.move(10, mabar_height * 2)

        # 第一个按钮
        button_1 = QPushButton('按钮1', self)
        button_1.move(label_1.width(), mabar_height)  # 按钮的位置
        # 第二个按钮
        button_2 = QPushButton('按钮2', self)
        button_2.move(label_2.width(), mabar_height * 2)


if __name__ == '__main__':
    # 每个应用程序都必须实例化一个QApplication()
    app = QApplication(sys.argv)
    gui = Gui()
    gui.show()
    sys.exit(app.exec_())
