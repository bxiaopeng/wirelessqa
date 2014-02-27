# 表的增删攺查

## 4.1 SQLite 存储类型

### SQLite 存储类型

存储类型|	描述
----|----
NULL	|值是一个 NULL 值。
INTEGER	|值是一个带符号的整数，根据值的大小存储在 1、2、3、4、6 或 8 字节中。
REAL	|值是一个浮点值，存储为 8 字节的 IEEE 浮点数字。
TEXT	|值是一个文本字符串，使用数据库编码（UTF-8、UTF-16BE 或 UTF-16LE）存储。
BLOB	|值是一个 blob 数据，完全根据它的输入存储。 


## 4.2 创建数据库和创建表

创建了一个 COMPANY 表，ID 作为主键，NOT NULL 的约束表示在表中创建纪录时这些字段不能为 NULL

```
bixiaopeng@bixiaopeng db$ sqlite3 wireless.db
SQLite version 3.7.13 2012-07-17 17:46:21
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> CREATE TABLE COMPANY(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,AGE INT NOT NULL,ADDRESS CHAR(50),SALARY REAL);
```

CREATE TABLE 是告诉数据库系统创建一个新表的关键字。CREATE TABLE 语句后跟着表的唯一的名称或标识。您也可以选择指定带有 table_name 的 database_name。

查看表是否创建成功

```
sqlite> .tables
COMPANY
```
查看表的完整信息

```
sqlite> .schema COMPANY
CREATE TABLE COMPANY(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,AGE INT NOT NULL,ADDRESS CHAR(50),SALARY REAL);
```
## 4.3 插入数据

### 插入数据，方法一:插入对应的列的值

```
sqlite> INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
   ...> VALUES (1, 'Paul', 32, 'California', 20000.00 );
```
查询是否插入成功

```
sqlite> SELECT * FROM COMPANY;
1|Paul|32|California|20000.0
```
###　插入数据，方法二:给所有列插入值

```
sqlite> INSERT INTO COMPANY VALUES (7, 'James', 24, 'Houston', 10000.00 );
sqlite> SELECT * FROM COMPANY;
1|Paul|32|California|20000.0
7|James|24|Houston|10000.0
```
用第二种方法多插入几个数据:

```
sqlite> INSERT INTO COMPANY VALUES (2, 'Allen', 25, 'Texas', 15000.00 );
sqlite> INSERT INTO COMPANY VALUES (3, 'Teddy', 23, 'Norway', 20000.00 );
sqlite> INSERT INTO COMPANY VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 );
sqlite> INSERT INTO COMPANY VALUES (5, 'David', 27, 'Texas', 85000.00 );
sqlite> INSERT INTO COMPANY VALUES (6, 'Kim', 22, 'South-Hall', 45000.00 );
sqlite> SELECT * FROM COMPANY;
1|Paul|32|California|20000.0
7|James|24|Houston|10000.0
2|Allen|25|Texas|15000.0
3|Teddy|23|Norway|20000.0
4|Mark|25|Rich-Mond |65000.0
5|David|27|Texas|85000.0
6|Kim|22|South-Hall|45000.0
```



## 4.4 更新数据

```
//先插入一条数据
sqlite> INSERT INTO COMPANY VALUES (8, 'wirelessqa', 28, 'HZ', 20000.00 );
sqlite> SELECT * FROM COMPANY;
ID	NAME	AGE	ADDRESS	SALARY
1	Paul	32	California	20000.0
7	James	24	Houston	10000.0
2	Allen	25	Texas	15000.0
3	Teddy	23	Norway	20000.0
4	Mark	25	Rich-Mond 	65000.0
5	David	27	Texas	85000.0
6	Kim	22	South-Hall	45000.0
8	wirelessqa	28	HZ	20000.0

//更新NAME为wirelessqa的地址为NanJing
sqlite> UPDATE COMPANY SET ADDRESS = 'NanJing' WHERE NAME = 'wirelessqa';
8	wirelessqa	28	NanJing	20000.0

//查看更新后的数据
sqlite> SELECT * FROM COMPANY WHERE NAME = 'wirelessqa';
ID	NAME	AGE	ADDRESS	SALARY
8	wirelessqa	28	NanJing	20000.0
```


## 4.5 删除数据

```
//删除ADDRESS为NanJing的这条数据
sqlite> DELETE FROM COMPANY WHERE ADDRESS = 'NanJing';
sqlite> SELECT * FROM COMPANY WHERE ADDRESS = 'NanJing';
sqlite>
```



## 4.6　数据查询


### 4.6.1. SQLite 算术运算符

运算符: + - * / %

```
sqlite> select 4 + 2;
6
sqlite> select 4 - 2;
2
sqlite> select 4 * 2;
8
sqlite> select 4 / 2;
2
sqlite> select 4 % 2;
0
```

### 4.6.2. SQLite 算术运算符

运算符	|描述|	实例
----|----|----
==	|检查两个操作数的值是否相等，如果相等则条件为真。 |(a == b) 不为真。
=	|检查两个操作数的值是否相等，如果相等则条件为真| (a = b) 不为真。
!=	|检查两个操作数的值是否相等，如果不相等则条件为真|	 (a != b) 为真。
<>	|检查两个操作数的值是否相等，如果不相等则条件为真|(a <> b) 为真。
\>	|检查左操作数的值是否大于右操作数的值，如果是则条件为真。|(a > b) 不为真。
<	|检查左操作数的值是否小于右操作数的值，如果是则条件为真|(a < b) 为真。
\>=	|检查左操作数的值是否大于等于右操作数的值，如果是则条件为真|(a >= b) 不为真。
<=	|检查左操作数的值是否小于等于右操作数的值，如果是则条件为真|(a <= b) 为真。


看一下表里现有的数据：

```
sqlite> .headers on
sqlite> .mode tabs
sqlite> SELECT * FROM COMPANY;
ID	NAME	AGE	ADDRESS	SALARY
1	Paul	32	California	20000.0
7	James	24	Houston	10000.0
2	Allen	25	Texas	15000.0
3	Teddy	23	Norway	20000.0
4	Mark	25	Rich-Mond 	65000.0
5	David	27	Texas	85000.0
6	Kim	22	South-Hall	45000.0
sqlite> SELECT * FROM COMPANY WHERE AGE = 32;
ID	NAME	AGE	ADDRESS	SALARY
1	Paul	32	California	20000.0
sqlite> SELECT * FROM COMPANY WHERE AGE == 32 ;
ID	NAME	AGE	ADDRESS	SALARY
1	Paul	32	California	20000.0
sqlite> SELECT * FROM COMPANY WHERE AGE < 32;
ID	NAME	AGE	ADDRESS	SALARY
7	James	24	Houston	10000.0
2	Allen	25	Texas	15000.0
3	Teddy	23	Norway	20000.0
4	Mark	25	Rich-Mond 	65000.0
5	David	27	Texas	85000.0
6	Kim	22	South-Hall	45000.0
sqlite> SELECT * FROM COMPANY WHERE AGE != 32;
ID	NAME	AGE	ADDRESS	SALARY
7	James	24	Houston	10000.0
2	Allen	25	Texas	15000.0
3	Teddy	23	Norway	20000.0
4	Mark	25	Rich-Mond 	65000.0
5	David	27	Texas	85000.0
6	Kim	22	South-Hall	45000.0
sqlite> SELECT * FROM COMPANY WHERE AGE <= 32;
ID	NAME	AGE	ADDRESS	SALARY
1	Paul	32	California	20000.0
7	James	24	Houston	10000.0
2	Allen	25	Texas	15000.0
3	Teddy	23	Norway	20000.0
4	Mark	25	Rich-Mond 	65000.0
5	David	27	Texas	85000.0
6	Kim	22	South-Hall	45000.0
sqlite> SELECT * FROM COMPANY WHERE AGE >= 32;
ID	NAME	AGE	ADDRESS	SALARY
1	Paul	32	California	20000.0
sqlite> SELECT * FROM COMPANY WHERE AGE > 32;
```

### 4.6.3. SQLite 逻辑运算符

运算符|	描述
----|----
AND|	AND 运算符允许在一个 SQL 语句的 WHERE 子句中的多个条件的存在。
BETWEEN|	BETWEEN 运算符用于在给定最小值和最大值范围内的一系列值中搜索值。
EXISTS|	EXISTS 运算符用于在满足一定条件的指定表中搜索行的存在。
IN	|IN 运算符用于把某个值与一系列指定列表的值进行比较。
NOT IN	|IN 运算符的对立面，用于把某个值与不在一系列指定列表的值进行比较。
LIKE	|LIKE 运算符用于把某个值与使用通配符运算符的相似值进行比较。
GLOB	|GLOB 运算符用于把某个值与使用通配符运算符的相似值进行比较。GLOB 与 LIKE 不同之处在于，它是大小写敏感的。
NOT	|NOT 运算符是所用的逻辑运算符的对立面。比如 NOT EXISTS、NOT BETWEEN、NOT IN，等等。它是否定运算符。
OR	|OR 运算符用于结合一个 SQL 语句的 WHERE 子句中的多个条件。
IS NULL	|NULL 运算符用于把某个值与 NULL 值进行比较。
IS	|IS 运算符与 = 相似。
IS NOT	|IS NOT 运算符与 != 相似。
\|\|	|连接两个不同的字符串，得到一个新的字符串。
UNIQUE	|UNIQUE 运算符搜索指定表中的每一行，确保唯一性（无重复）。

```
//AND 运算符允许在一个 SQL 语句的 WHERE 子句中的多个条件的存在。
sqlite> SELECT * FROM COMPANY WHERE AGE < 25 AND SALARY > 15000.0;
ID	NAME	AGE	ADDRESS	SALARY
3	Teddy	23	Norway	20000.0
6	Kim	22	South-Hall	45000.0

//OR 运算符用于结合一个 SQL 语句的 WHERE 子句中的多个条件。
sqlite> SELECT * FROM COMPANY WHERE AGE < 25 OR SALARY > 15000.0;
ID	NAME	AGE	ADDRESS	SALARY
1	Paul	32	California	20000.0
7	James	24	Houston	10000.0
3	Teddy	23	Norway	20000.0
4	Mark	25	Rich-Mond 	65000.0
5	David	27	Texas	85000.0
6	Kim	22	South-Hall	45000.0

//BETWEEN 运算符用于在给定最小值和最大值范围内的一系列值中搜索值。
sqlite> SELECT * FROM COMPANY WHERE AGE BETWEEN 25 AND 32;
ID	NAME	AGE	ADDRESS	SALARY
1	Paul	32	California	20000.0
2	Allen	25	Texas	15000.0
4	Mark	25	Rich-Mond 	65000.0
5	David	27	Texas	85000.0

//EXISTS 运算符用于在满足一定条件的指定表中搜索行的存在。
sqlite> SELECT AGE FROM COMPANY WHERE EXISTS (SELECT AGE FROM COMPANY WHERE SALARY > 65000);
AGE
32
24
25
23
25
27
22

//AGE 不为 NULL 的所有记录
sqlite> SELECT * FROM COMPANY WHERE AGE IS NOT NULL;
ID	NAME	AGE	ADDRESS	SALARY
1	Paul	32	California	20000.0
7	James	24	Houston	10000.0
2	Allen	25	Texas	15000.0
3	Teddy	23	Norway	20000.0
4	Mark	25	Rich-Mond 	65000.0
5	David	27	Texas	85000.0
6	Kim	22	South-Hall	45000.0

//LIKE 运算符用于把某个值与使用通配符运算符的相似值进行比较。
sqlite> SELECT * FROM COMPANY WHERE NAME LIKE 'Ki%';
ID	NAME	AGE	ADDRESS	SALARY
6	Kim	22	South-Hall	45000.0

//GLOB 运算符用于把某个值与使用通配符运算符的相似值进行比较。GLOB 与 LIKE 不同之处在于，它是大小写敏感的。
sqlite> SELECT * FROM COMPANY WHERE NAME GLOB 'Ki*';
ID	NAME	AGE	ADDRESS	SALARY
6	Kim	22	South-Hall	45000.0

//IN 运算符用于把某个值与一系列指定列表的值进行比较。
sqlite> SELECT * FROM COMPANY WHERE AGE IN ( 25, 27 );
ID	NAME	AGE	ADDRESS	SALARY
2	Allen	25	Texas	15000.0
4	Mark	25	Rich-Mond 	65000.0
5	David	27	Texas	85000.0

//IN 运算符的对立面，用于把某个值与不在一系列指定列表的值进行比较。
sqlite> SELECT * FROM COMPANY WHERE AGE NOT IN ( 25, 27 );
ID	NAME	AGE	ADDRESS	SALARY
1	Paul	32	California	20000.0
7	James	24	Houston	10000.0
3	Teddy	23	Norway	20000.0
6	Kim	22	South-Hall	45000.0

//
sqlite> SELECT * FROM COMPANY WHERE AGE > (SELECT AGE FROM COMPANY WHERE SALARY > 65000);
ID	NAME	AGE	ADDRESS	SALARY
1	Paul	32	California	20000.0

sqlite> SELECT * FROM COMPANY WHERE AGE < (SELECT AGE FROM COMPANY WHERE SALARY > 65000);
ID	NAME	AGE	ADDRESS	SALARY
7	James	24	Houston	10000.0
2	Allen	25	Texas	15000.0
3	Teddy	23	Norway	20000.0
4	Mark	25	Rich-Mond 	65000.0
6	Kim	22	South-Hall	45000.0
```
### 4.6.4 排序、分组、去重、时间

```
//通过内置函数查看一共有多少条数据
sqlite> SELECT COUNT(*) AS "RECORDS" FROM COMPANY;
RECORDS
7

//显示前4条
sqlite> SELECT * FROM COMPANY LIMIT 4;
ID	NAME	AGE	ADDRESS	SALARY
1	Paul	32	California	20000.0
7	James	24	Houston	10000.0
2	Allen	25	Texas	15000.0
3	Teddy	23	Norway	20000.0


//按SALARY降序排序
sqlite> SELECT * FROM COMPANY ORDER BY SALARY ASC;
ID	NAME	AGE	ADDRESS	SALARY
7	James	24	Houston	10000.0
2	Allen	25	Texas	15000.0
1	Paul	32	California	20000.0
3	Teddy	23	Norway	20000.0
6	Kim	22	South-Hall	45000.0
4	Mark	25	Rich-Mond 	65000.0
5	David	27	Texas	85000.0

//按SALARY升序排序
sqlite> SELECT * FROM COMPANY ORDER BY SALARY DESC;
ID	NAME	AGE	ADDRESS	SALARY
5	David	27	Texas	85000.0
4	Mark	25	Rich-Mond 	65000.0
6	Kim	22	South-Hall	45000.0
1	Paul	32	California	20000.0
3	Teddy	23	Norway	20000.0
2	Allen	25	Texas	15000.0
7	James	24	Houston	10000.0

//按NAME和SALARY升序排序
sqlite> SELECT * FROM COMPANY ORDER BY AGE,SALARY DESC;
ID	NAME	AGE	ADDRESS	SALARY
6	Kim	22	South-Hall	45000.0
3	Teddy	23	Norway	20000.0
7	James	24	Houston	10000.0
4	Mark	25	Rich-Mond 	65000.0
2	Allen	25	Texas	15000.0
5	David	27	Texas	85000.0
1	Paul	32	California	20000.0

// GROUP BY 子句用于与 SELECT 语句一起使用，来对相同的数据进行分组。

// 查询某个人的工资总数
sqlite>  SELECT NAME, SUM(SALARY) FROM COMPANY GROUP BY NAME;
NAME	SUM(SALARY)
Allen	15000.0
David	85000.0
James	10000.0
Kim	45000.0
Mark	65000.0
Paul	20000.0
Teddy	20000.0

// GROUP BY 和 ORDER BY一起用
sqlite> SELECT NAME, SUM(SALARY) FROM COMPANY GROUP BY NAME ORDER BY NAME DESC;
NAME	SUM(SALARY)
Teddy	20000.0
Paul	20000.0
Mark	65000.0
Kim	45000.0
James	10000.0
David	85000.0
Allen	15000.0

//HAVING 子句允许指定条件来过滤将出现在最终结果中的分组结果。

//WHERE 子句在所选列上设置条件，而 HAVING 子句则在由 GROUP BY 子句创建的分组上设置条件。

//在一个查询中，HAVING 子句必须放在 GROUP BY 子句之后，必须放在 ORDER BY 子句之前


//查询所有数据
qlite> SELECT * FROM COMPANY;
ID	NAME	AGE	ADDRESS	SALARY
1	Paul	32	California	20000.0
7	James	24	Houston	10000.0
2	Allen	25	Texas	15000.0
3	Teddy	23	Norway	20000.0
4	Mark	25	Rich-Mond 	65000.0
5	David	27	Texas	85000.0
6	Kim	22	South-Hall	45000.0

//查询AGE，并去重
sqlite> SELECT DISTINCT AGE FROM COMPANY;
AGE
32
24
25
23
27
22

日期 & 时间

//把header关掉了
sqlite> . header off
sqlite> SELECT date('now');
2014-02-27

sqlite> SELECT datetime(1092941466, 'unixepoch');
2004-08-19 18:51:06

sqlite> SELECT TIME('NOW');
07:47:25å
```
### 4.6.5. 常用函数

```
//表行数
sqlite> SELECT count(*) FROM COMPANY;
7

//最大值
sqlite> SELECT max(salary) FROM COMPANY;
85000.0

//最小值 
sqlite> SELECT min(salary) FROM COMPANY;
10000.0

//平均值
sqlite> SELECT avg(salary) FROM COMPANY;
37142.8571428572
sqlite> SELECT sum(salary) FROM COMPANY;
260000.0

//转大写
sqlite> SELECT upper(name) FROM COMPANY;
PAUL
JAMES
ALLEN
TEDDY
MARK
DAVID
KIM

//转小写
sqlite> SELECT lower(name) FROM COMPANY;
paul
james
allen
teddy
mark
david
kim

//长度
sqlite> SELECT name, length(name) FROM COMPANY;
Paul	4
James	5
Allen	5
Teddy	5
Mark	4
David	5
Kim	3
sqlite>
```



## 4.7 删除表

```
sqlite> DROP TABLE COMPANY;
sqlite> .tables
```


## 4.8 删除数据库

```
直接rm 删除掉db文件就可以了
```

本系列主要参考：

http://www.w3cschool.cc/sqlite/sqlite-functions.html

http://www.cnblogs.com/myqiao/archive/2011/07/10/2102465.html


----
####  微信公众帐号: wirelessqa 
![wirelessqa](https://github.com/bxiaopeng/wirelessqa/raw/master/img/qrcode_for_gh_fdde1fe2880a_258.jpg)

#### 关于作者：

**作者:** 毕小朋 | 老 毕  **邮箱:** <wirelessqa.me@gmail.com> 

**微博:** [@WirelessQA](http://www.weibo.com/wirelessqa) **博客:** <http://blog.csdn.net/wirelessqa>

----