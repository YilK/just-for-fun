# 网格布局。
# 这种布局是把窗口分为行和列。创建和使用栅格布局，需要使用QGridLayout模块。


import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QGridLayout


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个网格布局
        grid = QGridLayout()
        grid.setSpacing(2)#设置每个网格之间的间隔
        self.setLayout(grid)


        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+'
                 ]

        positions = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(positions, names):
            if name == '':
                continue
            print(*position)

            button = QPushButton(name)
            grid.addWidget(button, *position)
        self.setWindowTitle('YilK')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
