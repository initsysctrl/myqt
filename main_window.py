'''
Date: 2021-02-26 04:24:41
LastEditTime: 2021-02-26 04:52:37
Author: Ye-P
Descripttion: 
'''
from Ui_first import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
import random
import requests


class MyWindow(Ui_MainWindow, QMainWindow):
    # parent = None代表此QWidget属于最上层的窗口,也就是MainWindows.
    def __init__(self, parent=None):
        super(MyWindow, self).__init__()  # 因为继承关系，要对父类初始化
        # 通过super初始化父类，__init__()函数无self，若直接QtWidgets.QDialog).__init__(self)，括号里是有self的
        self.setupUi(self)
        self.action()  # 存放所有的信号槽

    def action(self):
        self.pushButton.clicked.connect(self.buttonClicked)
        self.pushButton_2.clicked.connect(self.buttonClicked2)

    def buttonClicked(self):
        s = random.choice(['CCTV', 'XMD', 'Hello', 'world'])
        self.label.setText(s)
        if self.pushButton.text() == '开始':
            self.pushButton.setText('停止')
        else:
            self.pushButton.setText('开始')

    def buttonClicked2(self):
        # self.graphicsView.
        res = requests.get('http://www.baidu.com')
        print(res.status_code)
        self.label_2.setText(str(res.status_code))

        pass
