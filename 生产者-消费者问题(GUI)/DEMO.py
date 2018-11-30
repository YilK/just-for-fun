# ProducterAndConsumer
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, \
    QGridLayout
from PyQt5.QtGui import QFont, QIcon


class Example(QWidget):

    def __init__(self):
        """初始化"""
        super().__init__()  # 初始化父类

        self.initUI()

    def word_style(self):
        """定义文字格式"""
        '''其实修不修改都无所谓，我只是为更加美观'''

        font1 = QFont()
        font1.setFamily('consolas')  # 字体的类型
        font1.setBold(True)  # 将文字加粗
        font1.setPointSize(14)  # 字体的大小

        font2 = QFont()
        font2.setFamily('consolas')
        font2.setPointSize(12)

        font3 = QFont()
        font3.setFamily('consolas')
        font3.setPointSize(12)
        return font1, font2, font3

    def initUI(self):
        """创建一个GUI"""

        """创建组件"""

        # 定义文字的样式
        self.font1, self.font2, self.font3 = self.word_style()

        # 标签
        self.label1 = QLabel('阻塞队列')
        self.label1.setStyleSheet('color:red')
        self.label1.setFont(self.font1)  # 设置格式
        self.label2 = QLabel('仓库')
        self.label2.setStyleSheet('color:red')
        self.label2.setFont(self.font1)

        # 文本
        self.lineEdit1 = QLineEdit()
        self.lineEdit2 = QLineEdit()
        self.lineEdit3 = QLineEdit()
        self.lineEdit4 = QLineEdit()
        self.lineEdit5 = QLineEdit()
        self.lineEdit6 = QLineEdit()

        self.wavehouse = [self.lineEdit1, self.lineEdit2, self.lineEdit3]  # 仓库空间
        self.Block_queue = [self.lineEdit4, self.lineEdit5, self.lineEdit6]  # 阻塞队列

        # 按钮
        self.proButton1 = QPushButton('生产者1')
        self.proButton2 = QPushButton('生产者2')
        self.proButton3 = QPushButton('生产者3')

        self.cumButton1 = QPushButton('消费者1')
        self.cumButton2 = QPushButton('消费者2')
        self.cumButton3 = QPushButton('消费者3')

        # 设置按钮上的字体
        self.proButton1.setFont(self.font2)
        self.proButton2.setFont(self.font2)
        self.proButton3.setFont(self.font2)
        self.cumButton1.setFont(self.font2)
        self.cumButton2.setFont(self.font2)
        self.cumButton3.setFont(self.font2)

        # 使用网格布局
        grid = QGridLayout()
        grid.setSpacing(10)

        '''添加组件'''
        grid.addWidget(self.label2, 0, 0)
        grid.addWidget(self.label1, 1, 0)

        # 仓库行文本
        grid.addWidget(self.lineEdit1, 0, 1)
        grid.addWidget(self.lineEdit2, 0, 2)
        grid.addWidget(self.lineEdit3, 0, 3)

        # 阻塞队列 行文本
        grid.addWidget(self.lineEdit4, 1, 1)
        grid.addWidget(self.lineEdit5, 1, 2)
        grid.addWidget(self.lineEdit6, 1, 3)

        # 生产者按钮
        grid.addWidget(self.proButton1, 2, 1)
        grid.addWidget(self.proButton2, 2, 2)
        grid.addWidget(self.proButton3, 2, 3)

        # 消费者按钮
        grid.addWidget(self.cumButton1, 3, 1)
        grid.addWidget(self.cumButton2, 3, 2)
        grid.addWidget(self.cumButton3, 3, 3)
        self.setLayout(grid)

        '''添加事件'''

        # 生产者
        self.proButton1.clicked.connect(self.pressP)
        self.proButton2.clicked.connect(self.pressP)
        self.proButton3.clicked.connect(self.pressP)

        # 消费者
        self.cumButton1.clicked.connect(self.pressC)
        self.cumButton2.clicked.connect(self.pressC)
        self.cumButton3.clicked.connect(self.pressC)

        '''添加个人信息'''
        font4 = QFont()
        font4.setFamily('微软雅黑')

        author = QLineEdit('GitHub: YilK', self)
        author.setFont(font4)
        place = QLineEdit('CSDN: Yk_0311', self)
        place.resize(120, 30)
        place.setFont(font4)
        author.move(5, 280)
        place.move(5, 310)
        author.setDisabled(True)
        place.setDisabled(True)
        '''基本设置'''
        self.resize(470, 350)
        self.setWindowTitle('生产者-消费者问题')
        self.setWindowIcon(QIcon('a.JPG'))
        self.show()

    def pressP(self):
        """处理生产者按钮按下产生的事件"""
        source = self.sender()
        producer = source.text()  # 指明哪一个生产者

        if producer[-1] == '1':
            product = '1-Java'
        elif producer[-1] == '2':
            product = '2-Python'
        else:
            product = '3-C++'

        if self.lineEdit1.text() == '':  # 如果仓库为空
            # 先检查阻塞队列
            if self.lineEdit4.text() != '':  # 阻塞队列不为空，消费者阻塞了
                # 判断是哪个消费者阻塞了
                if self.lineEdit4.text()[-1] == '1':
                    button = 1  # 做标记，后面要将消费者按钮设置为可按
                    # self.cumButton1.setEnabled(True)

                elif self.lineEdit4.text()[-1] == '2':
                    button = 2

                else:
                    button = 3

                # 将阻塞的消费者删除
                for i in range(len(self.Block_queue) - 1):
                    self.Block_queue[i].setText(self.Block_queue[i + 1].text())
                self.Block_queue[2].setText('')
                # 对应的消费者按钮设置为可按
                if button == 1:
                    self.cumButton1.setEnabled(True)
                elif button == 2:
                    self.cumButton2.setEnabled(True)
                else:
                    self.cumButton3.setEnabled(True)

            else:  # 如果阻塞队列也为空
                for item in self.wavehouse:  # 遍历仓库的空间
                    if item.text() == '':  # 该空间为空
                        item.setFont(self.font3)
                        item.setText(product)  # 添加产品
                        break

        else:
            if self.lineEdit3.text() != '':  # 如果仓库已经满了

                # 进入阻塞队列
                for item in self.Block_queue:  # 遍历阻塞队列的空间
                    if item.text() == "":  # 该空间为空
                        item.setFont(self.font3)
                        item.setText(product)  # 添加产品
                        self.sender().setEnabled(False)  # 将对应生产者的按钮设置为不可按
                        break
            else:  # 如果仓库还没有满

                for item in self.wavehouse:  # 遍历仓库的空间
                    if item.text() == '':  # 该空间为空
                        item.setFont(self.font3)
                        item.setText(product)  # 添加产品
                        break

    def pressC(self):
        source = self.sender()
        consumer = source.text()  # 指明哪一个消费者

        if consumer[-1] == '1':
            consume = 'consumer1'
        elif consumer[-1] == '2':
            consume = 'consumer2'
        else:
            consume = 'consumer3'

        if self.lineEdit1.text() == '':  # 如果仓库中没有产品
            # self.sender().setEnabled(False)
            # if self.sender().
            for item in self.Block_queue:  # 遍历阻塞队列的空间
                if item.text() == "":  # 该空间为空
                    item.setFont(self.font3)  # 设置字体
                    item.setText(consume)
                    self.sender().setEnabled(False)  # 设置为不可按
                    break

        else:  # 如果仓库中有产品
            # 遍历仓库，取走一个位置的产品
            for i in range(len(self.wavehouse) - 1):
                self.wavehouse[i].setText(self.wavehouse[i + 1].text())

            # 将阻塞队列的第一个产品放入仓库
            self.lineEdit3.setText(self.lineEdit4.text())

            # 从阻塞队列进入到仓库的产品对应的生产者按钮设置为可按
            if self.lineEdit3.text() == '1-Java':
                self.proButton1.setEnabled(True)
            elif self.lineEdit3.text() == '2-Python':
                self.proButton2.setEnabled(True)
            else:
                self.proButton3.setEnabled(True)

            # 阻塞队列中产品往前移
            for j in range(len(self.Block_queue) - 1):
                self.Block_queue[j].setText(self.Block_queue[j + 1].text())
            self.lineEdit6.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
