## SQLite是什么
SQLite是一个进程内的库，实现了自给自足的、无服务器的、零配置的、事务性的 SQL 数据库引擎。它是一个零配置的数据库，这意味着与其他数据库一样，您不需要在系统中配置。

就像其他数据库，SQLite 引擎不是一个独立的进程，可以按应用程序需求进行静态或动态连接。SQLite 直接访问其存储文件。

## 为什么要用 SQLite？
不需要一个单独的服务器进程或操作的系统（无服务器的）。

SQLite 不需要配置，这意味着不需要安装或管理。

一个完整的 SQLite 数据库是存储在一个单一的跨平台的磁盘文件。

SQLite 是非常小的，是轻量级的，完全配置时小于 400KiB，省略可选功能配置时小于250KiB。

SQLite 是自给自足的，这意味着不需要任何外部的依赖。

SQLite 事务是完全兼容 ACID 的，允许从多个进程或线程安全访问。

SQLite 支持 SQL92（SQL2）标准的大多数查询语言的功能。

SQLite 使用 ANSI-C 编写的，并提供了简单和易于使用的 API。

SQLite 可在 UNIX（Linux, Mac OS-X, Android, iOS）和 Windows（Win32, WinCE, WinRT）中运行。

## SQLite 语法

SQLite 是遵循一套独特的称为语法的规则和准则。

### 1. 大小写敏感性
有个重要的点值得注意，SQLite 是不区分大小写的，但也有一些命令是大小写敏感的，比如 GLOB 和 glob 在 SQLite 的语句中有不同的含义。

### 2. 注释
SQLite 注释是附加的注释，可以在 SQLite 代码中添加注释以增加其可读性，他们可以出现在任何空白处，包括在表达式内和其他 SQL 语句的中间，但它们不能嵌套。

SQL 注释以两个连续的 "-" 字符（ASCII 0x2d）开始，并扩展至下一个换行符（ASCII 0x0a）或直到输入结束，以先到者为准。

您也可以使用 C 风格的注释，以 "/*" 开始，并扩展至下一个 "*/" 字符对或直到输入结束，以先到者为准。C 庚哥的注释可以跨越多行。

sqlite&gt;.help -- This is a single line comment

### 3. SQLite 语句
所有的 SQLite 语句可以以任何关键字开始，如 SELECT、INSERT、UPDATE、DELETE、ALTER、DROP 等，所有的语句以分号（;）结束。

更多请参考：<http://www.w3cschool.cc/sqlite/sqlite-syntax.html>

## SQLite 数据类型

SQLite 数据类型是一个用来指定任何对象的数据类型的属性。SQLite 中的每一列，每个变量和表达式都有相关的数据类型。

您可以在创建表的同时使用这些数据类型。SQLite 使用一个更普遍的动态类型系统。在 SQLite 中，值的数据类型与值本身是相关的，而不是与它的容器相关。

### SQLite 存储类
每个存储在 SQLite 数据库中的值都具有以下存储类之一：

存储类|	描述
----|----
NULL	|值是一个 NULL 值。
INTEGER	|值是一个带符号的整数，根据值的大小存储在 1、2、3、4、6 或 8 字节中。
REAL	|值是一个浮点值，存储为 8 字节的 IEEE 浮点数字。
TEXT	|值是一个文本字符串，使用数据库编码（UTF-8、UTF-16BE 或 UTF-16LE）存储。
BLOB	|值是一个 blob 数据，完全根据它的输入存储。

SQLite 的存储类稍微比数据类型更普遍。INTEGER 存储类，例如，包含 6 种不同的不同长度的整数数据类型。

更多请参考: <http://www.w3cschool.cc/sqlite/sqlite-data-types.html>

## 环境配置

### sqlite3下载地址:

http://www.sqlite.org/download.html

### 配置环境变量

```
bixiaopeng@bixiaopeng ~$ vim .bash_profile
#SQLITE3=/Users/bixiaopeng/software/jars/sqlite3
bixiaopeng@bixiaopeng ~$ source .bash_profile
bixiaopeng@bixiaopeng ~$ sqlite3
SQLite version 3.7.13 2012-07-17 17:46:21
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .quit
```

## 基本命令

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

### 进入和退出命令行环境

```
#退出方法1: .quit
bixiaopeng@bixiaopeng ~$ sqlite3
SQLite version 3.7.13 2012-07-17 17:46:21
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .quit

#退出方法2: .exit
bixiaopeng@bixiaopeng ~$ sqlite3
SQLite version 3.7.13 2012-07-17 17:46:21
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .exit
```

## 数据库和表相关命令

### 创建一个新的数据库: sqlite3 数据库名

```
bixiaopeng@bixiaopeng SQLITE$ mkdir db && cd db && sqlite3 wiressqa.db
SQLite version 3.7.13 2012-07-17 17:46:21
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite>
```
### 打开一个已经存在的数据库: sqlite3 数据库名

```
bixiaopeng@bixiaopeng db$ sqlite3 wirelessqa.db
SQLite version 3.7.13 2012-07-17 17:46:21
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite>
```

### 导入数据: .read 数据文件

#### 准备testdata.sql文件

```
BEGIN TRANSACTION;

CREATE TABLE Cars(Id integer PRIMARY KEY, Name text, Cost integer);

INSERT INTO Cars VALUES(1,'Audi',52642);

INSERT INTO Cars VALUES(2,'Mercedes',57127);

INSERT INTO Cars VALUES(3,'Skoda',9000);

INSERT INTO Cars VALUES(4,'Volvo',29000);

INSERT INTO Cars VALUES(5,'Bentley',350000);

INSERT INTO Cars VALUES(6,'Citroen',21000);

INSERT INTO Cars VALUES(7,'Hummer',41400);

INSERT INTO Cars VALUES(8,'Volkswagen',21600);

COMMIT;

BEGIN TRANSACTION;

CREATE TABLE Orders(Id integer PRIMARY KEY, OrderPrice integer CHECK(OrderPrice>0), Customer text);

INSERT INTO Orders(OrderPrice, Customer) VALUES(1200, "Williamson");

INSERT INTO Orders(OrderPrice, Customer) VALUES(200, "Robertson");

INSERT INTO Orders(OrderPrice, Customer) VALUES(40, "Robertson");

INSERT INTO Orders(OrderPrice, Customer) VALUES(1640, "Smith");

INSERT INTO Orders(OrderPrice, Customer) VALUES(100, "Robertson");

INSERT INTO Orders(OrderPrice, Customer) VALUES(50, "Williamson");

INSERT INTO Orders(OrderPrice, Customer) VALUES(150, "Smith");

INSERT INTO Orders(OrderPrice, Customer) VALUES(250, "Smith");

INSERT INTO Orders(OrderPrice, Customer) VALUES(840, "Brown");

INSERT INTO Orders(OrderPrice, Customer) VALUES(440, "Black");

INSERT INTO Orders(OrderPrice, Customer) VALUES(20, "Brown");

COMMIT;

BEGIN TRANSACTION;

CREATE TABLE Friends(Id integer PRIMARY KEY, Name text UNIQUE NOT NULL, Sex text CHECK(Sex IN ('M', 'F')));

INSERT INTO Friends VALUES(1,'Jane', 'F');

INSERT INTO Friends VALUES(2,'Thomas', 'M');

INSERT INTO Friends VALUES(3,'Franklin', 'M');

INSERT INTO Friends VALUES(4,'Elisabeth', 'F');

INSERT INTO Friends VALUES(5,'Mary', 'F');

INSERT INTO Friends VALUES(6,'Lucy', 'F');

INSERT INTO Friends VALUES(7,'Jack', 'M');

COMMIT;

BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS Customers(CustomerId integer PRIMARY KEY, Name text);

INSERT INTO Customers(Name) VALUES('Paul Novak');

INSERT INTO Customers(Name) VALUES('Terry Neils');

INSERT INTO Customers(Name) VALUES('Jack Fonda');

INSERT INTO Customers(Name) VALUES('Tom Willis');


CREATE TABLE IF NOT EXISTS Reservations(Id integer PRIMARY KEY, CustomerId integer, Day text);

INSERT INTO Reservations(CustomerId, Day) VALUES(1, '2009-22-11');

INSERT INTO Reservations(CustomerId, Day) VALUES(2, '2009-28-11');

INSERT INTO Reservations(CustomerId, Day) VALUES(2, '2009-29-11');

INSERT INTO Reservations(CustomerId, Day) VALUES(1, '2009-29-11');

INSERT INTO Reservations(CustomerId, Day) VALUES(3, '2009-02-12');

COMMIT;

BEGIN TRANSACTION;

CREATE TABLE Names(Id integer, Name text);

INSERT INTO Names VALUES(1,'Tom');

INSERT INTO Names VALUES(2,'Lucy');

INSERT INTO Names VALUES(3,'Frank');

INSERT INTO Names VALUES(4,'Jane');

INSERT INTO Names VALUES(5,'Robert');

COMMIT;

BEGIN TRANSACTION;

CREATE TABLE Books(Id integer PRIMARY KEY, Title text, Author text, Isbn text default 'not available');

INSERT INTO Books VALUES(1,'War and Peace','Leo Tolstoy','978-0345472403');

INSERT INTO Books VALUES(2,'The Brothers Karamazov','Fyodor Dostoyevsky','978-0486437910');

INSERT INTO Books VALUES(3,'Crime and Punishment','Fyodor Dostoyevsky','978-1840224306');

COMMIT;
```
#### 读入数据

```
sqlite> .read testdata.sql
```

### 列出所有数据表: .tables

```
sqlite> .tables
Books         Customers     Names         Reservations
Cars          Friends       Orders
```
### 显示数据库结构：.schema

```
sqlite> .schema
CREATE TABLE Books(Id integer PRIMARY KEY, Title text, Author text, Isbn text default 'not available');
CREATE TABLE Cars(Id integer PRIMARY KEY, Name text, Cost integer);
CREATE TABLE Customers(CustomerId integer PRIMARY KEY, Name text);
CREATE TABLE Friends(Id integer PRIMARY KEY, Name text UNIQUE NOT NULL, Sex text CHECK(Sex IN ('M', 'F')));
CREATE TABLE Names(Id integer, Name text);
CREATE TABLE Orders(Id integer PRIMARY KEY, OrderPrice integer CHECK(OrderPrice>0), Customer text);
CREATE TABLE Reservations(Id integer PRIMARY KEY, CustomerId integer, Day text);
```

### 显示当前所有的数据库

```
bixiaopeng@bixiaopeng db$ sqlite3 wirelessqa.db ".databases"
seq  name             file
---  ---------------  ----------------------------------------------------------
0    main             /Users/bixiaopeng/workspace/source-github/wirelessqa/SQLIT
```

### 显示表的结构：.schema    表名

```
sqlite> .schema Books
CREATE TABLE Books(Id integer PRIMARY KEY, Title text, Author text, Isbn text default 'not available');
```

### 导出SQL脚本
将SQLite中指定的数据表以SQL创建的形式导出

```
.output FILENAME       Send output to FILENAME
```

```
.dump ?TABLE? ...      Dump the database in an SQL text format
                         If TABLE specified, only dump tables matching
                         LIKE pattern TABLE.
```

#### 导出所有的SQL脚本
```
sqlite> .output outputdata.sql
sqlite> .dump
sqlite>
```
#### 导出指定表的的SQL脚本

```
sqlite> .output carsdata.sql
sqlite> .dump Cars
sqlite>
```

### 导出数据库

```
bixiaopeng@bixiaopeng db$ sqlite3 wirelessqa.db ".dump" | sqlite3 bxp.db
bixiaopeng@bixiaopeng db$ ls -al
total 168
drwxr-xr-x  7 bixiaopeng  staff    238  2 24 17:37 .
drwxr-xr-x  7 bixiaopeng  staff    238  2 24 17:37 ..
-rw-r--r--  1 bixiaopeng  staff  36864  2 24 17:37 bxp.db
-rw-r--r--  1 bixiaopeng  staff    484  2 24 17:31 carsdata.sql
-rw-r--r--  1 bixiaopeng  staff   2727  2 24 17:24 outputdata.sql
-rw-r--r--  1 bixiaopeng  staff   3174  2 24 17:15 testdata.sql
-rw-r--r--  1 bixiaopeng  staff  36864  2 24 17:15 wirelessqa.db
bixiaopeng@bixiaopeng db$ sqlite3 bxp.db "SELECT * FROM Cars;"
1|Audi|52642
2|Mercedes|57127
3|Skoda|9000
4|Volvo|29000
5|Bentley|350000
6|Citroen|21000
7|Hummer|41400
8|Volkswagen|21600
```
### 导出其它格式

#### 导出html格式
```
bixiaopeng@bixiaopeng db$ sqlite3 -html wirelessqa.db "SELECT * FROM Cars;"> wirelessqa.html
```


## 数据显示相关命令

### 设置分隔符：.separator    分隔符

```
.separator STRING      Change separator used by output mode and .import
```

默认分隔符是 |

```
sqlite> SELECT * FROM Cars;
1|Audi|52642
2|Mercedes|57127
3|Skoda|9000
4|Volvo|29000
5|Bentley|350000
6|Citroen|21000
7|Hummer|41400
8|Volkswagen|21600
```
自定义分隔符

```
sqlite> .separator -
sqlite> SELECT * FROM Cars;
1-Audi-52642
2-Mercedes-57127
3-Skoda-9000
4-Volvo-29000
5-Bentley-350000
6-Citroen-21000
7-Hummer-41400
8-Volkswagen-21600
sqlite> .separator ;
sqlite> SELECT * FROM Cars;
1;Audi;52642
2;Mercedes;57127
3;Skoda;9000
4;Volvo;29000
5;Bentley;350000
6;Citroen;21000
7;Hummer;41400
8;Volkswagen;21600
```
### 设置显示模式：.mode  模式
```
.mode MODE ?TABLE?     Set output mode where MODE is one of:
                         csv      Comma-separated values
                         column   Left-aligned columns.  (See .width)
                         html     HTML <table> code
                         insert   SQL insert statements for TABLE
                         line     One value per line
                         list     Values delimited by .separator string
                         tabs     Tab-separated values
                         tcl      TCL list elements
```

#### 默认是list显示模式

```
sqlite> SELECT * FROM Cars;
1|Audi|52642
2|Mercedes|57127
3|Skoda|9000
4|Volvo|29000
5|Bentley|350000
6|Citroen|21000
7|Hummer|41400
8|Volkswagen|21600
```
#### 更攺显示模式

```
sqlite> .mode csv
sqlite> SELECT * FROM Cars;
1,Audi,52642
2,Mercedes,57127
3,Skoda,9000
4,Volvo,29000
5,Bentley,350000
6,Citroen,21000
7,Hummer,41400
8,Volkswagen,21600
sqlite> .mode tabs
sqlite> SELECT * FROM Cars;
1	Audi	52642
2	Mercedes	57127
3	Skoda	9000
4	Volvo	29000
5	Bentley	350000
6	Citroen	21000
7	Hummer	41400
8	Volkswagen	21600
```

### 显示标题栏：.headers   on

```
.echo ON|OFF           Turn command echo on or off
```
#### 显示标题栏
```
sqlite> .headers on
sqlite> SELECT * FROM Cars;
Id	Name	Cost
1	Audi	52642
2	Mercedes	57127
3	Skoda	9000
4	Volvo	29000
5	Bentley	350000
6	Citroen	21000
7	Hummer	41400
8	Volkswagen	21600
```
#### 不显示标题栏

```
sqlite> .headers off
sqlite> SELECT * FROM Cars;
1	Audi	52642
2	Mercedes	57127
3	Skoda	9000
4	Volvo	29000
5	Bentley	350000
6	Citroen	21000
7	Hummer	41400
8	Volkswagen	21600
```
### 设置每一列的显示宽度：.width     NUM1 NUM2 ...

```
.width NUM1 NUM2 ...   Set column widths for "column" mode
```
默认的宽度显示不下需要用到这个命令

### 设置 NULL 值显示成什么样子： .nullvalue     你想要的NULL值格式

默认情况下NULL值什么也不显示，你可以设置成你自己想要的样子

```
sqlite> SELECT NULL,NULL,NULL;

sqlite> . nullvalue null
sqlite> SELECT NULL,NULL,NULL;
null	null	null
```

### 列出当前显示格式设置情况：.show

### 配置文件 .sqliterc