#!/usr/bin/env python
# ------------------------------------------------------------------------------
#
# filename:     sql_char.py
# version:      1.0.5
# description:  The Command User Interface for sqlite3.
# first create: ppxxyy1110
# history:
#       2012-10-01 | 0.0.1
#                    ppxxyy1110 create
# ------------------------------------------------------------------------------

"""this a sql char interface"""
from wxPython.实例收藏.sqlite3数据库的gui界面 import sql

ERRORMSG = 'please enter a correct cmd, you can enter help'
DATA_BASE = sql.MyDB()

def shell_show():
    """ show all tables"""
    ret = DATA_BASE.gettables()
    print ret

def shell_table():
    """in this shell you can add,delete,rename a table"""
    msgs = {'add':'add--- add a table',
            'delete':'delete--- delete a table',
            'rename':'rename--- rename a table',
            'r':'r--- return to up level menu',
            'exit':'exit --- exit'
    }
    
    funs = {'add':'add_a_table()',
           'delete':'delete_a_table()',
           'rename':'rename_a_table()',
           'r':'return',
           'exit':'exit()',
           
           'help':'myhelp()'
           }
    
    def myhelp():
        """get help info"""
        print "%" + ("="*40) + "%"
        for msg in msgs.values():
            print msg
        print "%" + ("="*40) + "%"
        
    myhelp()
    cmd = raw_input("sqlite/table>>")
    while True:
        if cmd not in funs.keys():
            print ERRORMSG
        else:
            eval(funs[cmd])
        cmd = raw_input("sqlite/table>>")
            
def shell_item():
    """in this shell you can add,delete,update a item from a table"""
    msgs = {'add':'add--- add a item',
            'delete':'delete--- delete a item',
            'update':'update--- update a item',
            'r':'r--- return to up level menu',
            'exit':'exit --- exit'
            }
    funs = {'add':'add_a_item()',
           'delete':'delete_a_item()',
           'rename':'update_a_item()',
           'exit':'exit()',
           'help':'myhelp()'
           }
    
    def myhelp():
        """get help info"""
        print "%" + ("="*40) + "%"
        for msg in msgs.values():
            print msg
        print "%" + ("="*40) + "%"
        
    myhelp()
    cmd = raw_input("sqlite/item>>")
    while True:
        if cmd not in funs.keys():
            print ERRORMSG
        else:
            eval(funs[cmd])
        cmd = raw_input("sqlite/item>>")

def shell_key():
    """in this shell you can add,delete a key from a table"""
    msgs = {'add':'add--- add primary key',
            'delete':'delete--- delete primary key',
            'r':'r--- return to up level menu',
            'exit':'exit --- exit'
            }
    funs = {'add':'add_primary_key()',
           'delete':'delete_primary_key()',
           'exit':'exit()',
           'help':'myhelp()'
           }
    
    def myhelp():
        """get help info"""
        print "%" + ("="*40) + "%"
        for msg in msgs.values():
            print msg
        print "%" + ("="*40) + "%"
        
    myhelp()
    cmd = raw_input("sqlite/key>>")
    while True:
        if cmd not in funs.keys():
            print ERRORMSG
        else:
            eval(funs[cmd])
        cmd = raw_input("sqlite/key>>")
    
    
def add_a_table():
    """this function allow you add a table to current database"""
    newtable = raw_input('please input the new table name')
    newtable = newtable.strip()
    cols = {}
    print 'please input fieldname and type, if no more field, just input end'
    while True:
        text = raw_input('format filename,type or "end": ')
        if text == "end":
            break
        else:
            tmp = text.strip().split(":")
            cols[tmp[0]] = tmp[1]
    DATA_BASE.addatable(newtable, cols)
    
def delete_a_table():
    """this function allow you delete a table from database"""
    tblname = raw_input('please input the table name you want to delete')
    tblname = tblname.strip()
    DATA_BASE.deleteatable(tblname)
    
def rename_a_table():
    """rename a table"""
    oldname = raw_input('please input the old table name: ')
    newname = raw_input('please input the new table name: ')
    DATA_BASE.renametablename(oldname, newname)
    
def add_a_item():
    """insert a row or item to a table"""
    tblname = raw_input('please input the tablename: ')
    tableinfo = DATA_BASE.gettableinfo(tblname)
    colname = [tp[1] for tp in tableinfo]
    coltype = [tp[2] for tp in tableinfo]
    print zip(colname, coltype)
    dic = {}
    i = 0
    for col in colname:
        val = raw_input("please input the value of %s, if no value just input 'None': " % col)
        if val != 'None':
            if coltype[i] == 'integer':
                dic[col] = int(val)
            else:
                dic[col] = val
        i = i + 1
    DATA_BASE.additem(tblname, dic)

def delete_a_item():
    """delete a row or a item"""
    tblname = raw_input('please input the tablename: ')
    tableinfo = DATA_BASE.gettableinfo(tblname)
    colname = [tp[1] for tp in tableinfo]
    coltype = [tp[2] for tp in tableinfo]
    print zip(colname, coltype)
    dic = {}
    i = 0
    for col in colname:
        val = raw_input("please input the value of %s, if no value just input 'None'" % col)
        if val != 'None':
            if coltype[i] == 'integer' or coltype[i] == 'int':
                dic[col] = int(val)
            else:
                dic[col] = val
        i += 1
    DATA_BASE.deleteitem(tblname, dic)

def update_a_item():
    """update a row or a item"""
    tblname = raw_input('please input the tablename: ')
    tableinfo = DATA_BASE.gettableinfo(tblname)
    colname = [tp[1] for tp in tableinfo]
    coltype = [tp[2] for tp in tableinfo]
    print zip(colname, coltype)
    print "please input the where"
    dic = {}
    i = 0
    for col in colname:
        val = raw_input("please input the value of %s, if no value just input 'None': " % col)
        if val != 'None':
            if coltype[i] == 'integer':
                dic[col] = int(val)
            else:
                dic[col] = val
        i = i + 1
    #make set
    print "please input the set statement"
    setdic = {}
    i = 0
    for col in colname:
        val = raw_input("please input the value of %s, if no value just input 'None': " % col)
        if val != 'None':
            if coltype[i] == 'integer':
                setdic[col] = int(val)
            else:
                setdic[col] = val
        i = i + 1
    DATA_BASE.updateitem(tblname, dic, setdic)
    
def add_primary_key():
    """add a primary key to table"""
    tblname = raw_input('please input the tablename: ')
    tableinfo = DATA_BASE.gettableinfo(tblname)
    colname = [tp[1] for tp in tableinfo]
    coltype = [tp[2] for tp in tableinfo]
    print zip(colname, coltype)
    
    keyname = DATA_BASE.get_primary_key(tblname)
    if keyname != None:
        print "table %s already has a key as '%s', if you must add a key, delete this key first" \
        % (tblname, keyname)
    else:
        colname = raw_input("Enter the fieldname as a primary key: ")
        DATA_BASE.addkey(tblname, colname)
        
def delete_primary_key():
    """delete a primary key from a table"""
    tblname = raw_input('please input the tablename: ')
    tableinfo = DATA_BASE.gettableinfo(tblname)
    colname = [tp[1] for tp in tableinfo]
    coltype = [tp[2] for tp in tableinfo]
    print zip(colname, coltype)
    DATA_BASE.deletekey(tblname)
    
    
def shell_top():
    """if this module run as top module this method would be called"""
    import sys
    database = DATA_BASE
    if len(sys.argv) < 2:
        dbname = raw_input("Enter a database name: ")
    else:
        dbname = sys.argv[1]
    database.connect_db(dbname)

    msgs = {'show':'show --- show all tables',
            'table':'table --- add,delete,rename a table',
            'item':'item --- add,delete,update a item in a table',
            'key':'key --- add,delete a key',
            'exit':'exit --- exit'
            }
    
    funs = {'show':'shell_show()',
           'table':'shell_table()',
           'item':'shell_item()',
           'key':'shell_key()',
           'exit':'exit()',
           'help':'myhelp()'
           }
    
    def myhelp():
        """get help info"""
        print "%" + ("="*40) + "%"
        for msg in msgs.values():
            print msg
        print "%" + ("="*40) + "%"
        
    myhelp()
    
    while True:
        cmd = raw_input("sqlite>>")
        if cmd not in funs.keys():
            print ERRORMSG
        else:
            eval(funs[cmd])



if __name__ == "__main__":
    
    shell_top()
