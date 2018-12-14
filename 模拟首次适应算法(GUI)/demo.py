import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, \
    QTextEdit, QMessageBox

from PyQt5.QtGui import QFont, QIcon


class Example(QWidget):

    def __init__(self):
        """初始化"""
        super().__init__()  # 初始化父类

        self.initUI()

    def word_style(self):
        """定义文字格式"""
        font1 = QFont()
        font1.setFamily("consolas")

        font2 = QFont()
        font2.setFamily("微软雅黑")
        font2.setBold(True)
        font2.setPointSize(11)

        font3 = QFont()
        font3.setFamily("微软雅黑")
        font3.setBold(True)
        font3.setPointSize(12)

        font4 = QFont()
        font4.setFamily("微软雅黑")
        font4.setPointSize(10)

        font5 = QFont()
        font5.setFamily("微软雅黑")

        return font1, font2, font3, font4, font5

    def initUI(self):
        """创建一个GUI"""

        # 定义文字的样式
        font1, font2, font3, font4, font5 = self.word_style()

        '''创建组件'''
        # 内存块
        self.LineEdit1 = QLineEdit(self)
        self.LineEdit2 = QLineEdit(self)
        self.LineEdit3 = QLineEdit(self)
        self.LineEdit4 = QLineEdit(self)
        self.LineEdit5 = QLineEdit(self)
        self.LineEdit6 = QLineEdit(self)
        self.LineEdit7 = QLineEdit(self)
        self.LineEdit8 = QLineEdit(self)
        self.LineEdit9 = QLineEdit(self)
        self.LineEdit10 = QLineEdit(self)
        self.LineEdit11 = QLineEdit(self)
        self.LineEdit12 = QLineEdit(self)
        self.LineEdit13 = QLineEdit(self)
        self.LineEdit14 = QLineEdit(self)
        self.LineEdit15 = QLineEdit(self)
        self.LineEdit16 = QLineEdit(self)
        self.LineEdit17 = QLineEdit(self)
        self.LineEdit18 = QLineEdit(self)
        self.LineEdit19 = QLineEdit(self)
        self.LineEdit20 = QLineEdit(self)
        self.LineEdit21 = QLineEdit(self)
        self.LineEdit22 = QLineEdit(self)
        self.LineEdit23 = QLineEdit(self)
        self.LineEdit24 = QLineEdit(self)
        self.LineEdit25 = QLineEdit(self)
        self.LineEdit26 = QLineEdit(self)
        self.LineEdit27 = QLineEdit(self)
        self.LineEdit28 = QLineEdit(self)
        self.LineEdit29 = QLineEdit(self)
        self.LineEdit30 = QLineEdit(self)
        self.LineEdit31 = QLineEdit(self)
        self.LineEdit32 = QLineEdit(self)
        self.LineEdit33 = QLineEdit(self)
        self.LineEdit34 = QLineEdit(self)
        self.LineEdit35 = QLineEdit(self)
        self.LineEdit36 = QLineEdit(self)
        self.LineEdit37 = QLineEdit(self)
        self.LineEdit38 = QLineEdit(self)
        self.LineEdit39 = QLineEdit(self)
        self.LineEdit40 = QLineEdit(self)
        self.LineEdit41 = QLineEdit(self)
        self.LineEdit42 = QLineEdit(self)
        self.LineEdit43 = QLineEdit(self)
        self.LineEdit44 = QLineEdit(self)
        self.LineEdit45 = QLineEdit(self)
        self.LineEdit46 = QLineEdit(self)
        self.LineEdit47 = QLineEdit(self)
        self.LineEdit48 = QLineEdit(self)
        self.LineEdit49 = QLineEdit(self)
        self.LineEdit50 = QLineEdit(self)
        self.LineEdit51 = QLineEdit(self)
        self.LineEdit52 = QLineEdit(self)
        self.LineEdit53 = QLineEdit(self)
        self.LineEdit54 = QLineEdit(self)
        self.LineEdit55 = QLineEdit(self)
        self.LineEdit56 = QLineEdit(self)
        self.LineEdit57 = QLineEdit(self)
        self.LineEdit58 = QLineEdit(self)
        self.LineEdit59 = QLineEdit(self)
        self.LineEdit60 = QLineEdit(self)

        self.all_lineedit = [self.LineEdit1, self.LineEdit2, self.LineEdit3, self.LineEdit4, self.LineEdit5,
                             self.LineEdit6, self.LineEdit7, self.LineEdit8, self.LineEdit9, self.LineEdit10,
                             self.LineEdit11, self.LineEdit12, self.LineEdit13, self.LineEdit14, self.LineEdit15,
                             self.LineEdit16, self.LineEdit17, self.LineEdit18, self.LineEdit19, self.LineEdit20,
                             self.LineEdit21, self.LineEdit22, self.LineEdit23, self.LineEdit24, self.LineEdit25,
                             self.LineEdit26, self.LineEdit27, self.LineEdit28, self.LineEdit29, self.LineEdit30,
                             self.LineEdit31, self.LineEdit32, self.LineEdit33, self.LineEdit34, self.LineEdit35,
                             self.LineEdit36, self.LineEdit37, self.LineEdit38, self.LineEdit39, self.LineEdit40,
                             self.LineEdit41, self.LineEdit42, self.LineEdit43, self.LineEdit44, self.LineEdit45,
                             self.LineEdit46, self.LineEdit47, self.LineEdit48, self.LineEdit49, self.LineEdit50,
                             self.LineEdit51, self.LineEdit52, self.LineEdit53, self.LineEdit54, self.LineEdit55,
                             self.LineEdit56, self.LineEdit57, self.LineEdit58, self.LineEdit59, self.LineEdit60,
                             ]
        # 设置内存块的位置
        i = 10
        for item in self.all_lineedit:
            item.setGeometry(i, 80, 16, 71)
            i = i + 20

        # 添加按钮组件
        self.Button1 = QPushButton(self)
        self.Button1.setGeometry(680, 320, 151, 81)
        self.Button1.setText("添加")
        self.Button1.setFont(font3)
        self.Button2 = QPushButton(self)
        self.Button2.setGeometry(1050, 320, 151, 81)
        self.Button2.setText("回收")
        self.Button2.setFont(font3)

        # 添加标签组件
        self.label = QLabel(self)
        self.label.setGeometry(10, 153, 16, 31)
        self.label.setFont(font1)
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(110, 160, 16, 16)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self)
        self.label_3.setGeometry(410, 160, 16, 16)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self)
        self.label_4.setGeometry(610, 160, 16, 16)
        self.label_4.setFont(font1)
        self.label_5 = QLabel(self)
        self.label_5.setGeometry(1010, 160, 72, 15)
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self)
        self.label_6.setGeometry(10, 10, 81, 31)
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet('color:red')
        self.label_7 = QLabel(self)
        self.label_7.setGeometry(10, 60, 72, 15)
        self.label_7.setFont(font1)
        self.label_8 = QLabel(self)
        self.label_8.setGeometry(100, 60, 72, 15)
        self.label_8.setFont(font1)
        self.label_9 = QLabel(self)
        self.label_9.setGeometry(400, 60, 72, 15)
        self.label_9.setFont(font1)
        self.label_10 = QLabel(self)
        self.label_10.setGeometry(600, 60, 72, 15)
        self.label_10.setFont(font1)
        self.label_11 = QLabel(self)
        self.label_11.setGeometry(1000, 60, 72, 15)
        self.label_11.setFont(font1)
        self.label_12 = QLabel(self)
        self.label_12.setGeometry(1190, 60, 72, 15)
        self.label_12.setFont(font1)
        self.label_13 = QLabel(self)
        self.label_13.setGeometry(420, 270, 270, 31)
        self.label_13.setFont(font4)
        self.label_14 = QLabel(self)
        self.label_14.setGeometry(870, 270, 200, 31)
        self.label_14.setFont(font4)

        # 添加文本组件
        self.lineEdit_61 = QLineEdit(self)
        self.lineEdit_61.setGeometry(700, 270, 113, 31)
        self.lineEdit_62 = QLineEdit(self)
        self.lineEdit_62.setGeometry(1070, 270, 113, 31)
        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(580, 180, 650, 60)
        # 设置内容
        self.label.setText("1")
        self.label_2.setText("2")
        self.label_3.setText("3")
        self.label_4.setText("4")
        self.label_5.setText("5")
        self.label_6.setText("内存状态")
        self.label_7.setText("0")
        self.label_8.setText("5")
        self.label_9.setText("20")
        self.label_10.setText("30")
        self.label_11.setText("50")
        self.label_12.setText("60")
        self.label_13.setText("请输入需要分配的作业大小(0-20K)：")
        self.label_14.setText("请输入要回收的作业号：")
        self.textEdit.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'微软雅黑\'; font-size:10pt; font-weight:400; font-style:consoals;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">注:1.有五个空闲分区，分区1(5K),分区2(15K),分区3(10K),分区4(20K),分区5(10K)\r\t\t"
            "    2.作业号从1开始</p></body></html>")
        self.textEdit.setEnabled(False)  # 设置组件内容为不可变

        self.label_15 = QLabel(self)
        self.label_15.setGeometry(10, 190, 91, 31)
        self.label_15.setText("内存分配表")
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet("color:red")

        self.number = 0
        # 标记每个分区的大小
        self.place1 = 5
        self.place2 = 15
        self.place3 = 10
        self.place4 = 20
        self.place5 = 10

        # 每个分区所拥有的内存块，将其加入相应的列表
        self.content1 = [self.LineEdit1, self.LineEdit2, self.LineEdit3, self.LineEdit4, self.LineEdit5]
        self.content2 = [self.LineEdit6, self.LineEdit7, self.LineEdit8, self.LineEdit9, self.LineEdit10,
                         self.LineEdit11, self.LineEdit12, self.LineEdit13, self.LineEdit14, self.LineEdit15,
                         self.LineEdit16, self.LineEdit17, self.LineEdit18, self.LineEdit19, self.LineEdit20
                         ]
        self.content3 = [self.LineEdit21, self.LineEdit22, self.LineEdit23, self.LineEdit24, self.LineEdit25,
                         self.LineEdit26, self.LineEdit27, self.LineEdit28, self.LineEdit29, self.LineEdit30]

        self.content4 = [self.LineEdit31, self.LineEdit32, self.LineEdit33, self.LineEdit34, self.LineEdit35,
                         self.LineEdit36, self.LineEdit37, self.LineEdit38, self.LineEdit39, self.LineEdit40,
                         self.LineEdit41, self.LineEdit42, self.LineEdit43, self.LineEdit44, self.LineEdit45,
                         self.LineEdit46, self.LineEdit47, self.LineEdit48, self.LineEdit49, self.LineEdit50]
        self.content5 = [self.LineEdit51, self.LineEdit52, self.LineEdit53, self.LineEdit54, self.LineEdit55,
                         self.LineEdit56, self.LineEdit57, self.LineEdit58, self.LineEdit59, self.LineEdit60, ]

        # 每个分区的起始位置
        self.a = 0
        self.b = 5
        self.c = 20
        self.d = 30
        self.e = 50

        self.places = [[self.place1, self.content1, self.a],
                       [self.place2, self.content2, self.b],
                       [self.place3, self.content3, self.c],
                       [self.place4, self.content4, self.d],
                       [self.place5, self.content5, self.e]]

        self.text_list = [[0, '作业名\t起始地址\t终止地址\t作业长度\t分区\r']]  # 内存分配区的内容
        # 创建内存分配区
        self.textEdit_2 = QTextEdit(self)
        self.textEdit_2.setGeometry(10, 220, 400, 185)
        self.textEdit_2.setText(self.text_list[0][1])
        self.textEdit_2.setFont(font5)

        # 按钮按下的信号
        self.Button1.clicked.connect(self.pressadd)
        self.Button2.clicked.connect(self.pressremove)

        '''添加个人信息'''
        font6 = QFont()
        font6.setFamily("微软雅黑")

        author = QLineEdit('GitHub: YilK', self)
        author.setGeometry(411, 345, 120, 30)
        author.setFont(font6)
        author.setEnabled(False)
        place = QLineEdit('CSDN: Yk_0311', self)
        place.setGeometry(411, 378, 120, 30)
        place.setFont(font6)
        place.setEnabled(False)

        """基本设置"""
        self.setWindowTitle('首次适应算法')
        self.resize(1242, 419)
        self.show()

    def pressadd(self):  # 添加按钮按下

        content = self.lineEdit_61.text()  # 添加的作业的长度
        size = int(content)  # 转换为整形数据
        bool = False
        for item in self.places:  # 遍历每个分区空闲的大小
            if size <= item[0]:  # 如果作业长度小于分区的大小
                j = 0  # 计数器
                self.number += 1  # 表示第几个作业
                for LE in item[1]:  # 遍历这个分区的内存块
                    if LE.text() == "":  # 当此内存块没有占用
                        LE.setText(str(self.number))  # 填入作业名，表示属于第几个作业
                        j = j + 1
                        bool = True
                    if j == size:  # 装载完毕
                        break
                item[0] = item[0] - size  # 分区空闲减小
                # 写log
                a = item[2]  # 该作业的起始地址
                if a < 5:
                    rank = 1  # 该作业所在的分区
                elif a < 20:
                    rank = 2
                elif a < 30:
                    rank = 3
                elif a < 50:
                    rank = 4
                else:
                    rank = 5
                item[2] = item[2] + j  # 该作业的终止地址，是下个进入该区作业的起始地址
                ddv = '{}\t{}\t{}\t{}\t{}\r'.format(self.number, a, item[2], size, rank)  # 该作业的信息
                text = [self.number, ddv]  # 其中的self.number其实是其标记的作用，为回收作业做准备
                self.text_list.append(text)  # 添加入文本
                Text = ''
                for item in self.text_list:
                    Text += item[1]

                self.textEdit_2.setText(Text)  # 在文本区中输出

                break

        # 结束for循环，作业大小大于内存空间
        if bool == False:
            replay = QMessageBox.warning(self, 'warning',
                                         '无法为此作业分配内存', QMessageBox.Ok | QMessageBox.Ok)

    def pressremove(self):  # 回收按钮按下
        content = self.lineEdit_62.text()  # 要回收的作业号
        j = 0  # 计数
        LE = self.lineEdit_62  # 随便赋值的，最后指向的是某个区的内存块
        for item in self.all_lineedit:  # 遍历所有的内存块
            if item.text() == content:  # 找到内容是回收的作业号，将里面的内容删除
                j = j + 1
                LE = item
                item.setText('')  # 将里面的内容删除
        for item in self.places:
            if LE in item[1]:  # 如果是这个区的内存块
                item[0] += j  # 释放了作业，那么该区的空间应该对应的增加
                item[2] -= j  # 该区的下个作业的起始地址也应该改变
                break
        # 下面就是在内存分配表要输出的内容
        number = int(content)
        for item in self.text_list:
            if item[0] == number:
                self.text_list.remove(item)  # self.number会在这里起作用，删去对应的作业内容
                break
        Text = ''
        for item in self.text_list:
            Text += item[1]

        self.textEdit_2.setText(Text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
