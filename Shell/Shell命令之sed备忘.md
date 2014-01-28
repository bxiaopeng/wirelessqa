
## 一、sed简明教程

http://coolshell.cn/articles/9104.html


## 二、sed总结
```
sed命令的格式是 
sed [-options] [command] [stdin] 
例子： 
$ sed –e ‘d’ test.txt 
执行该命令，将得不到任何输出。在该例中，用一个编辑命令 'd' 调用 sed；sed 打开 test.txt 将一行读入其模式缓冲区，执行’d’（“删除行”）；然后打印模式缓冲区（缓冲区已为空）；它对后面的每一行重复这些步骤，这不会产生输出！
```

### 指定sed的作用范围
```
$ sed –e ‘1d’ test.txt
$ sed –e ‘1,10d’ test.txt
$ sed –e ‘/begin/,/end/p’ test.txt
第一个例子说明只删除test.txt第一行的缓冲
第二个例子将删除第1~10行的缓冲。
第三个例子最复杂，它定义了以字符串’begin’开始到’end’结束的作用范围
```
### sed中的正则表达式

sed支持正则表达式，eg:
$ sed –n -e ‘/regexp/p’ test.txt

删除所有的空行
$ sed –e ‘/^$/d’ test.txt


### sed中的一些特殊定义是

```
/./ 将与包含至少一个字符的任何行匹配
/../ 将与包含至少两个字符的任何行匹配
/^#/ 将与以 '#' 开始的任何行匹配
/^$/ 将与所有空行匹配
/}^/ 将与以 '}'（无空格）结束的任何行匹配
/} *^/ 将与以 '}' 后面跟有 零或多个空格结束的任何行匹配 
/[abc]/ 将与包含小写 'a'、'b' 或 'c' 的任何行匹配
/^[abc]/ 将与以 'a'、'b' 或 'c' 开始的任何行匹配
```

### 打印、替换
```
打印:
$ sed –n –e ‘/main[[:space]]*(/,/^}/p’ ./Mydir/*.c
其中[:space]表示空格，[[:space]]*表示有0~多个空格，所以main[[:space]]*(的意思是匹配“main (”字符串；“^}”表示这一行有且只有一个字符}。当然，上面的命令不是十分严谨。

sed –e ‘s/regexp/repalcement’ file
替换：
$ sed –e ‘s/a/b’ test.txt
$ sed –e ‘s/a/b/g’ test.txt
第一个命令将test.txt中每一行第一次出现的字符a替换成字符b；第二个命令由于加入了’/g’，表示是全局（全部）替换字符a成字符b。

指定替换行：
$ sed –e ‘1,10s/a/b’ test.txt
$ sed –e ‘/^$/,/^END/s/a/b/g’ test.txt
第一个命令是指替换1~10行；第二个命令是指全局替换从空行开始到以END开始的行中的内容。

替换命令不一定非要以/分隔:
$ sed –e ‘s:usr/local:/usr:g’ test.txt
就是将test.txt中的usr/local全部替换成/usr
要用好替换命令，当然要使用正则表达式，除了上面所说的表达式的例子，还有一些是非常有用的
```
### 特殊字符
```
[:alnum:] 字母数字 [a-z A-Z 0-9]
[:alpha:] 字母 [a-z A-Z]
[:blank:] 空格或制表键
[:cntrl:] 任何控制字符
[:digit:] 数字 [0-9]
[:graph:] 任何可视字符（无空格）
[:lower:] 小写 [a-z]
[:print:] 非控制字符
[:punct:] 标点字符
[:space:] 空格
[:upper:] 大写 [A-Z]
[:xdigit:] 十六进制数字 [0-9 a-f A-F]
```

### 去掉html中的标签

```
$ sed –e ‘s/<[^>]*>//g’ test.txt
#< [^>]*>匹配<…>这样的字符串（…中不含>）。运行这个命令，能够将 “<b>This</b> is what <b>I</b> meant.”这样的字符串替换成“This is what I meant.”
```


### sed中组合命令

sed中的命令可以组合，以；号隔开，比如
$ sed –n –e ‘=;p’ test.txt
=表示打印行号，p表示打印。

对于更复杂的指令，则可以写成命令脚本，然后用-f选项导入，比如
$ sed –n –f MyScript.sed test.txt
对于同一个地址上的操作，则可以用{}组合，比如
$ sed –n ‘1,20{ s/samba/Samba/g s/posix/POSIX/g }’ test.txt
