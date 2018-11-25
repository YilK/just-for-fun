# 组件能跨列跨行展示

import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建标签
        title = QLabel('Title')
        author = QLabel("Author")
        review = QLabel('Review')
        # 文字编辑
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        # 创建网格布局
        grid = QGridLayout()
        grid.setSpacing(10)  # 设置网格之间的间隔

        # 添加组件
        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)  # 占5行列

        self.setLayout(grid)

        self.setGeometry(300, 300, 400, 400)
        self.setWindowTitle('YilK')
        self.show()


if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
