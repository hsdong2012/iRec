# -*- coding:utf-8 -*-
__author__ = "董虎胜"

'''
iRec基于人脸识别的会议考勤系统
开发环境:Python3.7, face_recoginition 1.2.3, dlib1.9.8, MySQL5.5.46, PyQt5.12, PyCharm2017
开发人:董虎胜
联系方式:hsdong2012@QQ.com
'''

# 添加项目所到目录到sys.path中
import os
import sys
sys.path.append(os.path.dirname(__file__))


import shutil
import qdarkstyle

from util.dbutil import DbUtil
from form.login import Ui_MainWindow as LoginWindow

from PyQt5.QtWidgets import QApplication, QWidget

def initSys():
    # 如果系统中不存在msyh字体则拷贝字体到系统目录
    if "win32" in sys.platform:
        if "msyh.ttc" not in os.listdir("C:\\windows\\fonts"):
            shutil.copy("resources\\font\\msyh.ttc", "C:\\windows\\fonts")
    elif "linux" in sys.platform:
        os.popen(r"sudo cp resources/font/msyh.ttc /usr/share/fonts/truetype/")
    elif "darwin" in sys.platform:
        os.popen(r"sudo cp resources/font/msyh.ttc /System/Library/Fonts/")

    # 首次运行时需要导入数据库
    if not DbUtil.isDataBaseExist(): # 查看系统所需数据库是否存在
        DbUtil.importDatabase()


if __name__ == '__main__':
    # 系统初始化
    initSys()

    app = QApplication(sys.argv)
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5()) # 使用黑色主题

    loginWindow = LoginWindow()
    loginWindow.show()

    # 加入消息循环队列
    sys.exit(app.exec_())