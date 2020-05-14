# -*- coding:utf-8 -*-

class Attend(object):
    """
    对应于tab_attend数据表中的数据字段
    """
    def __init__(self, meetingid, empid, arrivaltime, islate):
        """Constructor for Attend"""
        self.__meetingid = meetingid
        self.__empid = empid
        self.__arrivaltime = arrivaltime
        self.__islate = islate

    def set_meetingid(self, meetingid):
        self.__meetingid = meetingid

    def get_meetingid(self):
        return self.__meetingid

    def set_empid(self, empid):
        self.__empid = empid

    def get_empid(self):
        return self.__empid

    def set_arrivaltime(self, arrivaltime):
        self.__arrivaltime = arrivaltime

    def get_arrivaltime(self):
        return self.__arrivaltime

    def set_islate(self, islate):
        self.__islate = islate

    def get_islate(self):
        return self.__islate

    def __str__(self):
        return "attend:[meetingid:%s, staffid:%s, arrivaltime:%s, islate:%s]" %(
            self.__meetingid, self.__empid, self.__arrivaltime, self.__islate )

if __name__ == '__main__':
    attendSample = Attend("20190102130908", "s001", "2019-12-21", "是")
    print(attendSample)

