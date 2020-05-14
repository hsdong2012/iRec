# -*- coding:utf-8 -*-

class Emp:
    def __init__(self, empid, name, password, gender, phone, deptid, postid, syslevel):
        """
        :param empid: 员工编号id
        :param name: 员工姓名
        :param password: 员工密码
        :param gender: 员工性别
        :param phone: 电话号码
        :param deptid: 所在部分id
        :param postid: 所在岗位id
        :param syslevel: 级别
        """

        self.__empid = empid
        self.__name = name
        self.__password = password
        self.__gender = gender
        self.__phone = phone
        self.__deptid = deptid
        self.__postid = postid
        self.__syslevel = syslevel

    def get_empid(self):
        return self.__empid

    def set_empid(self, empid):
        self.__empid = empid

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_deptid(self):
        return self.__deptid

    def set_deptid(self, deptid):
        self.__deptid = deptid

    def get_postid(self):
        return self.__postid

    def set_postid(self, postid):
        self.__postid = postid

    def get_syslevel(self):
        return self.__syslevel

    def set_syslevel(self, syslevel):
        self.__syslevel = syslevel

    def __str__(self):
        return "Emp:[empid:%s, name:%s, passoword:%s, gender:%s, phone:%s, dept:%s, postid:%s, syslevel:%s]"%(self.__empid,
                self.__name, self.__password, self.__gender, self.__phone, self.__deptid, self.__postid, self.__syslevel)

if __name__ == '__main__':
    s = Emp("001", "张三", "123", "男", "123", "1", "2", 1) # 示例
    print(s)