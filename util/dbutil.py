# -*- coding:utf-8 -*-
import os
import sys
import codecs
import pymysql
from configparser import ConfigParser
from PyQt5.QtWidgets import QMessageBox

"""
连接MySQL, 导入数据库, 加载配置文件, 创建Connection与Cursor对象 
"""
class DbUtil(object):
    conn = None

    # 查询MySQL数据库中是否存存在本系统所需数据库
    @classmethod
    def isDataBaseExist(cls):
        # 读取数据库配置文件
        host, port, user, password, database = cls.loadConfig()

        # 创建connection对象执行创建数据库语句
        try:
            conn = pymysql.connect(host=host, port=port, user=user, password=password)

            # 返回数据库执行游标
            cur = conn.cursor()

            # 执行创建数据库语句
            results = cur.execute("SELECT * FROM information_schema.SCHEMATA where SCHEMA_NAME='%s';"%database)

            if results:
                return True
            else:
                return False

        except Exception as e:
            print(e)
            return False
        finally:
            if cur:
                cur.close()

            if conn:
                conn.close()

    # 创建数据库,导入数据库(导入SQL语句)
    @classmethod
    def importDatabase(cls):
        # 读取数据库配置文件
        host, port, user, password, database = cls.loadConfig()

        # 创建connection对象执行创建数据库语句
        try:
            conn = pymysql.connect(host=host, port=port, user=user, password=password)

            # 返回数据库执行游标
            cur = conn.cursor()

            # 执行创建数据库语句
            cur.execute("create database "+database+" character set utf8;")
        except Exception as e:
            print(e)
            print("错误!访问MySQL数据库失败!")
            return
        finally:
            if cur:
                cur.close()

            if conn:
                conn.close()

        # sql文件
        sqlfile = 'conf/attend_bak.sql'

        if not os.path.isfile(sqlfile):
            print("严重错误!需要导入的SQL文件不存在!")
            sys.exit(1) # 错误退出!

        # 导入数据库命令
        command = "mysql -u"+user+" -h"+host+" -p"+password+" -P3306 "+database+"  < " + sqlfile

        # 执行命令
        try:
            os.system(command)
        except Exception as e:
            print(e)
            print("导入数据库失败!")

    # 创建数据库连接对象
    @classmethod
    def getConnection(cls):
        # 读取数据库配置
        host, port, user, password, database = cls.loadConfig()

        # 创建数据库connection对象
        try:
            conn = pymysql.connect(host=host, port=port, user=user, password=password, db=database)

            # 返回数据库执行游标
            cur = conn.cursor()

            return conn, cur
        except Exception as e:
            print(e)
            QMessageBox.critical(cls, "错误", "数据访问错误!", QMessageBox.Yes)

            return None, None


    # 关闭数据连接，释放资源
    @classmethod
    def close(cls, conn, cur):
        # 非空则释放资源
        if conn:
            conn.close()

        if cur:
            cur.close()

    # 加载数据库配置文件
    @classmethod
    def loadConfig(cls):
        # 创建ConfigParser对象
        parser = ConfigParser()

        try:
            # 读取配置文件
            parser.readfp(codecs.open("conf/config.ini","r","utf-8-sig"))

            # 获取配置
            host = parser.get("mysql", "db_host")
            port = parser.getint("mysql", "db_port")
            user = parser.get("mysql", "db_user")
            password = parser.get("mysql", "db_password")
            database = parser.get("mysql", "db_database")

            # 读取成功，返回
            return host, port, user, password, database
        except Exception as e:
            print(e)

        # 未获取到内容, 返回None
        return None


if __name__ == '__main__':
    DbUtil.importDatabase()
    conn, cur = DbUtil.getConnection()
    DbUtil.close(conn, cur)
