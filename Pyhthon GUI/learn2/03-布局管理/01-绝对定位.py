import sys
from PyQt5.QtWidgets import QWidget,QLabel,QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        lb1=QLabel('zetcode',self)
        lb1.move(15,10)

        lb2=QLabel('hjkcode',self)
        lb2.move(30,55)

        self.setWindowTitle('YilK')
        self.setGeometry(200,200,300,300)
        
        self.show()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())

