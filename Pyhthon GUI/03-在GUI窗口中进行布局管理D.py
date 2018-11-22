# 水平垂直布局
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, \
    QPushButton, QHBoxLayout, QVBoxLayout, QWidget


class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('hjk的第三个图形化界面')
        self.resize(400, 600)
        self.add_menu_and_statu()  # 添加菜单栏和文本状态栏
        self.horizontal_vertical_box_layout()  # 添加布局部件

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

    def horizontal_vertical_box_layout(self):
        """水平垂直布局"""
        # 两个标签
        label_1 = QLabel('第一个标签')
        label_2 = QLabel('第二个标签')

        # 两个按钮
        button_1 = QPushButton('第一个按钮')
        button_2 = QPushButton('第二个按钮')

        # 创建两个垂直盒子
        vbox_1 = QVBoxLayout()
        vbox_2 = QVBoxLayout()

        # 在垂直盒子1中添加标签1和标签2
        vbox_1.addWidget(label_1)
        vbox_1.addWidget(label_2)

        # 在水平盒子2中添加按钮1和按钮2
        vbox_2.addWidget(button_1)
        vbox_2.addWidget(button_2)

        # 创建一个水平盒子，包含两个垂直盒子
        hbox = QVBoxLayout()
        hbox.addLayout(vbox_1)
        hbox.addLayout(vbox_2)

        # 创建一个窗口部件，设置布局为水平盒子
        layout_widget = QWidget()
        layout_widget.setLayout(hbox)

        self.setCentralWidget(layout_widget)#中心窗口部件


if __name__ == '__main__':
    # 每个应用程序都必须实例化一个QApplication()
    app = QApplication(sys.argv)
    gui = Gui()
    gui.show()
    sys.exit(app.exec_())
