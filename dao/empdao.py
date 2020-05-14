# -*- coding:utf-8 -*-
from entity.emp import Emp
from util.dbutil import DbUtil

# 对tb_staff表进行DAO操作的类
class EmpDAO(object):
    def __init__(self):
        self.conn, self.cur = DbUtil.getConnection()


    # 检索所有用户信息
    def findAll(self):
        empList = []

        try:
            # 定义sql语句
            sql = """SELECT
                        e.empid, e.name, e.password, e.gender, e.phone, d.deptname, p.postname, e.syslevel
                    FROM 
                        tab_emp e , tab_dept d, tab_post p
                    WHERE 
                        e.deptid = d.deptid AND e.postid = p.postid;"""

            self.cur.execute(sql)
            results = self.cur.fetchall()

            for row in results:
                emp = self.__mapToEmp(row)
                empList.append(emp) # 加入列表
            return empList
        except Exception as e:
            print(e)
            return empList
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)


    # 根据输入的用户名与MD5加密后的密码检索所用户, 用户登录时验证
    def findEmpByNameAndPassword(self, inputName, inputPasswordMd5):
        emp = None

        try:
            # 定义sql语句
            sql = "select * from tab_emp where name={} and password={};".format(repr(inputName), repr(inputPasswordMd5))

            self.cur.execute(sql)
            results = self.cur.fetchall()

            if len(results) > 1:
                raise Exception("存在多条重复记录!")
            elif len(results) == 1:
                row = results[0]
                emp = self.__mapToEmp(row) # 封装为emp对象

                return emp
        except Exception as e:
            print(e)
            return emp
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)

    # 根据输入empid进行精确检索
    def findEmpByID(self, empid):
        emp = None

        try:
            # 定义sql语句
            sql = "select * from tab_emp where empid='%s';"%empid

            self.cur.execute(sql)
            results = self.cur.fetchall()

            if len(results) > 1:
                raise Exception("存在多条重复记录!")
            elif len(results) == 1:
                row = results[0]
                emp = self.__mapToEmp(row)  # 封装为emp对象

                return emp
        except Exception as e:
            print(e)
            return emp
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)


    # 根据empName进行模糊检索emp信息
    def findEmpByName(self, empName):
        empList = []

        try:
            # 定义sql语句, 采用模糊检索
            sql = "select * from tab_emp where name like '%%%s%%';" % empName

            self.cur.execute(sql)
            results = self.cur.fetchall()

            for row in results:
                emp = self.__mapToEmp(row)

                # 加入列表
                empList.append(emp)
            return empList
        except Exception as e:
            print(e)
            return empList
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)

    # 向数据表中插入一条记录
    def addEmp(self, emp):
        empid = emp.get_empid()
        name = emp.get_name()
        password = emp.get_password()
        gender = emp.get_gender()
        phone = emp.get_phone()
        deptid = emp.get_deptid()
        postid = emp.get_postid()
        syslevel = emp.get_syslevel()

        try:
            # 定义sql语句, 采用模糊检索
            sql = "insert into tab_emp values ('%s', '%s', '%s', '%s', '%s', %d, %d, %d);" % (empid, name, password, gender, phone, deptid, postid, syslevel)

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

            # 更新tab_dept中的一条记录

    # 更新tab_emp中的一条记录
    def updateEmp(self, emp):
        empid = emp.get_empid()
        name = emp.get_name()
        password = emp.get_password()
        gender = emp.get_gender()
        phone = emp.get_phone()
        deptid = emp.get_deptid()
        postid = emp.get_postid()
        syslevel = emp.get_syslevel()

        try:
            # 定义sql语句, 采用模糊检索
            sql = "update tab_emp set name='%s', password='%s', gender='%s', phone='%s', deptid=%d," \
                   "postid=%d, syslevel=%d where empid='%s';" % (name, password, gender, phone, deptid, postid, syslevel, empid)

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


    # 删除tab_emp中的一条记录
    def deleteEmpByEmpid(self, empid):
        try:
            # 定义sql语句, 采用模糊检索
            sql = "delete from tab_emp where empid='%s';" %empid

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

    # 根据检索条件来模糊检索emp信息
    def findEmpByQueryField(self, queryInfo, index):
        # 基准的SQL语句
        baseSQL = """
                    SELECT 
                        e.empid, e.name, e.password, e.gender, e.phone, d.deptname, p.postname, e.syslevel
                    FROM 
                        tab_emp e , tab_dept d, tab_post p
                    WHERE 
                        e.deptid = d.deptid AND e.postid = p.postid AND """

        if index == 0: # 根据部门名称进行模糊查询
            sql = baseSQL + " d.deptname LIKE '%%%s%%';" % queryInfo
        elif index == 1:
            sql = baseSQL + " p.postname LIKE '%%%s%%';" % queryInfo
        elif index == 2:
            sql = baseSQL +" e.name LIKE '%%%s%%';" % queryInfo
        elif index == 3:
            sql = baseSQL +" e.empid='%s';" % queryInfo
        elif index == 4:
            sql = baseSQL +" e.phone LIKE '%%%s%%';" % queryInfo

        # 检索返回emp列表
        empList = []

        try:
            self.cur.execute(sql)
            results = self.cur.fetchall()

            for row in results:
                emp = self.__mapToEmp(row)

                # 加入列表
                empList.append(emp)
            return empList
        except Exception as e:
            print(e)
            return empList
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)

    # 根据姓名列表中的每个姓名检索对应的empid,返回姓名：id的词典
    def findEmpidListByNameList(self, nameList):
        empname2id_dict = {}

        for name in nameList:
            try:
                sql = "select empid from tab_emp where name='%s'"%name
                self.cur.execute(sql)
                results = self.cur.fetchall()

                empname2id_dict[name] = results[0][0]
            except Exception as e:
                empname2id_dict[name] = 0 # 未检索到此人的姓名则置返回的id为0

        # 手动关闭数据库连接
        DbUtil.close(self.conn, self.cur)
        return empname2id_dict



    # 将从数据库中检索出的所有对象的一行信息封装为一个emp对象
    def __mapToEmp(self, row):
        empid = row[0]
        empname = row[1]
        password = row[2]
        gender = row[3]
        phone = row[4]
        deptid = row[5]
        postid = row[6]
        syslevel = row[7]

        # 创建emp对象
        emp = Emp(empid, empname, password, gender, phone, deptid, postid, syslevel)

        return emp

