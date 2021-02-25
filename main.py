'''
Date: 2021-02-24 02:05:21
LastEditTime: 2021-02-26 03:09:17
Author: Ye-P
Descripttion: 
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    print(sys.argv)
    # 创建应用程序
    app = QApplication(sys.argv)
    print(app.arguments())
    window = QWidget()
    window.setWindowTitle('操盘手.app')
    # 消息循环
    window.show()
    sys.exit(app.exec_())
