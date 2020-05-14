# -*- coding:utf-8 -*-

class Meeting(object):
    """
    对应于tab_meeting数据表中的数据字段
    """
    def __init__(self, meetingid, starttime, place, chairman, topic, attenders, remarks):
        """Constructor for Attend"""
        self.__meetingid = meetingid
        self.__starttime = starttime
        self.__place = place
        self.__chairman = chairman
        self.__topic = topic
        self.__attenders = attenders
        self.__remarks = remarks

    def get_meetingid(self):
        return self.__meetingid

    def set_meetingid(self, meetingid):
        self.__meetingid = meetingid

    def get_starttime(self):
        return self.__starttime

    def set_starttime(self, starttime):
        self.__starttime = starttime

    def get_place(self):
        return self.__place

    def set_place(self, place):
        self.__place = place

    def get_chairman(self):
        return self.__chairman

    def set_chairman(self, chairman):
        self.__chairman = chairman

    def get_topic(self):
        return self.__topic

    def set_topic(self, topic):
        self.__topic = topic

    def get_attenders(self):
        return self.__attenders

    def set_attenders(self, attenders):
        self.__attenders = attenders

    def get_remarks(self):
        return self.__remarks

    def set_remarks(self, remarks):
        self.__remarks = remarks

    def __str__(self):
        return "meeting:[meetingid:%s, starttime:%s, place:%s, chairman:%s, topic:%s, attenders:%s, remarks:%s]" %(
            self.__meetingid, self.__starttime, self.__place, self.__chairman, self.__topic, self.__attenders, self.__remarks)

if __name__ == '__main__':
    meetingSample = Meeting(1, "13:00", "李冬","3318会议室", "办公室会议", "张三,李四", "没有什么信息需要说明")
    print(meetingSample)


