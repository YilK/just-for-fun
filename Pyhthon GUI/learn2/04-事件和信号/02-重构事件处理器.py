# 在PyQt5中，事件处理器经常被重写（也就是用自己的覆盖库自带的）

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('YilK')
        self.show()

    def keyPressEvent(self, e):
        """替换了事件处理器函数keyPressEvent()"""

        if e.key() == Qt.Key_Escape:  # 如果按下Esc键
            self.close()  # 程序退出


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
