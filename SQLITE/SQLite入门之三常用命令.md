## 3. 数据显示相关命令

### 3.1 设置分隔符：.separator    分隔符

#### help:

```
.separator STRING      Change separator used by output mode and .import
```
#### example:

##### 默认分隔符是 |

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
##### 自定义分隔符

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
### 3.2 设置显示模式：.mode  模式
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

####  默认是list显示模式

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

### 3.3 显示标题栏：.headers   on

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
### 3.4 设置每一列的显示宽度：.width     NUM1 NUM2 ...

```
.width NUM1 NUM2 ...   Set column widths for "column" mode
```
默认的宽度显示不下需要用到这个命令

### 3.5 设置 NULL 值显示成什么样子： .nullvalue     你想要的NULL值格式

默认情况下NULL值什么也不显示，你可以设置成你自己想要的样子

```
sqlite> SELECT NULL,NULL,NULL;

sqlite> . nullvalue null
sqlite> SELECT NULL,NULL,NULL;
null	null	null
```

### 3.6 列出当前显示格式设置情况：.show

#### help:
```
.show                  Show the current values for various settings
```
#### example:
```
bixiaopeng@bixiaopeng db$ sqlite3 wirelessqa.db
SQLite version 3.7.13 2012-07-17 17:46:21
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .show
     echo: off
  explain: off
  headers: off
     mode: list
nullvalue: ""
   output: stdout
separator: "|"
    stats: off
    width:
```

### 3.7 配置文件 .sqliterc

如果我们每次进入命令行都要重新设置显示格式，很麻烦，其实 .show 命令列出的所有设置项都可以保存到一个 .sqliterc 文件中，这样每次进入命令行就自动设置好了。

.sqlterc 文件在 Linux下保存在用户的Home目录下,在Windows下可以保存到任何目录下，但是需要设置环境变量让数据库引擎能找到它，这个就不举例了，感兴趣的可以看看帮助。 

### 3.8 更多命令请查看帮助