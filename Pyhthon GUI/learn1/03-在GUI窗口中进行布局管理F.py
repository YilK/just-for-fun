# 网格布局的一些变型
# 使用网格布局
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLabel, \
    QPushButton, QGridLayout, QWidget

from PyQt5.QtCore import Qt


class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('hjk的第三个图形化界面')
        self.resize(400, 600)
        self.add_menu_and_statu()  # 添加菜单栏和文本状态栏
        self.grid_layout()  # 添加布局部件

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

    def grid_layout(self):
        """网格布局"""
        # 两个标签
        label_1 = QLabel('第一个标签')
        label_2 = QLabel('第二个标签')

        # 两个按钮
        button_1 = QPushButton('第一个按钮')
        button_2 = QPushButton('第二个按钮')
        button_3 = QPushButton('第三个按钮')
        # 创建一个网格布局对象
        grid_layout = QGridLayout()

        # 在网格中添加窗口部件
        grid_layout.addWidget(label_1, 0, 0)  # 放在0行0列
        grid_layout.addWidget(label_2, 1, 0)  # 放在1行0列
        grid_layout.addWidget(button_1, 0, 1)
        grid_layout.addWidget(button_2, 1, 1)
        # 新建一个按钮，让其占1行和5列
        grid_layout.addWidget(button_3, 2, 0, 1, 5)  # 1代表占1行，5代表占5列

        # 指定表格的对齐方式
        grid_layout.setAlignment(Qt.AlignTop)  # 底部对齐
        grid_layout.setAlignment(label_1, Qt.AlignRight)  # 在label_1所在的单元格内是label_l右对齐
        # 创建一个窗口对象
        layout_widget = QWidget()

        # 设置窗口的布局
        layout_widget.setLayout(grid_layout)

        self.setCentralWidget(layout_widget)  # 中心窗口部件


if __name__ == '__main__':
    # 每个应用程序都必须实例化一个QApplication()
    app = QApplication(sys.argv)
    gui = Gui()
    gui.show()
    sys.exit(app.exec_())
