# -*- coding:utf-8 -*-
import os
import sys
import codecs
from configparser import ConfigParser

"""
读取配置文件config.in中的系统设置参数
"""
class ParamUtil(object):
    # 加载系统参数
    @classmethod
    def loadSysParams(cls):
        # 创建ConfigParser对象
        parser = ConfigParser()

        try:
            # 读取配置文件
            parser.readfp(codecs.open("conf/config.ini","r","utf-8-sig"))

            # 获取配置, 会议开始前900秒/15分钟开始签到，会议开始后1800秒停止签到
            checkin_interval = parser.getint("sysparam", "checkin_interval") # 签到时间长度, 以会议开始时间starttime为结束点
            checkin_stop = parser.getint("sysparam", "checkin_stop") # 停止签到时间长度, 以会议开始时间starttime为原点

            # 读取成功，返回
            return checkin_interval, checkin_stop
        except Exception as e:
            print(e)

        # 未获取到内容, 返回None
        return None


if __name__ == '__main__':
    checkin_interval, checkin_stop = ParamUtil.loadSysParams()
    print(checkin_interval, checkin_stop)
