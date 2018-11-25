import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout, QVBoxLayout


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建2个按钮
        okButton = QPushButton('ok')
        cancelButton = QPushButton('cancel')

        # 创建一个水平布局
        hbox = QHBoxLayout()
        hbox.addStretch(1)  # 增加弹性空间
        # 在水平布局中添加按钮
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        # 创建一个垂直布局
        vbox = QVBoxLayout()
        vbox.addStretch(1)  # 增加弹性空间
        vbox.addLayout(hbox)  # 将水平布局放到垂直布局盒里

        self.setLayout(vbox)

        self.setGeometry(300, 300, 400, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
