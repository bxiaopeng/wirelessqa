## 2.1 基本命令

### 2.1.1 显示帮助

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

### 2.1.2 进入和退出命令行环境

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

## 2.2 数据库和表相关命令

### 2.2.1 创建一个新的数据库: sqlite3 数据库名

```
bixiaopeng@bixiaopeng SQLITE$ mkdir db && cd db && sqlite3 wiressqa.db
SQLite version 3.7.13 2012-07-17 17:46:21
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite>
```
### 2.2.3  打开一个已经存在的数据库: sqlite3 数据库名

```
bixiaopeng@bixiaopeng db$ sqlite3 wirelessqa.db
SQLite version 3.7.13 2012-07-17 17:46:21
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite>
```

### 2.2.3 导入数据: .read 数据文件

#### help:

```
.read FILENAME         Execute SQL in FILENAME
```
#### example:

##### 准备testdata.sql文件

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
##### 读入数据

```
sqlite> .read testdata.sql
```

### 2.2.4 导入文本数据

##### 准备data.txt文件

```
id,name,age,address,hobby
1,bxp,28,hz,ktv
2,zxh,30,hz,play
3,mx,25,kf,ktv
4,ml,26,jx,play
5,cc,25,qdh,ktv
```
##### 导入data.txt文件

```
//步骤: 创建表 -- 指定分隔符 -- 导入数据到表 -- 查看
bixiaopeng@bixiaopeng db$ sqlite3 txtdata.db
SQLite version 3.7.13 2012-07-17 17:46:21
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> create table txt_data_table(id char(10),name char(10),age char(10),address varchar(15),hobby varchar (15));
sqlite> .separator ","
sqlite> .import data.txt txt_data_table
sqlite> SELECT * FROM txt_data_table;
id,name,age,address,hobby
1,bxp,28,hz,ktv
2,zxh,30,hz,play
3,mx,25,kf,ktv
4,ml,26,jx,play
5,cc,25,qdh,ktv
```

### 2.2.5 列出所有数据表: .tables

#### help:

```
.tables ?TABLE?        List names of tables
                         If TABLE specified, only list tables matching
                         LIKE pattern TABLE.
```

#### example:

```
sqlite> .tables
Books         Customers     Names         Reservations
Cars          Friends       Orders
```
### 2.2.6 显示数据库或表结构：.schema

#### help:

```
.schema ?TABLE?        Show the CREATE statements
                         If TABLE specified, only show tables matching
                         LIKE pattern TABLE.
```

#### example:

#### 1. 显示数据库结构

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
#### 2. 显示表结构

```
sqlite> .schema Books
CREATE TABLE Books(Id integer PRIMARY KEY, Title text, Author text, Isbn text default 'not available');
```

### 2.2.7 显示当前所有的数据库: .databases

#### help:

```
.databases             List names and files of attached databases
```

#### example:

```
bixiaopeng@bixiaopeng db$ sqlite3 wirelessqa.db ".databases"
seq  name             file
---  ---------------  ----------------------------------------------------------
0    main             /Users/bixiaopeng/workspace/source-github/wirelessqa/SQLIT
```



### 2.2.7 导出SQL脚本
将SQLite中指定的数据表以SQL创建的形式导出

#### help：

```
.output FILENAME       Send output to FILENAME
```

```
.dump ?TABLE? ...      Dump the database in an SQL text format
                         If TABLE specified, only dump tables matching
                         LIKE pattern TABLE.
```
#### example:

##### 1. 导出所有的SQL脚本
```
sqlite> .output outputdata.sql
sqlite> .dump
sqlite>
```
##### 2. 导出指定表的的SQL脚本

```
sqlite> .output carsdata.sql
sqlite> .dump Cars
sqlite>
```

##### 3. 导出数据库

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
##### 4. 导出其它格式

###### 默认list，其它任选

```
                         csv      Comma-separated values
                         column   Left-aligned columns.  (See .width)
                         html     HTML <table> code
                         insert   SQL insert statements for TABLE
                         line     One value per line
                         list     Values delimited by .separator string
                         tabs     Tab-separated values
                         tcl      TCL list elements
```

###### 导出html格式

```
bixiaopeng@bixiaopeng db$ sqlite3 -html wirelessqa.db "SELECT * FROM Cars;"> wirelessqa.html
```

###### 导出csv格式

```
bixiaopeng@bixiaopeng db$ sqlite3 -csv wirelessqa.db "SELECT * FROM Cars;"> wirelessqa.csv
bixiaopeng@bixiaopeng db$ cat wirelessqa.csv
1,Audi,52642
2,Mercedes,57127
3,Skoda,9000
4,Volvo,29000
5,Bentley,350000
6,Citroen,21000
7,Hummer,41400
8,Volkswagen,21600
```


