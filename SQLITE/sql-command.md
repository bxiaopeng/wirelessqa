

SQLite 入门教程（一）基本控制台（终端）命令

http://www.cnblogs.com/myqiao/archive/2011/07/10/2102465.html

SQLite 入门教程（二）创建、修改、删除表

http://www.cnblogs.com/myqiao/archive/2011/07/12/2103527.html

SQLite 入门教程（三）好多约束 Constraints

http://www.cnblogs.com/myqiao/archive/2011/07/13/2105550.html

SQLite 入门教程（四）增删改查，有讲究

http://www.cnblogs.com/myqiao/archive/2011/07/13/2105800.html

### sqlite3下载地址:
http://www.sqlite.org/download.html

###  配置环境变量
```
bixiaopeng@bixiaopeng ~$ vim .bash_profile
bixiaopeng@bixiaopeng ~$ source .bash_profile
bixiaopeng@bixiaopeng ~$ sqlite3
SQLite version 3.7.13 2012-07-17 17:46:21
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .quit

```

### 显示帮助

```
sqlite> .help
.backup ?DB? FILE      Backup DB (default "main") to FILE
.bail ON|OFF           Stop after hitting an error.  Default OFF
.databases             List names and files of attached databases
.dump ?TABLE? ...      Dump the database in an SQL text format
                         If TABLE specified, only dump tables matching
                         LIKE pattern TABLE.
.echo ON|OFF           Turn command echo on or off
.exit                  Exit this program
.explain ?ON|OFF?      Turn output mode suitable for EXPLAIN on or off.
                         With no args, it turns EXPLAIN on.
.header(s) ON|OFF      Turn display of headers on or off
.help                  Show this message
.import FILE TABLE     Import data from FILE into TABLE
.indices ?TABLE?       Show names of all indices
                         If TABLE specified, only show indices for tables
                         matching LIKE pattern TABLE.
.log FILE|off          Turn logging on or off.  FILE can be stderr/stdout
.mode MODE ?TABLE?     Set output mode where MODE is one of:
                         csv      Comma-separated values
                         column   Left-aligned columns.  (See .width)
                         html     HTML <table> code
                         insert   SQL insert statements for TABLE
                         line     One value per line
                         list     Values delimited by .separator string
                         tabs     Tab-separated values
                         tcl      TCL list elements
.nullvalue STRING      Print STRING in place of NULL values
.output FILENAME       Send output to FILENAME
.output stdout         Send output to the screen
.prompt MAIN CONTINUE  Replace the standard prompts
.quit                  Exit this program
.read FILENAME         Execute SQL in FILENAME
.restore ?DB? FILE     Restore content of DB (default "main") from FILE
.schema ?TABLE?        Show the CREATE statements
                         If TABLE specified, only show tables matching
                         LIKE pattern TABLE.
.separator STRING      Change separator used by output mode and .import
.show                  Show the current values for various settings
.stats ON|OFF          Turn stats on or off
.tables ?TABLE?        List names of tables
                         If TABLE specified, only list tables matching
                         LIKE pattern TABLE.
.timeout MS            Try opening locked tables for MS milliseconds
.trace FILE|off        Output each SQL statement as it is run
.vfsname ?AUX?         Print the name of the VFS stack
.width NUM1 NUM2 ...   Set column widths for "column" mode
.timer ON|OFF          Turn the CPU timer measurement on or off
sqlite>
```
** 下面内容转自：http://jianlee.ylinux.org/Computer/Server/sqlite.html**

# 创建数据库
### 创建数据库就是创建一个 SQLite 文件。

```
# 当前目录下如果有 test.db ，那么就读取这个文件，否则创建。
bixiaopeng@bixiaopeng ~$ sqlite3 test.db
SQLite version 3.7.13 2012-07-17 17:46:21
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> create table mytable(name varchar (40), age smallint);
sqlite> insert into mytable values ('Jian Lee',23);
sqlite>  select * from mytable;
Jian Lee|23
sqlite>
```
** 上面简单使用几个 SQL 命令创建一个表，并插入一条记录，最后查看创建的表内 容。使用 .help 可以列出帮助信息。 .quit 可以退出**

### 显示数据库

```
sqlite> .databases
seq  name             file
---  ---------------  ----------------------------------------------------------
0    main             /Users/bixiaopeng/test.db
```

### 显示表
```
sqlite> .tables
mytable
```

# SQL 指令简介
** 所有的 SQL 指令都以 ";" 号结尾。 ”- -“ 表示注释。**

### 创建 table，插入记录

```
sqlite> create table 数据库 (名字, 嵌入式);
sqlite> insert into 数据库 values ('PostgreSQL','否');
sqlite> insert into 数据库 values ('MySQL','否');
sqlite> insert into 数据库 values ('SQLite','是');
ssqlite> select * from 数据库;
PostgreSQL|否
MySQL|否
SQLite|是
```

** insert into 命令中不存在的字段可以用 NULL 代替。**

** 瞧，优秀的程序设计的多么好！任何”字符串“都只是一个”标签“，所以都能完美支持！**

### 建立索引

** 创建索引可以加快访问速度。**

```
sqlite> create index 数据库名字索引 on 数据库 (名字);
```

## 查询

## 更新或修改/删除

### 更新

```
sqlite> select * from 数据库;
PostgreSQL|否
MySQL|否
SQLite|是
sqlite> update 数据库 set 名字='SQLite3' where 名字='SQLite';
sqlite> select * from 数据库;
PostgreSQL|否
MySQL|否
SQLite3|是
```
### 删除
```
sqlite> select * from 数据库;
PostgreSQL|否
MySQL|否
SQLite3|是
sqlite> delete from 数据库 where 嵌入式='是';
sqlite> select * from 数据库;
PostgreSQL|否
MySQL|否
```

# SQLite 的特别用法

### 修改 sqlite3 的默认分隔符（｜）
```
sqlite> .separator "-"
```
### shell 下访问

```
# sqlite3 test.db "select * from 数据库;"
PostgreSQL|否
MySQL|否
```

如果要执行多条 sql 语句，可以先生成这样的sql语句文件，比如 “sql.txt”：

```
.output Somefile    // 这句话告诉sqlite把sql执行的结果输出到文件
create tab ...        // 正常的sql语句
insert into ....
.quit                // 告诉sqlite退出
```

然后， “cat sql.txt	sqlite data.db”。sqlite就会执行sql.txt中的sql语
句，并把结果保存到Somefile中。

### 输出 HTML 表格

```
root@jianlee:~/lab/xml/crepo/test# sqlite3 -html test.db "select * from 数据库;"
<TR><TD>PostgreSQL</TD>
<TD>否</TD>
</TR>
<TR><TD>MySQL</TD>
<TD>否</TD>
</TR>
```
### 将数据库倒出来（输出 SQL 指令）

```
root@jianlee:~/lab/xml/crepo/test# sqlite3 test.db ".dump"  > test.sql
root@jianlee:~/lab/xml/crepo/test# cat test.sql
BEGIN TRANSACTION;
CREATE TABLE mytable(name varchar (40), age smallint);
INSERT INTO "mytable" VALUES('Jian Lee',23);
CREATE TABLE 操作系统 (title, length, year, starring);
INSERT INTO "操作系统" VALUES('Jian Lee',23,33,45);
CREATE TABLE 数据库 (名字, 嵌入式);
INSERT INTO "数据库" VALUES('PostgreSQL','否');
INSERT INTO "数据库" VALUES('MySQL','否');
CREATE INDEX 数据库名字索引 on 数据库 (名字);
COMMIT;
```

在大量插入资料时，你可能会需要先打这个指令：

```
begin;
```
插入完资料后要记得打这个指令，资料才会写进数据库中：

```
commit;
```
begin; 和 commit; 是 SQL 处理一个事务的语法。

### 数据表结构

SQLite 数据库的数据结构保存在 "sqlite_master" 表中，下例针对 rpm 的 yum 源里的 repodata 目录中的 other.sqlite.bz2 数据库进行查询：

```
# sqlite3 other.sqlite
SQLite version 3.5.9
Enter ".help" for instructions
sqlite> select * from sqlite_master;
table|db_info|db_info|2|CREATE TABLE db_info (dbversion INTEGER, checksum TEXT)
table|packages|packages|3|CREATE TABLE packages (  pkgKey INTEGER PRIMARY KEY,  pkgId TEXT)
table|changelog|changelog|4|CREATE TABLE changelog (  pkgKey INTEGER,  author TEXT,  date INTEGER,  changelog TEXT)
index|keychange|changelog|5|CREATE INDEX keychange ON changelog (pkgKey)
index|pkgId|packages|6|CREATE INDEX pkgId ON packages (pkgId)
trigger|remove_changelogs|packages|0|CREATE TRIGGER remove_changelogs AFTER DELETE ON packages  BEGIN    DELETE FROM changelog WHERE pkgKey = old.pkgKey;  END sqlite>
```

但是你不能够对sqlite_master 表执行 DROP TABLE, UPDATE, INSERT or DELETE ，当你创建或者删除表的时候，sqlite_master 表会自动更新。你不能手 工改变 sqlite_master 表。

临时表的结构不会存贮到 sqlite_master 表中，临时表是存贮在另一个特殊的 表，叫做 "sqlite_temp_master"。"sqlite_temp_master" 表本身就是临时的。

### 将结果写到文件中

取自参考资料2的示例，我现在还用不到：

默认情况下，sqlite3会将结果发送到标准输出，你可以使用 ".output" 来改 变，只是将输出到的文件名作为参数传递给 .output，所有后面的查询结果都会 写到文件里。开头使用 ".output stdout" 会再次写到标准输出，例如：

    sqlite> .mode list
    sqlite> .separator |
    sqlite> .output test_file_1.txt
    sqlite> select * from tbl1;
    sqlite> .exit
    $ cat test_file_1.txt
    hello|10
    goodbye|20
    $

### 查询数据库结构

#### 列出所有数据表 (.tables)

```
sqlite> .tables
changelog  db_info    packages
sqlite>
```
".tables" 命令和一下的查询相似：

    SELECT name FROM sqlite_master
    WHERE type IN ('table','view') AND name NOT LIKE 'sqlite_%'
    UNION ALL
    SELECT name FROM sqlite_temp_master
    WHERE type IN ('table','view')
    ORDER BY 1

#### 列出特殊表的索引 (.indices)

".indices" 命令以相似的方法列出一个特殊表的索引。".indices" 命令以一个 数据表的名字作为参数。

#### .schema

不带参数的 .schema 命令会显示用来创建数据库的 “CREATE TABLE and CREATE INDEX” 语句，如果你给一个表名为参数，他会显示用来创建表和索引（如果有的 话）的 CREATE 语句。

```
sqlite> .schema
CREATE TABLE changelog (  pkgKey INTEGER,  author TEXT,  date INTEGER,  changelog TEXT);
CREATE TABLE db_info (dbversion INTEGER, checksum TEXT);
CREATE TABLE packages (  pkgKey INTEGER PRIMARY KEY,  pkgId TEXT);
CREATE INDEX keychange ON changelog (pkgKey);
CREATE INDEX pkgId ON packages (pkgId);
CREATE TRIGGER remove_changelogs AFTER DELETE ON packages  BEGIN    DELETE FROM changelog WHERE pkgKey = old.pkgKey;  END;
schema>
sqlite> .schema changelog
CREATE TABLE changelog (  pkgKey INTEGER,  author TEXT,  date INTEGER,  changelog TEXT);
CREATE INDEX keychange ON changelog (pkgKey);
```

# 常用命令
```
.databases 列出数据库文件名
.tables ?PATTERN? 列出?PATTERN?匹配的表名
.import FILE TABLE 将文件中的数据导入的文件中
.dump ?TABLE? 生成形成数据库表的SQL脚本
.output FILENAME 将输出导入到指定的文件中
.output stdout 将输出打印到屏幕
.mode MODE ?TABLE?     设置数据输出模式(csv,html,tcl…
.nullvalue STRING 用指定的串代替输出的NULL串
.read FILENAME 执行指定文件中的SQL语句
.schema ?TABLE? 打印创建数据库表的SQL语句
.separator STRING 用指定的字符串代替字段分隔符,这个很有用！
.show 打印所有SQLite环境变量的设置
.quit 退出命令行接口
```

# SQLite 结构分析

每一个 SQLite 数据库都有一个叫 SQLITE_MASTER 的表， 它定义数据库的模式。 SQLITE_MASTER 表看起来如下：

```
CREATE TABLE sqlite_master (
      type TEXT,
      name TEXT,
      tbl_name TEXT,
      rootpage INTEGER,
      sql TEXT
);
```

对于表来说，type 字段永远是 'table'，name 字段永远是表的名字。所以，要 获得数据库中所有表的列表， 使用下列SELECT语句：

```
SELECT name FROM sqlite_master
WHERE type='table'
ORDER BY name;
```
对于索引，type 等于 'index', name 则是索引的名字，tbl_name 是该索引所属 的表的名字。 不管是表还是索引，sql 字段是原先用 CREATE TABLE 或 CREATE INDEX 语句创建它们时的命令文本。对于自动创建的索引（用来实现 PRIMARY KEY 或 UNIQUE 约束），sql字段为NULL。

SQLITE_MASTER 表是只读的。不能对它使用 UPDATE、INSERT 或 DELETE。 它会 被 CREATE TABLE、CREATE INDEX、DROP TABLE 和 DROP INDEX 命令自动更新。

临时表不会出现在 SQLITE_MASTER 表中。临时表及其索引和触发器存放在另外一 个叫 SQLITE_TEMP_MASTER 的表中。SQLITE_TEMP_MASTER 跟 SQLITE_MASTER 差 不多，但它只是对于创建那些临时表的应用可见。如果要获得所有表的列表， 不 管是永久的还是临时的，可以使用类似下面的命令：

```
SELECT name FROM
    (SELECT * FROM sqlite_master UNION ALL
     SELECT * FROM sqlite_temp_master)
WHERE type='table'
    ORDER BY name
```
# 触发器

假设"customers"表存储了客户信息，"orders"表存储了订单信息，下面的触发器 确保当用户改变地址时所有的 关联订单地址均进行相应改变：

```
CREATE TRIGGER update_customer_address UPDATE OF address ON customers
  BEGIN
    UPDATE orders SET address = new.address WHERE customer_name = old.name;
  END;
```
定义了该触发器后执行如下语句：

```
UPDATE customers SET address = '1 Main St.' WHERE name = 'Jack Jones';
```
会使下面的语句自动执行：

```
UPDATE orders SET address = '1 Main St.' WHERE customer_name = 'Jack Jones';
```
注意，目前在有INTEGER PRIMARY KEY域的表上触发器可能工作不正常。若 BEFORE触发器修改了一行的 INTEGER PRIMARY KEY域，而该域将由触发该触发器 的语句进行修改，则可能根本不会修改该域。 可以用PRIMARY KEY字段代替 INTEGER PRIMARY KEY字段来解决上述问题。

再举 1 例，在 primary.sqlite.bz2 数据库中：

```
CREATE TRIGGER removals AFTER DELETE ON packages
  BEGIN
    DELETE FROM files WHERE pkgKey = old.pkgKey;
    DELETE FROM requires WHERE pkgKey = old.pkgKey;
    DELETE FROM provides WHERE pkgKey = old.pkgKey;
    DELETE FROM conflicts WHERE pkgKey = old.pkgKey;
    DELETE FROM obsoletes WHERE pkgKey = old.pkgKey;
  END;
```