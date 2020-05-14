# -*- coding:utf-8 -*-

class Dept(object):
    """
    对应于tab_dept数据表中的数据字段
    """
    def __init__(self, deptid, deptname, deptintro):
        """Constructor for Dept"""
        self.__deptid = deptid
        self.__deptname = deptname
        self.__deptintro = deptintro

    def get_deptid(self):
        return self.__deptid

    def set_deptid(self, deptid):
        self.__deptid == deptid

    def get_deptname(self):
        return self.__deptname

    def set_deptname(self, deptname):
        self.__deptname = deptname

    def get_deptintro(self):
        return self.__deptintro

    def set_deptintro(self, deptintro):
        self.__deptintro = deptintro

    def __str__(self):
        return "department:[deptid:%s, deptname:%s, deptintro:%s]" %(
            self.__deptid, self.__deptname, self.__deptintro)

if __name__ == '__main__':
    deptSample = Dept(1, "办公室", "办公室负责为整个单位的所有人提供日常办公服务与管理")
    print(deptSample)


