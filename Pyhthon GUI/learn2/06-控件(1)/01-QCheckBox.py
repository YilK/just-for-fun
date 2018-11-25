#QCheckBox组件有俩状态：开和关。通常跟标签一起使用，用在激活和关闭一些选项的场景。


from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        #创建一个单选框
        cb=QCheckBox('Show title',self)
        cb.move(20,20)
        cb.toggle()#使单选框选中
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.show()

    def changeTitle(self,state):

        if state==Qt.Checked:
            self.setWindowTitle('111')
        else:
            self.setWindowTitle('')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


