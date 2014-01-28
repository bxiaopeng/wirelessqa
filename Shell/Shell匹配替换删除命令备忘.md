# 一、匹配

### 1.1 匹配多个字符
```
cat test.txt |grep -E "a|b|c"
```
### 1.2 匹配取反
```
cat test.txt |grep -v "a"
```
### 1.3 匹配指字字符，并且指定多打印几行
```
cat test.txt| grep -1 "<dt>版本</dt>" #会多打钱出匹配到字符的上下一行
```
### 1.4 匹配指定关键字之间的行
```
cat test.txt |sed -n '/【更新内容】/,/展开/p'
```
### 1.5 指定匹配的行数
```
cat test.txt |sed -n '1,1p'
```
# 二、删除

### 2.1 删除指定行
```
cat test.txt |sed '/展开/d'
```
### 2.2 删除开头空行
```
cat test.txt |sed /^[[:space:]]*$/d
```
### 2.3 删除^M
```
cat test.txt |tr -d "\r"
```

### 2.4 删除html标签
```
sed 's/<[^>]*>//g'
```
# 三、输出

### 指定输出分隔符
```
cat test.txt |awk 'ORS="<br/>" {print $0}'
```

