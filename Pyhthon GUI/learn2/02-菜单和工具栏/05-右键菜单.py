# 右键弹出菜单

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, qApp, QMenu


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('YilK')
        self.show()

    def contextMenuEvent(self, event):
        """重写方法"""

        cmenu = QMenu(self)
        newAct = cmenu.addAction('New')
        opnAct = cmenu.addAction('Open')
        quitAct = cmenu.addAction('Quit')
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        '''
        使用exec_()方法显示菜单。
        从鼠标右键事件对象中获得当前坐标。
        mapToGlobal()方法把当前组件的相对坐标转换为窗口（window）的绝对坐标。
        '''
        if action == quitAct:
            qApp.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
