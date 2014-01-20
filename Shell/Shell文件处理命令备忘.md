# 文件处理

## 文件显示

### 文件输出

#### 过滤输出文件

```
bixiaopeng@bixiaopengdeiMac ~$ adb -s 192.168.56.101:5555 shell ps |grep monkey
root      1449  1446  438284 16024 ffffffff b7510dbe S com.android.commands.monkey
root      1467  1464  438284 16020 ffffffff b7597dbe S com.android.commands.monkey
root      1486  1481  438284 16024 ffffffff b7556dbe S com.android.commands.monkey
```
#### 打印出输出文件的某一列的内容

```
#使用awk
bixiaopeng@bixiaopengdeiMac ~$ adb -s 192.168.56.101:5555 shell ps |grep monkey|awk '{print $2}'
1449
1467
1486
```
#### 指定换行符

```
#使用ORS
bixiaopeng@bixiaopengdeiMac ~$ adb -s 192.168.56.101:5555 shell ps |grep monkey|awk 'ORS=";" {print $2}'
1449;1467;1486;
```

#### 指定输出某一行的某一列

```
awk    ‘NR==m {print $k}’  path/filename
```

```
bixiaopeng@bixiaopengdeiMac ~$ adb -s 192.168.56.101:5555 shell ps |grep monkey|awk 'NR==1 {print $2}'
1449
```

#### 指定输出m行到n行的某一列

```
awk ‘NR==m，NR==n {print $k}’  path/filename
```

### 一次显示多行输出

命令：

```
cat << EOF
****************
my name is bixiaopeng
my blog is http://blog.csdn.net/wirelessqa
my weibo is http://www.weibo.com/wirelessqa
****************
EOF
```
执行结果：

```
bixiaopeng@bixiaopengdeiMac Shell$ cat << EOF
> ****************
> my name is bixiaopeng
> my blog is http://blog.csdn.net/wirelessqa
> my weibo is http://www.weibo.com/wirelessqa
> ****************
> EOF
****************
my name is bixiaopeng
my blog is http://blog.csdn.net/wirelessqa
my weibo is http://www.weibo.com/wirelessqa
****************
```

### 创建一个空文件并添加内容 

```
bixiaopeng@bixiaopengdeiMac Shell$ cat << EOF >> wirelessqa.sh
> my name: bixiaopeng
> my blog: http://blog.csdn.net/wirelessqa
> EOF
bixiaopeng@bixiaopengdeiMac Shell$ cat wirelessqa.sh
my name: bixiaopeng
my blog: http://blog.csdn.net/wirelessqa
```

## 文件名/路径

#### 获取文件名

```
basename 文件路径
```

例子：

```
bixiaopeng@bixiaopengdeiMac Shell$ basename /Users/bixiaopeng/workspace/wirelessqa.txt

wirelessqa.txt
```
#### 获取文件路径

```
dirname 文件路径
```
例子：

```
bixiaopeng@bixiaopengdeiMac Shell$ dirname /Users/bixiaopeng/workspace/wirelessqa.txt
/Users/bixiaopeng/workspace
```
#### 获取文件名及后缀

```
获取文件名: ${文件名%.*}

获取文件后缀: ${文件名##*.}

```
例子： 

```
bixiaopeng@bixiaopengdeiMac Shell$ name=wirelessqa.txt
bixiaopeng@bixiaopengdeiMac Shell$ echo ${name%.*}
wirelessqa
bixiaopeng@bixiaopengdeiMac Shell$ echo ${name##*.}
txt
```
## 文件判断

#### 判断文件是否存在

```
if [ ! -d 文件路径 ]; then
 #新建一个
 mkdir -p $output_path
fi
```


## 编码格式转换

可以直接用iconv命令

    iconv -f UTF-16 -t UTF-8 src.txt > srcutf8.txt

如果是excel文件转utf8可以先另存.xls为utf-16的文本文件，再转换成utf8

