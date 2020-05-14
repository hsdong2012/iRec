# -*- coding:utf-8 -*-

class Post(object):
    """
    对应于tab_post数据表中的数据字段
    """
    def __init__(self, postid, postname, postintro):
        """Constructor for Post"""
        self.__postid = postid
        self.__postname = postname
        self.__postintro = postintro

    def get_postid(self):
        return self.__postid

    def set_postid(self, postid):
        self.__postid == postid

    def get_postname(self):
        return self.__postname

    def set_postname(self, postname):
        self.__postname = postname

    def get_postintro(self):
        return self.__postintro

    def set_postintro(self, postintro):
        self.__postintro = postintro

    def __str__(self):
        return "position:[postid:%s, postname:%s, postintro:%s]" %( self.__postid, self.__postname, self.__postintro)

if __name__ == '__main__':
    postSample = Post(1, "教师", "为本单位学生提供教学服务")
    print(postSample)


