#! bin/bash
# -------------------------------------------------------------------------------
# 文件名:  Shell学习总结之变量引用
# 版 本:   1.0
# 创建日期: 2014/02/15
# 描 述:   对shell变量的引用方式很多，用这些方式可以方便的获取shell变量的值，变量值的长度，变量的一个字串，变量被部分替换后的值等等
# 作 者:   毕小朋
# 邮 箱:   wirelessqa.me@gmail.com
# 博 客:   http://blog.csdn.net/wirelessqa
# -------------------------------------------------------------------------------

function show_var_info()
{

cat <<EOF
# -------------------------------------------------------
# =============  变量使用需知 ==========
# -------------------------------------------------------
# 1. 首个字符必须为字母（a-z，A-Z）
# 2. 中间不能有空格，可以使用下划线（_）
# 3. 不能使用标点符号
# 4. 不能使用bash里的关键字（可用help命令查看保留关键字） 
# 5. 需要给变量赋值时，可以这么写：变量名=值 
# 6. “=”是赋值符号。两边不能直接跟空格，否则shell将视为命令。
# 7. string是被赋予的变量值。若string中包含空格、制表符和换行符，则string必须用单双引号将其括起来。双引号了允许使用变量替换，单引号内不能。

EOF
}

var="http://blog.csdn.net/wirelessqa"
str_echo="echo "
str_quote_explain="# ====== 引用格式:"
str_result="# >-"

function show_example_title()
{
	echo ""
	echo ${str_quote_explain} $1
}

function show_example()
{
	echo "$str_echo$1 $str_result $2"
}

function var_instead_extend()
{
echo ""
echo "# -------------------------------------------------------"
echo "# =============  变量引用扩展 =========="
echo "# -------------------------------------------------------"

cat <<EOF
var="http://blog.csdn.net/wirelessqa"
var_empty=
var_empty2=
var_empty3=

EOF

var="http://blog.csdn.net/wirelessqa"
local var_empty=
local var_empty2=
local var_empty3=

cat <<EOF
# ====== 引用格式:1. \${var-DEFAULT}:如果var未被声明，则以default作为其值,同\${var=DEFAULT}

##例1. var已被声明,以声明的值作为其值
\${var-default} #<- ${var-default}
\${var=default} #<- ${var=default}

##例2. var未被声明,以default为其值
\${var_no-default} #<- ${var_no-default}
\${var_no=default} #<- ${var_no=default}

# ====== 引用格式:2. \${var:-DEFAULT}:如果var未被声明或其值为空，则以DEFAULT作为其值,同\${var:=DEFAULT}

##例1.var为空，以default为其值
\${var_empty:-default} #<- ${var_empty:-default}
\${var_empty:=default} #<- ${var_empty:=default}

##例2. var未被声明，以default为其值
\${var_no:-default} #<- ${var_no:-default}
\${var_no:=default} #<- ${var_no:=default}

##例3. var已被声明,以声明的值作为其值
\${var:-default} #<- ${var:-default}
\${var:=default} #<- ${var:=default}

# ====== 引用格式:3. \${var+OTHER}:如果var被声明了，那么其值就是OTHER，否则为空

##例1. var被声明，值为OTHER
\${var+i am other} #<- ${var+i am other}

##例2. var没有被声明,值为空
\${var_nono+i am other} #<- ${var_nono+i am other}

##例3. var为空,值也为OTHER
\${var_empty2+i am other} #<- ${var_empty2+i am other}

# ====== 引用格式:4. \${var:+OTHER}:如果var被声明了或其值不为空，那么其值就是OTHER，否则就为空

##例1. var被声明，值为OTHER
\${var:+i am other} #<- ${var:+i am other}

##例2. var没有被声明,值为空
\${var_nonono:+i am other} #<- ${var_nonono:+i am other}

##例3. var为空,值为空
\${var_empty3:+i am other} #<- ${var_empty3:+i am other}

# ====== 引用格式:5. \${!varprefix*}:匹配之前所有以varprefix开头进行声明的变量

\${!var*} #<- ${!var*}

# ====== 引用格式:6. \${!varprefix@}:匹配之前所有以varprefix开头进行声明的变量

\${!var@} #<- ${!var@}

EOF

}

show_var_info

echo "# -------------------------------------------------------"
echo "# =============  常见变量引用 =========="
echo "# -------------------------------------------------------"

echo "var="http://blog.csdn.net/wirelessqa""
show_example_title "\$var 返回变量值"
show_example "\$var" $var

show_example_title "\${var} 返回变量值,推荐此写法,可使代码的可读性更好,避免歧义"
show_example "\${var}" ${var}

show_example_title "\${#var} 返回字符串的长度"
show_example "\${#var}" ${#var}

show_example_title "\${var:start_index} 返回从start_index一直到字符串末尾,start_index为0-x,返回倒数第x个字符到末尾"
show_example "\${var:0}" ${var:0}
show_example "\${var:10}" ${var:10}
show_example "\${var:0-10}" ${var:0-10}

show_example_title "\${var:start_index:length} 返回从start_index开始的length个字符,length为要截取的字符串长度"
show_example "\${var:0:10}" ${var:0:10}

show_example_title "\${var#string} 返回从左边删除string前的字符串,包括string,它会匹配最近的那个字符"
show_example "\${var#*/}" ${var#*/}
show_example "\${var#*n}" ${var#*n}

show_example_title "\${var##string} 返回从左边删除string前的字符串,包括string,它会匹配最远的那个字符"
show_example "\${var##*/" ${var##*/}
show_example "\${var##*n" ${var##*n}

show_example_title "\${var%string} 返回从右边删除string后的字符串,包括string,它会匹配最近的那个字符"
show_example "\${var%n*}" ${var%n*}
show_example "\${var%/*}" ${var%/*}

show_example_title "\${var%%string} 返回从右边删除string后的字符串,包括string,它会匹配最远的那个字符"
show_example "\${var%%n*}" ${var%%n*}
show_example "\${var%%/*}" ${var%%/*}

show_example_title "\${var/substring/newstring}" 返回把匹配到的第一个substring替换成newstring
show_example "\${var///bixiaopeng}" ${var/\//bixiaopeng}

show_example_title "\${var//substring/newstring}" 返回把匹配到的第一个substring替换成newstring
show_example "\${var////bixiaopeng}" ${var//\//bixiaopeng}

show_example_title "\$(command) 返回command命令执行后的结果，相当于\`command\`"
show_example "\$(date)" $(date)
show_example "\`(date)\`" `date`

show_example_title "\$((算术表达式)) 返回算术运算的结果" 
show_example "\$((2 + 3 * 5 / 5))" $((2 + 3 * 5 / 5))

var_instead_extend