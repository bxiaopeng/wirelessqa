
## 一. shell条件语句(if用法)

### 1.1 if语法

### if语句结构 [if/then/elif/else/fi]


```
if 条件测试语句
then
action
[elif 条件
action
else
action
]
fi
```
**小贴示：**

***shell命令，可以按照分号分割，也可以按照换行符分割。如果想一行写入多个命令，可以通过“';”分割。***


如：

```
$ a=5;if [[ a -gt 4 ]] ;then echo 'ok';fi;                        
ok
```
### if的基本语法

1. if与[之间要有空格
2. [ ]与判断条件之间也必须有空格
3. ]与;之间不能有空格

### 对字符串的判断

1. if [ str1=str2 ];then fi #当两个字符串相同时返回真
2. if [ str1!=str2 ];then fi #当两个字符串不相等时返回真
3. if [ -n str1 ];then fi #当字符串的长度大于0时返回真 (判断变量是否有值)
4. if [ -z str1 ];then fi #当字符串的长度为0时返回真

### 对数字的判断

1. int1 -eq int2 #int1和int2相等
2. int1 -ne int2 #int1不相等int2
3. int1 -gt int2 #int1大于int2
4. int1 -ge int2 #int1大于等于int2
5. int1 -lt int2 #int1小于int2
6. int1 -le int2 #int1小于等于int2

### 对文件属性的判断

1. -r file #用户可读为真
2. -w file #用户可写为真
3. -x file #用户可执行为真
4. -f file #文件存在且为正规文件为真
5. -d file #如果是存在目录为真
6. -c file #文件存在且为字符设备文件
7. -b file #文件存在且为块设备文件
8. -s file #文件大小为非0为真，可以判断文件是否为空
9. -e file #如果文件存在为真

### 逻辑判断
1. -a #与
2. -o #或
3. ! #非

**例子:**

```
#!/bin/sh
scores=40;
if [[ $scores -gt 90 ]]; then
    echo "very good!";
elif [[ $scores -gt 80 ]]; then
    echo "good!";
elif [[ $scores -gt 60 ]]; then
    echo "pass!";
else
    echo "no pass!";
fi;
```

**小贴示：**

条件测试有：[[]],[],test 这几种，注意：[[]] 与变量之间用空格分开。

## 二. 循环语句(for,while,until用法）

### 2.1 for循环使用方法(for/do/done)


#### 1.for … in 语句

```
for 变量 in seq字符串
do
action
done
```
***例子:***

```
#!/bin/sh
for i in $(seq 10); do
    echo $i;
done;
```

**小贴示：**

seq字符串只要用空格字符分割，每次for…in 读取时候，就会按顺序将读到值，给前面的变量。

#### 2.for((赋值；条件；运算语句))

```
for((赋值；条件；运算语句))
do
action
done;
```

***例子：***

```
#!/bin/sh
for((i=1;i<=10;i++));do
    echo $i;
done;
```

### 2.2 while循环使用（while/do/done)

#### while语句结构


```
while 条件语句
do
action
done;
```
***例子:***

```
#!/bin/sh
i=10;
while [[ $i -gt 5 ]];do
    echo $i;
    ((i--));
done;
```


### 2.3 until循环语句

```
until 条件
do
action
done
```

## 三. shell选择语句（case、select用法）

#### 3.1 case选择语句使用（case/esac)

```
case $arg in  
    pattern | sample) # arg in pattern or sample  
    ;;  
    pattern1) # arg in pattern1  
    ;;  
    *) #default  
    ;;  
esac 

```                   
                    pattern1 是正则表达式,可以用下面字符：
                 *       任意字串
                 ?       任意字元
                 [abc]   a, b, 或c三字元其中之一
                 [a-n]   从a到n的任一字元
                 |       多重选择
```

意思是：直到满足条件，就退出。否则执行action.


#### 3.2 select语句使用方法（产生菜单选择）

```
select 变量name  in seq变量
do
    action
done
```

参考：http://www.cnblogs.com/chengmo/archive/2010/10/14/1851434.html(例子待补)