#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
# filename:     sql.py
# version:      1.0.5
# description:  The APIs for sqlite3.
# first create: ppxxyy1110
# history:
#       2012-09-22 | 0.0.1
#                    ppxxyy1110 create
#       2012-10-01 | 1.0.0
#                    ppxxyy1110 modified
# ------------------------------------------------------------------------------

"""this is my sql kernal for sqlite3"""
import logging

import sqlite3

logging.basicConfig(level=logging.DEBUG)

class MyDB:
    """ this a database class with suply the api for database """
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.databasename = None
        self.cxn = None  #connection
        self.tables = None
    
    def get_table_value(self, tablename):
        """here is a value"""
        cur = self.cxn.cursor()
        cur.execute("select * from %s" % tablename)
        result = cur.fetchall()
        cur.close()
        return result
    
    def connect_db(self, databasename):
        """create a connect to database
        """
        self.databasename = databasename
        self.logger.debug("opening database %s" % (self.databasename))
        try:
            self.cxn = sqlite3.connect(self.databasename)
        except IOError:
            self.logger.error('could not open database file')
        else:
            self.logger.info('open database sucess')
    
        self.tables = self.gettables()
        
    def close_db(self):
        pass
    
    def gettables(self):
        """get all the tables for on the current opened database"""
        self.logger.debug( "cxn = %s" % self.cxn)
        cur = self.cxn.cursor()
        cur.execute("select name from sqlite_master where type='table'")
        tmp = cur.fetchall()
        cur.close()
        result = []
        for item in tmp:
            result.append(item[0])
        return result
    
    def addatable(self, newtable, cols):
        """add a table to the database
            newtable----new table name
            cols--- dictionary as colname:coltype
        """
        cur = self.cxn.cursor()
        fields = ""
        for item in cols.items():
            if len(fields) > 0:
                fields = "%s,%s %s" % (fields, item[0], item[1])
            else:
                fields = "%s %s" % (item[0], item[1])
        statment = "CREATE TABLE %s (%s)" % (newtable, fields)
        self.logger.debug("statement = %s" % statment)
        cur.execute(statment)
        cur.close()
    
    def deleteatable(self, tblname):
        """delete a table from database"""
        statement = "DROP TABLE %s" % tblname
        cur = self.cxn.cursor()
        cur.execute(statement)
        cur.close()
        
    def renametablename(self, oldname, newname):
        """renname a table"""
        statement = 'ALTER TABLE %s RENAME TO %s' % (oldname, newname)
        cur = self.cxn.cursor()
        cur.execute(statement)
        cur.close()
    
    def additem(self, tblname, dic):
        """ add a item to table
            tblname --- table name
            dic ---- a dictionnray of colname:colvalue
        """
        tableinfo = self.gettableinfo(tblname)
        name_type = {}
        for item in tableinfo:
            name_type[item[1]] = item[2]
        cols = ""
        vals = ""
        
        for col in dic.keys():
            if cols == "":
                cols = col
            else:
                cols = "%s,%s" % (cols, col)
            val = ""
            if name_type[col] == 'integer' or name_type[col] == 'int':
                val = int(dic[col])
            else:
                val = "'%s'" % dic[col]
            if vals == "":
                vals = val
            else:
                vals = "%s,%s" % (vals, val)
                      
        statement = u"INSERT INTO %s (%s) VALUES (%s)" % (tblname, cols, vals) #`tuple(dic.values())`)
        self.logger.debug("statement = %s" % statement)
        cur = self.cxn.cursor()
        cur.execute(statement)
        cur.close()
        self.cxn.commit()
        
    def deleteitem(self, tblname, dic):
        """delete items from table
            dic --- a dictionary used to make where statement 
        """
#        name_type = self.gettablecoltype(tblname)
        self.logger.debug( "dic = %s" % dic)
        self.logger.debug("dic type = %s" % [(type(item),item) for item in dic.values()])
        cols = ""
        for col in dic.keys():
            if dic[col] == None:
                continue
            if type(dic[col]) == int:
                tmp = "%s = %s" % (col, dic[col])
            else:
                tmp = "%s = '%s'" % (col, dic[col])
            if cols == "":
                cols = tmp
            else:
                cols = "%s and %s" % (cols, tmp)
#        self.logger.debug( "cols = %s " % cols )
#        self.logger.debug( "dic = %s"% dic )
    
        statement = "DELETE FROM %s WHERE %s" % (tblname, cols)
        self.logger.debug( "statement = %s " % statement)
        cur = self.cxn.cursor()
        cur.execute(statement)
        cur.close()
        self.cxn.commit()
    
    def updateitem(self, tblname, dic, setdic):
        """update items from table
        dic --- a dictionary of where sub statement as colname:colvalue
        setdic --- a dictionary of set sub statement as colname:colvalue
        """
        cols = ""
        for col in dic.keys():
            if dic[col] == None:
                continue
            if type(dic[col]) == int:
                tmp = "%s = %s" % (col, dic[col])
            else:
                tmp = "%s = '%s'" % (col, dic[col])
            if cols == "":
                cols = tmp
            else:
                cols = "%s and %s" % (cols, tmp)
        self.logger.debug( "cols = %s " % cols)
        self.logger.debug( "dic = %s" % dic)
    
    
        setcols = ""
        for col in setdic.keys():
            tmp = "%s = '%s'" % (col, setdic[col])
            if setcols == "":
                setcols = tmp
            else:
                setcols = "%s ,%s" % (setcols, tmp)
        self.logger.debug( "setcols = %s " % setcols )
        self.logger.debug( "setdic = %s" % setdic)
    
        statement = "UPDATE %s SET %s WHERE %s" % (tblname, setcols, cols)
        self.logger.debug( "statement = %s" % statement)
        cur = self.cxn.cursor()
        cur.execute(statement)
        cur.close()
        self.cxn.commit()
    
    def addkey(self, tblname, colname):
        """ add a primary key to table"""
        cur = self.cxn.cursor()
        #get the table create sql statement
        cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name = '%s'" % tblname)
        create_statement = cur.fetchall()[0][0]
#        self.logger.debug( "create_statement = %s" % create_statement)
        import re
        field_statement = re.search(r"\(.*\)", create_statement).group()[1:-1] #Removed both sides of the brackets
#        self.logger.debug( "field_statement =", field_statement
#        field_list = field_statement.split(",") #re.split("[,\W]",field_statement)
#        self.logger.debug( "field_list = %s" % field_list)
        
        keyname = self.get_primary_key(tblname)
        if keyname != None:
            self.logger.error( "this table already has a key as (%s), if you must add a key, delete this key first"
                               % keyname)
            return
        #this table has no primary key
        index = field_statement.find(",", field_statement.find(colname))
        field_statement_new = ""
        if index >= 0:
            field_statement_new = "%s PRIMARY KEY %s" % (field_statement[:index], field_statement[index:])
        else:
            field_statement_new = "%s PRIMARY KEY" % field_statement

        cur.execute("CREATE TEMPORARY TABLE TEMP_TABLE (%s)" % field_statement_new)
        cur.execute("INSERT INTO TEMP_TABLE SELECT * FROM %s" % tblname)
        cur.execute("DROP TABLE %s" % tblname)
        cur.execute("CREATE TABLE %s (%s)" % (tblname, field_statement_new))
        cur.execute("INSERT INTO %s SELECT * FROM TEMP_TABLE" % tblname)
        cur.execute("DROP TABLE TEMP_TABLE")
        cur.close()
        self.cxn.commit()
    
    def deletekey(self, tblname):
        """ delete primary key from table"""
        
        cur = self.cxn.cursor()
        cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name = '%s'" % tblname)
        
        create_statement = cur.fetchall()[0][0]
#        self.logger.debug( "create_statement = %s" % create_statement)
        import re
        field_statement = re.search(r"\(.*\)", create_statement).group()[1:-1] #Removed both sides of the brackets
#        self.logger.debug( "field_statement = %s" % field_statement)
#        field_list = field_statement.split(",") #re.split("[,\W]",field_statement)
#        self.logger.debug( "field_list = %s" % field_list)
        
        keyname = self.get_primary_key(tblname)
        if keyname == None:
            self.logger.info( "this table has no key")
            return
        else:
            indexs = field_statement.upper().find('PRIMARY KEY')
            primarykey = field_statement[ indexs : indexs + len('PRIMARY KEY')]
            field_statement_new = field_statement.replace(primarykey, "")
    
            self.logger.debug( "field_statement_new = %s" % field_statement_new)
            cur.execute("CREATE TEMPORARY TABLE TEMP_TABLE (%s)" % field_statement_new)
            cur.execute("INSERT INTO TEMP_TABLE SELECT * FROM %s" % tblname)
            cur.execute("DROP TABLE %s" % tblname)
            cur.execute("CREATE TABLE %s (%s)" % (tblname, field_statement_new))
            cur.execute("INSERT INTO %s SELECT * FROM TEMP_TABLE" % tblname)
            cur.execute("DROP TABLE TEMP_TABLE")
            cur.close()
            self.cxn.commit()
    
    def gettableinfo(self, tablename):
        """get the table infomation"""
        cur = self.cxn.cursor()
        cur.execute("PRAGMA table_info(%s)" % tablename)
        info = cur.fetchall()
        self.logger.debug( "info = %s" % info)
        cur.close()
        return info

    def gettablecoltype(self, tblname):
        """ get the table's colname:coltype dictionary"""
        tableinfo = self.gettableinfo(tblname)
        name_type = {}
        for item in tableinfo:
            name_type[item[1]] = item[2]
        return name_type
    
    def get_primary_key(self, tblname):
        """detective whether table already has a primary key,
            if this table already has a primary key, return the key name
            if not return None
        """
        
        cur = self.cxn.cursor()
        #get the table create sql statement
        cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name = '%s'" % tblname)
        create_statement = cur.fetchall()[0][0]
        import re
        field_statement = re.search(r"\(.*\)", create_statement).group()[1:-1] #Removed both sides of the brackets
        field_list = field_statement.split(",") #re.split("[,\W]",field_statement)
        
        for item in field_list:
            if item.upper().find('PRIMARY KEY') >= 0:
                indexs = item.upper().find('PRIMARY KEY')
                primarykey = item[ : indexs]
                #self.logger.debug( 
                #"this table already has a key as (%s), if you must add a key, delete this key first" % item )
                return primarykey
        return None
