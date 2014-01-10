
## 一. shell条件语句(if用法)

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

``[chengmo@centos5 ~]$ a=5;if [[ a -gt 4 ]] ;then echo 'ok';fi;                        
ok``

例子:

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

**小贴示：**

seq字符串只要用空格字符分割，每次for…in 读取时候，就会按顺序将读到值，给前面的变量。

#### 2.for((赋值；条件；运算语句))

```
for((赋值；条件；运算语句))
do
action
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