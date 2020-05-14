# -*- coding:utf-8 -*-
from entity.meeting import Meeting
from util.dbutil import DbUtil

# 对tab_meeting表进行DAO操作的类
class MeetingDAO(object):
    def __init__(self):
        self.conn, self.cur = DbUtil.getConnection()

    # 根据时间地点与参会人员检索会议
    def findMeetingByTimePlaceAttenders(self, starttime, place, attenders):
        meetingList = []

        try:
            # 定义sql语句
            sql = "select * from tab_meeting where starttime='%s' and place='%s' and attenders='%s';"%(starttime, place, attenders)

            self.cur.execute(sql)
            results = self.cur.fetchall()

            for row in results:
                meeting = self.__mapToMeeting(row)
                meetingList.append(meeting)  # 加入列表
            return meetingList
        except Exception as e:
            print(e)
            return meetingList
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)

    # 检索所有会议信息
    def findAll(self):
        meetingList = []

        try:
            # 定义sql语句
            sql = "select * from tab_meeting;"

            self.cur.execute(sql)
            results = self.cur.fetchall()

            for row in results:
                meeting = self.__mapToMeeting(row)
                meetingList.append(meeting) # 加入列表
            return meetingList
        except Exception as e:
            print(e)
            return meetingList
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)

    # 根据日期检索会议
    def findMeetingByDate(self, meetingDate):
        meetingList = []

        # 定义基本sql语句
        sql = "select * from tab_meeting where DATE(starttime)='%s';" % meetingDate

        try:
            self.cur.execute(sql)
            results = self.cur.fetchall()

            for row in results:
                meeting = self.__mapToMeeting(row)
                meetingList.append(meeting)  # 加入列表

            return meetingList
        except Exception as e:
            print(e)
            return meetingList
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)


    # 根据输入的会议日期与主题进行模糊检索
    def findMeetingByDateAndTopic(self, meetingDate, meetingTopic):
        meetingList = []

        # 定义基本sql语句
        baseSQL = "select * from tab_meeting where 1=1 "

        # 拼接日期, 精确匹配日期(不考虑时间)
        if meetingDate:
            sql = baseSQL + " and DATE(starttime)='%s' "%meetingDate

        # 拼接主题, 模糊查找
        if len(meetingTopic) > 0:
            sql = sql + " and topic like '%%%s%%'"%meetingTopic

        try:
            self.cur.execute(sql)
            results = self.cur.fetchall()

            for row in results:
                meeting = self.__mapToMeeting(row)
                meetingList.append(meeting)  # 加入列表
            return meetingList
        except Exception as e:
            print(e)
            return meetingList
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)

    # 向数据表中插入一条记录
    def addMeeting(self, meeting):
        meetingid = meeting.get_meetingid()
        starttime = meeting.get_starttime()
        chairman = meeting.get_chairman()
        place = meeting.get_place()
        topic = meeting.get_topic()
        attenders = meeting.get_attenders()
        remarks = meeting.get_remarks()

        try:
            # 定义sql语句
            sql = "insert into tab_meeting values ('%s', str_to_date('%s','%%Y-%%m-%%d %%H:%%i:%%s'), '%s', '%s', '%s', '%s','%s');" % (meetingid, starttime, place, chairman, topic, attenders, remarks)

            self.cur.execute(sql)
            self.conn.commit()

            return True  # 添加成功，返回True
        except Exception as e:
            print(e)
            self.conn.rollback()
            return False  # 添加失败, 返回False
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)

    # 更新tab_emp中的一条记录
    def updateMeeting(self, meeting):
        meetingid = meeting.get_meetingid()
        starttime = meeting.get_starttime()
        chairman = meeting.get_chairman()
        place = meeting.get_place()
        topic = meeting.get_topic()
        attenders = meeting.get_attenders()
        remarks = meeting.get_remarks()

        try:
            # 定义sql语句, 采用模糊检索
            sql = "update tab_meeting set starttime=str_to_date('%s','%%Y-%%m-%%d %%H:%%i'), chairman='%s', place='%s', topic='%s', attenders='%s', remarks='%s' where meetingid='%s';" % (starttime, chairman, place, topic, attenders, remarks, meetingid)

            self.cur.execute(sql)
            self.conn.commit()

            return True  # 添加成功，返回True
        except Exception as e:
            print(e)
            self.conn.rollback()
            return False  # 添加失败, 返回False
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)

    # 删除tab_meeting中的一条记录
    def deleteMeetingByID(self, meetingid):
        try:
            # 定义sql语句, 采用模糊检索
            sql = "delete from tab_meeting where meetingid='%s';"%meetingid

            self.cur.execute(sql)
            self.conn.commit()

            return True  # 添加成功，返回True
        except Exception as e:
            print(e)
            self.conn.rollback()
            return False  # 添加失败, 返回False
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)

    # 将从数据库中检索出的所有对象的一行信息封装为一个Meeting对象
    def __mapToMeeting(self, row):
        meetingid = row[0]
        starttime = row[1]
        chairman = row[2]
        place = row[3]
        topic = row[4]
        attenders = row[5]
        remarks = row[6]

        # 创建Meeting对象
        meeting = Meeting(meetingid, starttime, chairman, place, topic, attenders, remarks)

        return meeting

