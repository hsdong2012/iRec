# -*- coding:utf-8 -*-
from entity.post import Post
from util.dbutil import DbUtil

# 对tb_post表进行DAO操作的类
class PostDAO(object):
    def __init__(self):
        self.conn, self.cur = DbUtil.getConnection()

    # 检索所有post信息
    def findAll(self):
        postList = []

        try:
            # 定义sql语句
            sql = "select * from tab_post;"

            self.cur.execute(sql)
            results = self.cur.fetchall()

            for row in results:
                postid = row[0]
                postname = row[1]
                postintro = row[2]

                # 创建Post对象
                post = Post(postid, postname, postintro)

                # 加入列表
                postList.append(post)

            return postList
        except Exception as e:
            print(e)
            return postList
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)


    # 根据postName模糊检索post信息
    def findPostByName(self, postName):
        postList = []

        try:
            # 定义sql语句, 采用模糊检索
            sql = "select * from tab_post where postname like '%%%s%%';"%postName

            self.cur.execute(sql)
            results = self.cur.fetchall()

            for row in results:
                postid = row[0]
                postname = row[1]
                postintro = row[2]

                # 创建taff对象
                post = Post(postid, postname, postintro)

                # 加入列表
                postList.append(post)

            return postList
        except Exception as e:
            print(e)
            return postList
        finally:
            # 关闭数据库连接
            DbUtil.close(self.conn, self.cur)

    # 向数据表中插入一条记录
    def addPost(self, postName, postIntro):
        try:
            # 定义sql语句, 插入记录
            sql = "insert into tab_post(postname, postintro) values ('%s', '%s');" % (postName, postIntro)

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

    # 更新tab_post中的一条记录
    def updatePost(self, post):
        try:
            # 定义sql语句, 采用模糊检索
            sql = "update tab_post set postname='%s', postintro='%s' where postid='%s';" % (post.get_postname(), post.get_postintro(), post.get_postid())

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


    # 删除tab_post中的一条记录
    def deletePostByPostid(self, postid):
        try:
            # 定义sql语句, 采用模糊检索
            sql = "delete from tab_post where postid='%s';" % (postid)

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



