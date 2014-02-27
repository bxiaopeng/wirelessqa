## 1.1. SQLite是什么
SQLite是一个进程内的库，实现了自给自足的、无服务器的、零配置的、事务性的 SQL 数据库引擎。它是一个零配置的数据库，这意味着与其他数据库一样，您不需要在系统中配置。

就像其他数据库，SQLite 引擎不是一个独立的进程，可以按应用程序需求进行静态或动态连接。SQLite 直接访问其存储文件。

## 1.2 为什么要用 SQLite？
不需要一个单独的服务器进程或操作的系统（无服务器的）。

SQLite 不需要配置，这意味着不需要安装或管理。

一个完整的 SQLite 数据库是存储在一个单一的跨平台的磁盘文件。

SQLite 是非常小的，是轻量级的，完全配置时小于 400KiB，省略可选功能配置时小于250KiB。

SQLite 是自给自足的，这意味着不需要任何外部的依赖。

SQLite 事务是完全兼容 ACID 的，允许从多个进程或线程安全访问。

SQLite 支持 SQL92（SQL2）标准的大多数查询语言的功能。

SQLite 使用 ANSI-C 编写的，并提供了简单和易于使用的 API。

SQLite 可在 UNIX（Linux, Mac OS-X, Android, iOS）和 Windows（Win32, WinCE, WinRT）中运行。

## 1.3 SQLite 语法

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



## 1.4 SQLite 数据类型

SQLite 数据类型是一个用来指定任何对象的数据类型的属性。SQLite 中的每一列，每个变量和表达式都有相关的数据类型。

您可以在创建表的同时使用这些数据类型。SQLite 使用一个更普遍的动态类型系统。在 SQLite 中，值的数据类型与值本身是相关的，而不是与它的容器相关。

### SQLite 存储类型
每个存储在 SQLite 数据库中的值都具有以下存储类型之一：

存储类型|	描述
----|----
NULL	|值是一个 NULL 值。
INTEGER	|值是一个带符号的整数，根据值的大小存储在 1、2、3、4、6 或 8 字节中。
REAL	|值是一个浮点值，存储为 8 字节的 IEEE 浮点数字。
TEXT	|值是一个文本字符串，使用数据库编码（UTF-8、UTF-16BE 或 UTF-16LE）存储。
BLOB	|值是一个 blob 数据，完全根据它的输入存储。

SQLite 的存储类型稍微比数据类型更普遍。INTEGER 存储类，例如，包含 6 种不同的不同长度的整数数据类型。



## 1.5 环境配置

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