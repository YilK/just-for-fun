import sys
from PyQt5.QtWidgets import QApplication, QWidget


class GUi(QWidget):

    def __init__(self):
        """初始化"""
        #实例化super类,用来创建窗口
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('hjk的第二个图形化界面')

if __name__ == '__main__':
    #每个应用程序都必须实例化一个QApplication()
    app=QApplication(sys.argv)
    gui=GUi()#创建实例
    gui.show()
    sys.exit(app.exec_())
