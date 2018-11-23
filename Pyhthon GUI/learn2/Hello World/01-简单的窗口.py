import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    '''
    实例化了一个应用程序对象QApplication()，
    在PyQt5中，每个应用程序都必须实例化一个QApplication()：
    sys.argv是一组命令行参数的列表
    '''
    app = QApplication(sys.argv)
    '''
    创建了一个QWidget()对象，它是pyqt5中所有的图形用户界面的基类:
    它提供了基本的应用构造器
    '''
    w = QWidget()
    w.resize(250, 150)  # 改变窗口的大小 宽250px，高150px
    w.move(300, 300)  # 改变窗口的位置
    w.setWindowTitle('YilK')  # 给窗口添加标题
    w.show()  # 将窗口显示出来
    '''
    最后，我们进入了应用的主循环中，事件处理器这个时候开始工作。
    主循环从窗口上接收事件，并把事件传入到派发到应用控件里。
    当调用exit()方法或直接销毁主控件时，主循环就会结束。
    sys.exit()方法能确保主循环安全退出。
    外部环境能通知主控件怎么结束。
    '''
    sys.exit(app.exec_())
