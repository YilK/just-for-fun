import sys
import demoTest
import matplotlib.pyplot as plt
import re

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QLabel, QTextEdit
from PyQt5.QtGui import QFont

class Example(QMainWindow):  # 单条评论语句的分析窗口
    def __init__(self):
        """初始化"""
        super().__init__()  # 初始化父类

        self.initUI()

    def word_style(self):
        """定义文字格式"""
        font = QFont()
        font.setFamily('微软雅黑')
        font.setPointSize(9)

        return font

    def initUI(self):
        """创建一个GUI"""

        self.font=self.word_style()

        '''创建组件'''
        self.label1 = QLabel(self)
        self.label1.setGeometry(30, 30, 101, 16)
        self.label1.setText("输入评论语句：")
        self.label1.setFont(self.font)


        self.label2 = QLabel(self)
        self.label2.setGeometry(50, 120, 81, 20)
        self.label2.setText("好评/差评：")
        self.label2.setFont(self.font)

        self.textEdit1 = QTextEdit(self)
        self.textEdit2 = QTextEdit(self)
        self.textEdit1.setGeometry(130, 30, 221, 71)
        self.textEdit2.setGeometry(130, 120, 113, 27)

        self.button1 = QPushButton(self)
        self.button1.setText("提交")
        self.button1.setFont(self.font)
        self.button1.setGeometry(310, 110, 93, 28)

        self.button2 = QPushButton(self)
        self.button2.setFont(self.font)
        self.button2.setText('评论集测试')
        self.button2.setGeometry(310, 130, 93, 28)

        # 添加按钮事件
        self.button1.clicked.connect(self.pressadd)

        self.button2.clicked.connect(self.invisable)

        """基本设置"""
        self.setWindowTitle("评论分析")
        self.resize(414, 177)
        self.show()

    def invisable(self):  # button2按下后使窗口不可见
        self.setVisible(False)

    def pressadd(self):
        content = self.textEdit1.toPlainText()  # 输入的评论语句

        number, p1, p0 = demoTest.main(content)  # p1代表好评的概率，p0代表差评的概率，number=1代表是好评
        if number == 1:
            self.textEdit2.setText("好评")
        else:
            self.textEdit2.setText("差评")

        pgood = p0 / (p1 + p0)
        pbad = p1 / (p1 + p0)
        # 显示图片
        X = ["good", "bad"]
        Y = [pgood, pbad]
        plt.bar(X, Y, color=['#CDB5CD', '#B23AEE'], edgecolor='white', width=0.35)
        # for y in range(Y):
        #     plt.text
        plt.text(0, pgood, "{:.2f}".format(pgood), ha='center', va='bottom')
        plt.text(1, pbad, "{:.2f}".format(pbad), ha='center', va='bottom')
        plt.show()
    # self.textEdit2.setText(str(number))


class Example2(QWidget):#评论集的分析窗口

    def __init__(self):
        """初始化"""
        super().__init__()  # 初始化父类

        self.initUI()
    def word_style(self):
        """定义文字格式"""
        font = QFont()
        font.setFamily('微软雅黑')
        font.setPointSize(9)

        return font
    def initUI(self):
        """创建一个GUI"""
        self.font = self.word_style()
        '''创建组件'''
        self.label1 = QLabel(self)
        self.label1.setGeometry(10, 20, 155, 16)
        self.label1.setFont(self.font)
        self.label1.setText("输入评论集所在的位置:")

        self.label2 = QLabel(self)
        self.label2.setGeometry(50, 120, 81, 20)
        self.label2.setFont(self.font)
        self.label2.setText("好评/差评：")

        self.textEdit1 = QTextEdit(self)
        self.textEdit2 = QTextEdit(self)
        self.textEdit1.setGeometry(180, 20, 221, 71)
        self.textEdit2.setGeometry(130, 120, 113, 27)

        self.button = QPushButton(self)
        self.button.setText("提交")
        self.button.setFont(self.font)
        self.button.setGeometry(310, 100, 93, 28)

        # 添加按钮事件
        self.button.clicked.connect(self.pressadd)

        """基本设置"""
        self.setWindowTitle("评论集分析")
        self.resize(414, 177)
        self.show()

    def text_parse(self, path):
        '''读取评论集合内容'''
        contents = []
        path = path.replace('\\', '/')
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:  # 读行
                line = re.sub("\d.", "", line)  # 将所有的数字去掉
                contents.append(line)
                # text = re.sub('\W*', '', line)  # 将所有的特殊符号去掉
                # seg_list = jieba.cut(text, cut_all=False)  # 精确模式分割
                # contents.append(list(seg_list))
        return contents

    def pressadd(self):
        path = self.textEdit1.toPlainText()  # 输入的路径
        contents = self.text_parse(path)
        # print(contents)
        gtime = 0
        btime = 0
        for content in contents:
            number, p1, p0 = demoTest.main(content)
            if number == 1:
                gtime = gtime + 1
            else:
                btime = btime + 1
        if gtime > btime:
            self.textEdit2.setText("好评")
        else:
            self.textEdit2.setText("差评")
        pgood = gtime / (gtime + btime)
        pbad = 1 - pgood
        # 显示图片
        X = ["good", "bad"]
        Y = [pgood, pbad]
        plt.bar(X, Y, color=['#CDB5CD', '#B23AEE'], edgecolor='white', width=0.35,)
        # for y in range(Y):
        #     plt.text
        plt.text(0, pgood, "{:.2f}".format(pgood), ha='center', va='bottom')
        plt.text(1, pbad, "{:.2f}".format(pbad), ha='center', va='bottom')
        plt.legend(loc='right')
        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex2 = Example2()
    ex1 = Example()
    sys.exit(app.exec_())
