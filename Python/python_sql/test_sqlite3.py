#!/usr/bin/python
# -*- coding:utf-8 -*- 
#---------------------------------------------------------------------------
#  File:         test_sqlite3.py
#  Description:  
#
#  Date:         14/12/1 上午10:50
#  Author:       bixiaopeng
#  Tags:         
#---------------------------------------------------------------------------
import sqlite3
import os
import sys
import logging
#################################################################################################
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='',
                    filemode='w')
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
# console.setFormatter(formatter)
# logging.getLogger('').addHandler(console)
#################################################################################################

'''SQLite数据库是一款非常小巧的嵌入式开源数据库软件，也就是说
没有独立的维护进程，所有的维护都来自于程序本身。
在python中，使用sqlite3创建数据库的连接，当我们指定的数据库文件不存在的时候
连接对象会自动创建数据库文件；如果数据库文件已经存在，则连接对象不会再创建
数据库文件，而是直接打开该数据库文件。
    连接对象可以是硬盘上面的数据库文件，也可以是建立在内存中的，在内存中的数据库
    执行完任何操作后，都不需要提交事务的(commit)

    创建在硬盘上面： conn = sqlite3.connect('c:\\test\\test.db')
    创建在内存上面： conn = sqlite3.connect('"memory:')

    下面我们一硬盘上面创建数据库文件为例来具体说明：
    conn = sqlite3.connect('c:\\test\\hongten.db')
    其中conn对象是数据库链接对象，而对于数据库链接对象来说，具有以下操作：

        commit()            --事务提交
        rollback()          --事务回滚
        close()             --关闭一个数据库链接
        cursor()            --创建一个游标

    cu = conn.cursor()
    这样我们就创建了一个游标对象：cu
    在sqlite3中，所有sql语句的执行都要在游标对象的参与下完成
    对于游标对象cu，具有以下具体操作：

        execute()           --执行一条sql语句
        executemany()       --执行多条sql语句
        close()             --游标关闭
        fetchone()          --从结果中取出一条记录
        fetchmany()         --从结果中取出多条记录
        fetchall()          --从结果中取出所有记录
        scroll()            --游标滚动

'''

SHOW_SQL = True

class SqliteUtils:
    """
    基础数据库操作
    """
    def __init__(self, db_path):
        self.db = db_path
        self.logger = logging.getLogger(self.__class__.__name__)

    def get_conn(self):
        """
        获取到数据库的连接对象，参数为数据库文件的绝对路径
        如果传递的参数是存在，并且是文件，那么就返回硬盘上面改
        路径下的数据库文件的连接对象；否则，返回内存中的数据接
        连接对象
        :param path: 数据库文件的绝对路径
        :return:
        """
        conn = sqlite3.connect(self.db)
        if os.path.exists(self.db) and os.path.isfile(self.db):
            self.logger.info(u"获取硬盘上数据库的连接对象: %s" %self.db)
            return conn
        else:
            conn = None
            self.logger.info(u'内存上面:[:memory:]')
            return sqlite3.connect(':memory:')

    def get_cursor(self, conn):
        """
        该方法是获取数据库的游标对象，参数为数据库的连接对象
        如果数据库的连接对象不为None，则返回数据库连接对象所创
        建的游标对象；否则返回一个游标对象，该对象是内存中数据
        库连接对象所创建的游标对象
        :param conn:
        :return:
        """
        if conn is not None:
            self.logger.info(u"获得数据库游标")
            return conn.cursor()
        else:
            return self.get_conn().cursor()

    ###############################################################
    ####            创建|删除表操作     START
    ###############################################################

    def drop_table(self, conn, table):
        """
        如果表存在,则删除表，如果表中存在数据的时候，使用该
        方法的时候要慎用！
        :param conn:
        :param table:
        :return:
        """
        sql = None
        if table is not None and table != '':
            sql = 'DROP TABLE IF EXISTS ' + table
            if SHOW_SQL:
                self.logger.info(u'执行sql:[{}]'.format(sql))
            cu = self.get_cursor(conn)
            cu.execute(sql)
            conn.commit()
            self.logger.info(u'删除数据库表[{}]成功!'.format(table))
            self.close_all(conn, cu)
        else:
            print 'the [{}] is empty or equal None!'.format(sql)

    def create_table(self, conn, sql):
        """
        创建数据库表：student
        :param conn:
        :param sql:
        :return:
        """
        if sql is not None and sql != '':
            cu = self.get_cursor(conn)
            if SHOW_SQL:
                self.logger.info(u'执行sql:[{}]'.format(sql))
            cu.execute(sql)
            #提交事务
            conn.commit()
            self.logger.info(u'创建数据库表[student]成功!')
            self.close_all(conn, cu)
        else:
            self.logger.info('the [{}] is empty or equal None!'.format(sql))

    ###############################################################
    ####            创建|删除表操作     END
    ###############################################################

    def close_all(self, conn, cu):
        """
        关闭数据库游标对象和数据库连接对象
        :param conn:
        :param cu:
        :return:
        """
        self.logger.info(u"关闭数据库游标对象和数据库连接对象")
        try:
            if cu is not None:
                cu.close()
        finally:
            if cu is not None:
                cu.close()

    ###############################################################
    ####            数据库操作CRUD     START
    ###############################################################

    def save(self, conn, sql, data):
        """
        插入数据
        :param conn:
        :param sql:
        :param data:
        :return:
        """
        self.logger.info(u"准备插入数据")
        if sql is not None and sql != '':
            if data is not None:
                cu = self.get_cursor(conn)
                for d in data:
                    if SHOW_SQL:
                        self.logger.info(u'执行sql:[{}],参数:[{}]'.format(sql, d))
                    cu.execute(sql, d)
                    conn.commit()
                self.close_all(conn, cu)
        else:
            self.logger.info('the %s is empty or equal None!'.format(sql))

    def fetchall(self, conn, sql):
        """
        查询所有数据
        :param conn:
        :param sql:
        :return:
        """
        self.logger.info(u"查询所有数据")
        if sql is not None and sql != '':
            cu = self.get_cursor(conn)
            if SHOW_SQL:
                self.logger.info(u'执行sql:%s'.format(sql))
            cu.execute(sql)
            r = cu.fetchall()
            if len(r) > 0:
                for e in range(len(r)):
                    self.logger.info(r[e])
        else:
            self.logger.info('the [%s] is empty or equal None!'.format(sql))

    def fetchone(self, conn, sql, data):
        """
        查询一条数据
        :param conn:
        :param sql:
        :param data:
        :return:
        """

        self.logger.info(u"查询一条数据")
        if sql is not None and sql != '':
            if data is not None:
                #Do this instead
                d = (data,)
                cu = self.get_cursor(conn)
                if SHOW_SQL:
                    self.logger.info(u'执行sql:[%s],参数:[%s]'.format(sql, data))
                cu.execute(sql, d)
                r = cu.fetchall()
                if len(r) > 0:
                    for e in range(len(r)):
                        self.logger.info(r[e])
            else:
                self.logger.info('the [%s] equal None!'.format(data))
        else:
            self.logger.info('the [%s] is empty or equal None!'.format(sql))

    def update(self, conn, sql, data):
        """
        更新数据
        :param conn:
        :param sql:
        :param data:
        :return:
        """
        self.logger.info(u"更新数据")
        if sql is not None and sql != '':
            if data is not None:
                cu = self.get_cursor(conn)
                for d in data:
                    if SHOW_SQL:
                        self.logger.info(u'执行sql:[{}],参数:[{}]'.format(sql, d))
                    cu.execute(sql, d)
                    conn.commit()
                self.close_all(conn, cu)
        else:
            self.logger.info('the [%s] is empty or equal None!'.format(sql))

    def delete(self, conn, sql, data):
        """
        删除数据
        :param conn:
        :param sql:
        :param data:
        :return:
        """
        self.logger.info(u"删除数据")
        if sql is not None and sql != '':
            if data is not None:
                cu = self.get_cursor(conn)
                for d in data:
                    if SHOW_SQL:
                        self.logger.info(u'执行sql:[{}],参数:[{}]'.format(sql, d))
                    cu.execute(sql, d)
                    conn.commit()
                self.close_all(conn, cu)
        else:
            self.logger.info('the [%s] is empty or equal None!'.format(sql))
###############################################################
####            数据库操作CRUD     END
###############################################################

class SqliteTest:

    def __init__(self, db_path):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.db = db_path
        self.sqlutils = SqliteUtils(self.db)
        self.conn = self.sqlutils.get_conn()
        self.table_name = "student"

    def drop_table_test(self):
        """
        删除数据库表
        """
        self.logger.info(u"===========测试删除数据库表%s" %self.table_name)
        self.sqlutils.drop_table(self.conn, self.table_name)

    def create_table_test(self):
        """
        测试创建数据库表
        """
        self.logger.info(u"===========测试创建数据库表%s" %self.table_name)
        create_table_sql = '''CREATE TABLE `student` (
                          `id` int(11) NOT NULL,
                          `name` varchar(20) NOT NULL,
                          `gender` varchar(4) DEFAULT NULL,
                          `age` int(11) DEFAULT NULL,
                          `address` varchar(200) DEFAULT NULL,
                          `phone` varchar(20) DEFAULT NULL,
                           PRIMARY KEY (`id`)
                        )'''
        self.sqlutils.create_table(self.conn, create_table_sql)

    def save_test(self):
        """
        保存数据测试
        :return:
        """
        self.logger.info(u"===========测试保存数据")
        save_sql = '''INSERT INTO student values (?, ?, ?, ?, ?, ?)'''
        data = [(1, 'Hongten', u'男', 20, u'广东省广州市', '13423****62'),
                (2, 'Tom', u'男', 22, u'美国旧金山', '15423****63'),
                (3, 'Jake', u'女', 18, u'广东省广州市', '18823****87'),
                (4, 'Cate', u'女', 21, u'广东省广州市', '14323****32')]
        self.sqlutils.save(self.conn, save_sql, data)

    def fetchall_test(self):
        """
        查询所有数据
        :return:
        """
        self.logger.info(u"===========查询所有数据")
        fetchall_sql = '''SELECT * FROM student'''
        self.sqlutils.fetchall(self.conn, fetchall_sql)

    def fetchone_test(self):
        """
        查询一条数据..
        :return:
        """
        self.logger.info(u"===========查询一条数据")
        fetchone_sql = 'SELECT * FROM student WHERE ID = ? '
        data = 1
        self.sqlutils.fetchone(self.conn, fetchone_sql, data)

    def update_test(self):
        """
        更新数据
        :return:
        """
        self.logger.info(u"===========更新数据")
        update_sql = 'UPDATE student SET name = ? WHERE ID = ? '
        data = [('HongtenAA', 1),
                ('HongtenBB', 2),
                ('HongtenCC', 3),
                ('HongtenDD', 4)]
        self.sqlutils.update(self.conn, update_sql, data)

    def delete_test(self):
        """
        删除数据
        :return:
        """
        self.logger.info(u"===========删除数据")
        delete_sql = 'DELETE FROM student WHERE NAME = ? AND ID = ? '
        data = [('HongtenAA', 1),
                ('HongtenCC', 3)]
        self.sqlutils.delete(self.conn, delete_sql, data)

def main():
    cur_dir = sys.path[0].decode("utf-8")
    db_path = '%s/wirelessqa.db' %cur_dir
    sqltest = SqliteTest(db_path)

    #前戏: 删除表、新建表、保存
    sqltest.drop_table_test()
    sqltest.create_table_test()
    sqltest.save_test()
    #开始: 查询、更新、删除
    sqltest.fetchall_test()
    sqltest.update_test()
    sqltest.fetchall_test()
    sqltest.fetchone_test()
    sqltest.delete_test()

if __name__ == '__main__':
    main()

