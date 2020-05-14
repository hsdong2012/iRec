# -*- coding:utf-8 -*-
from entity.meeting import Meeting
from entity.attend import Attend
from dao.meetingdao import MeetingDAO
from util.dbutil import DbUtil
import time

# 对tab_meeting表进行DAO操作的类
class AttendDAO(object):
    def __init__(self):
        self.conn, self.cur = DbUtil.getConnection()

    # 增加多条员工的待参会信息
    def addMeeting4MultiAttenders(self, empIds, meetingid):
        resultList = list() # 返回各个EmpId的待参加会议记录的添加状态

        for empid in empIds:
            try:
                sql = "insert into tab_attend(empid, meetingid) values('%s', '%s')"%(empid, meetingid)
                flag = self.cur.execute(sql)
                self.conn.commit()

                resultList.append(flag)
            except Exception as e:
                resultList.append(0)

        # 手动关闭数据库连接
        DbUtil.close(self.conn, self.cur)
        return resultList


    # 删除多名员工的待参会记录
    def removeMultiAttenders(self, empIds, meetingid):
        resultList = list() # 返回各个EmpId的删除待参会记录的状态

        for empid in empIds:
            try:
                sql = "delete from tab_attend where empid='%s' and meetingid='%s';"%(empid, meetingid)
                flag = self.cur.execute(sql)
                self.conn.commit()

                resultList.append(flag)
            except Exception as e:
                resultList.append(0)

        # 手动关闭数据库连接
        DbUtil.close(self.conn, self.cur)
        return resultList

    # 为员工添加刷脸考勤时间记录, 注意考勤记录在安排会议时就已添加，只是没有插入时间，在下面的方法中只需要插入刷脸时间即可
    # !!!***!!!注意本方法没有设置关闭conn!需要手动关闭连接，目的是可以多次插入记录时减少连接时间，提高性能!
    def addAttendRecord(self, empid, meetingid, attendTime):
        try:
            sql = "update tab_attend set arrivaltime='%s' where empid='%s' and meetingid='%s';"%(attendTime, empid, meetingid)

            self.cur.execute(sql)
            self.conn.commit()

            return True  # 添加成功，返回True
        except Exception as e:
            print(e)
            self.conn.rollback()

            return False  # 添加失败, 返回False

    # 根据empid, 起止日期检索个人的考勤纪录情况, 根据前台页面需求进行了适当转换处理
    def findPersonalRecordInDateRange(self, empid, fromDate, endDate):
        attendRecordList = [] # 出勤纪录列表

        try:
            # 定义sql语句
            sql = """SELECT
                        e.name, m.topic, m.place, m.chairman, m.starttime, a.arrivaltime
                    FROM 
                        tab_emp e, tab_meeting m, tab_attend a
                    WHERE 
                        e.empid = a.empid AND m.meetingid = a.meetingid AND a.empid='%s'  
                        AND DATE(m.starttime)>='%s' AND DATE(m.starttime)<='%s';"""%(empid, fromDate, endDate)

            self.cur.execute(sql)
            results = self.cur.fetchall()

            for i in range(len(results)):
                rowRecord = list(results[i]) # 转换为列表类型
                rowRecord.insert(0, i+1)        # 添加搜索结果的序号, 从1开始计数

                if rowRecord[-1] is None:  # 如果为空说明没有参会
                    rowRecord.append('缺勤')
                else:
                    # 考勤时间戳大于会议开始时间，为迟到参会
                    if time.mktime(rowRecord[-1].timetuple()) > time.mktime(rowRecord[-2].timetuple()):
                        rowRecord.append('迟到')
                    # 小于等于会议开始时间为正常参会
                    else:
                        rowRecord.append('正常')

                attendRecordList.append(rowRecord) # 加入列表
            return attendRecordList
        except Exception as e:
            print(e)
            return attendRecordList
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)


    # 根据empid, 起止日期检索个人的迟到缺勤纪录情况, 根据前台页面需求进行了适当转换处理
    def findPersonalLateRecordInDateRange(self, empid, fromDate, endDate):
        lateAbsenceRecordList = [] # 出勤纪录列表

        try:
            # 定义sql语句, 在时间范围内，指定的empid的缺勤(签到时间为null)或迟到(签到时间大于会议开始时间)
            sql = """SELECT
                    e.name, m.topic, m.place, m.chairman, m.starttime, a.arrivaltime
                FROM 
                    tab_emp e, tab_meeting m, tab_attend a
                WHERE 
                    e.empid = a.empid AND m.meetingid = a.meetingid AND a.empid='%s'  
                    AND DATE(m.starttime)>='%s' AND DATE(m.starttime)<='%s' 
                    AND (a.arrivaltime>m.starttime OR a.arrivaltime IS NULL);"""%(empid, fromDate, endDate)

            self.cur.execute(sql)
            results = self.cur.fetchall()

            for i in range(len(results)):
                rowRecord = list(results[i]) # 转换为列表类型
                rowRecord.insert(0, i+1)        # 添加搜索结果的序号, 从1开始计数

                if rowRecord[-1] is None:  # 如果为空说明没有参会
                    rowRecord.append('缺勤')
                else:                       # 参会但是迟到
                    rowRecord.append('迟到')

                lateAbsenceRecordList.append(rowRecord) # 加入列表
            return lateAbsenceRecordList
        except Exception as e:
            print(e)
            return lateAbsenceRecordList
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)

    # 根据dept, 在起止日期内检索部门中所有成员的考勤, 根据前台页面需求进行了适当转换处理
    def findDeptRecordInDateRange(self, deptid, fromDate, endDate):
        attendRecordList = [] # 出勤纪录列表

        try:
            # 定义sql语句, 在时间范围内，指定的empid的缺勤(签到时间为null)或迟到(签到时间大于会议开始时间)
            sql = """SELECT
                        e.name, m.topic, m.place, m.chairman, m.starttime, a.arrivaltime
                    FROM 
                        tab_emp e, tab_meeting m, tab_attend a
                    WHERE 
                        e.empid = a.empid AND m.meetingid = a.meetingid AND e.deptid='%s'  
                        AND DATE(m.starttime)>='%s' AND DATE(m.starttime)<='%s';"""%(deptid, fromDate, endDate)

            self.cur.execute(sql)
            results = self.cur.fetchall()

            for i in range(len(results)):
                rowRecord = list(results[i])  # 转换为列表类型
                rowRecord.insert(0, i + 1)  # 添加搜索结果的序号, 从1开始计数

                if rowRecord[-1] is None:  # 如果为空说明没有参会
                    rowRecord.append('缺勤')
                else:
                    # 考勤时间戳大于会议开始时间，为迟到参会
                    if time.mktime(rowRecord[-1].timetuple()) > time.mktime(rowRecord[-2].timetuple()):
                        rowRecord.append('迟到')
                    # 小于等于会议开始时间为正常参会
                    else:
                        rowRecord.append('正常')

                attendRecordList.append(rowRecord) # 加入列表

            return attendRecordList
        except Exception as e:
            print(e)
            return attendRecordList
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)


    # 根据dept, 起止日期检索部门中所有成员的迟到缺勤纪录情况, 根据前台页面需求进行了适当转换处理
    def findDeptLateRecordInDateRange(self, deptid, fromDate, endDate):
        lateAbsenceRecordList = [] # 迟到缺勤纪录列表

        try:
            # 定义sql语句, 在时间范围内，指定的deptid的缺勤(签到时间为null)或迟到(签到时间大于会议开始时间)
            sql = """SELECT
                    e.name, m.topic, m.place, m.chairman, m.starttime, a.arrivaltime
                FROM 
                    tab_emp e, tab_meeting m, tab_attend a
                WHERE 
                    e.empid = a.empid AND m.meetingid = a.meetingid AND e.deptid='%s'  
                    AND DATE(m.starttime)>='%s' AND DATE(m.starttime)<='%s' 
                    AND (a.arrivaltime>m.starttime OR a.arrivaltime IS NULL);"""%(deptid, fromDate, endDate)

            self.cur.execute(sql)
            results = self.cur.fetchall()

            for i in range(len(results)):
                rowRecord = list(results[i]) # 转换为列表类型
                rowRecord.insert(0, i+1)        # 添加搜索结果的序号, 从1开始计数

                if rowRecord[-1] is None:  # 如果为空说明没有参会
                    rowRecord.append('缺勤')
                else:                       # 参会但是迟到
                    rowRecord.append('迟到')

                lateAbsenceRecordList.append(rowRecord) # 加入列表
            return lateAbsenceRecordList
        except Exception as e:
            print(e)
            return lateAbsenceRecordList
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)

    # 在起止日期内检索单位中所有成员的考勤, 根据前台页面需求进行了适当转换处理
    def findAllRecordInDateRange(self, fromDate, endDate):
        attendRecordList = [] # 出勤纪录列表

        try:
            # 定义sql语句, 在时间范围内所有考勤记录
            sql = """SELECT
                        e.name, m.topic, m.place, m.chairman, m.starttime, a.arrivaltime
                    FROM 
                        tab_emp e, tab_meeting m, tab_attend a
                    WHERE 
                        e.empid = a.empid AND m.meetingid = a.meetingid  
                        AND DATE(m.starttime)>='%s' AND DATE(m.starttime)<='%s';"""%(fromDate, endDate)

            self.cur.execute(sql)
            results = self.cur.fetchall()

            for i in range(len(results)):
                rowRecord = list(results[i])  # 转换为列表类型
                rowRecord.insert(0, i + 1)  # 添加搜索结果的序号, 从1开始计数

                if rowRecord[-1] is None:  # 如果为空说明没有参会
                    rowRecord.append('缺勤')
                else:
                    # 考勤时间戳大于会议开始时间，为迟到参会
                    if time.mktime(rowRecord[-1].timetuple()) > time.mktime(rowRecord[-2].timetuple()):
                        rowRecord.append('迟到')
                    # 小于等于会议开始时间为正常参会
                    else:
                        rowRecord.append('正常')

                attendRecordList.append(rowRecord) # 加入列表

            return attendRecordList
        except Exception as e:
            print(e)
            return attendRecordList
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)


    # 在起止日期内检索单位中所有成员的迟到缺勤纪录情况, 根据前台页面需求进行了适当转换处理
    def findAllLateRecordInDateRange(self, fromDate, endDate):
        lateAbsenceRecordList = [] # 迟到缺勤纪录列表

        try:
            # 定义sql语句, 在时间范围内，指定的deptid的缺勤(签到时间为null)或迟到(签到时间大于会议开始时间)
            sql = """SELECT
                    e.name, m.topic, m.place, m.chairman, m.starttime, a.arrivaltime
                FROM 
                    tab_emp e, tab_meeting m, tab_attend a
                WHERE 
                    e.empid = a.empid AND m.meetingid = a.meetingid 
                    AND DATE(m.starttime)>='%s' AND DATE(m.starttime)<='%s' 
                    AND (a.arrivaltime>m.starttime OR a.arrivaltime IS NULL);"""%(fromDate, endDate)

            self.cur.execute(sql)
            results = self.cur.fetchall()

            for i in range(len(results)):
                rowRecord = list(results[i]) # 转换为列表类型
                rowRecord.insert(0, i+1)        # 添加搜索结果的序号, 从1开始计数

                if rowRecord[-1] is None:  # 如果为空说明没有参会
                    rowRecord.append('缺勤')
                else:                       # 参会但是迟到
                    rowRecord.append('迟到')

                lateAbsenceRecordList.append(rowRecord) # 加入列表
            return lateAbsenceRecordList
        except Exception as e:
            print(e)
            return lateAbsenceRecordList
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)
