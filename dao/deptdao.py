# -*- coding:utf-8 -*-
from entity.dept import Dept
from util.dbutil import DbUtil

# 对tb_dept表进行DAO操作的类
class DeptDAO(object):
    def __init__(self):
        self.conn, self.cur = DbUtil.getConnection()

    # 检索所有dept信息
    def findAll(self):
        deptList = []

        try:
            # 定义sql语句
            sql = "select * from tab_dept;"

            self.cur.execute(sql)
            results = self.cur.fetchall()

            for row in results:
                deptid = row[0]
                deptname = row[1]
                deptintro = row[2]

                # 创建taff对象
                dept = Dept(deptid, deptname, deptintro)

                # 加入列表
                deptList.append(dept)

            return deptList
        except Exception as e:
            print(e)
            return deptList
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)


    # 根据deptName检索dept信息
    def findDeptByName(self, deptName):
        deptList = []

        try:
            # 定义sql语句, 采用模糊检索
            sql = "select * from tab_dept where deptname like '%%%s%%';"%deptName

            self.cur.execute(sql)
            results = self.cur.fetchall()

            for row in results:
                deptid = row[0]
                deptname = row[1]
                deptintro = row[2]

                # 创建taff对象
                dept = Dept(deptid, deptname, deptintro)

                # 加入列表
                deptList.append(dept)

            return deptList
        except Exception as e:
            print(e)
            return deptList
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)


            # 根据deptName检索dept信息

    # 向数据表中插入一条记录
    def addDept(self, deptName, deptIntro):
        try:
            # 定义sql语句, 采用模糊检索
            sql = "insert into tab_dept(deptname, deptintro) values ('%s', '%s');" % (deptName, deptIntro)

            self.cur.execute(sql)
            self.conn.commit()

            return True # 添加成功，返回True
        except Exception as e:
            print(e)
            self.conn.rollback()
            return False # 添加失败, 返回False
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)

    # 更新tab_dept中的一条记录
    def updateDept(self, dept):
        try:
            # 定义sql语句, 采用模糊检索
            sql = "update tab_dept set deptname='%s', deptintro='%s' where deptid='%s';" % (dept.get_deptname(), dept.get_deptintro(), dept.get_deptid())

            self.cur.execute(sql)
            self.conn.commit()

            return True # 添加成功，返回True
        except Exception as e:
            print(e)
            self.conn.rollback()
            return False # 添加失败, 返回False
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)


    # 删除tab_dept中的一条记录
    def deleteDeptByDeptid(self, deptid):
        try:
            # 定义sql语句, 采用模糊检索
            sql = "delete from tab_dept where deptid='%s';" % (deptid)

            self.cur.execute(sql)
            self.conn.commit()

            return True # 添加成功，返回True
        except Exception as e:
            print(e)
            self.conn.rollback()
            return False # 添加失败, 返回False
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)



