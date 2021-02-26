'''
Date: 2021-02-24 02:05:21
LastEditTime: 2021-02-26 04:47:01
Author: Ye-P
Descripttion: 
'''
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_window import MyWindow


if __name__ == "__main__":
    print(sys.argv)
    # 创建应用程序
    app = QApplication(sys.argv)
    print(app.arguments())
    window = MyWindow()
    window.setWindowTitle('操盘圣手.app')
    window.show()
    sys.exit(app.exec_())
