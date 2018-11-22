import sys
from PyQt5.QtWidgets import *

'''
实例化了一个应用程序对象QApplication()，
在PyQt5中，每个应用程序都必须实例化一个QApplication()：
'''
app = QApplication(sys.argv)
'''
创建了一个QWidget()对象，它是pyqt5中所有的图形用户界面的基类:
'''
win = QWidget()
win.resize(450, 150)  # 将窗口的大小设置为450*150
win.move(0, 300)  # 将窗口移动到显示器x=0，y=300的位置
win.setWindowTitle('hjk的第一个图形化界面')
win.show()  # 使用QWidget对象的show()方法将创建的窗口显示出来
sys.exit(app.exec_())
