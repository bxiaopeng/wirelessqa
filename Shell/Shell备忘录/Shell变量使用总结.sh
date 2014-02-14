#! bin/bash


#整理变量http://bashrc.blog.51cto.com/7339808/1228336
#http://www.cnblogs.com/barrychiao/archive/2012/10/22/2733210.html

function var_escape()
{
cat <<EOF
========= 用转义符\，屏蔽下一个字符的特殊意义
========= 特殊字符及其意义 ========= 
&  :传递到脚本的参数数量
*  :0个或多个在*字符前的那个普通字符
+  :匹配1个或多个在其之前的普通字符
^  :匹配行首，或后面字符的非
\$  :命令退出状态，0表示没错误，非0...
\`  :反引号，shell引用符号，解析命令
"  :双引用，shell引用符号
|  :管道符号或表示“或”意义
?  :管道符号或表示“或”意义
\\  :转义符本身

========= 转义符后跟字母表示的特殊意义：========= 
\n     :换行
\r     :回车
\t     :Tab键
\v或\f :换行但光标停留在原来位置
\b     :Backspace键
\a     :警报声
\0xx   :ASCII码0xx对应字符

EOF


}

function var_instead()
{

cat <<EOF
首个字符必须为字母（a-z，A-Z）
中间不能有空格，可以使用下划线（_）
不能使用标点符号
不能使用bash里的关键字（可用help命令查看保留关键字） 
需要给变量赋值时，可以这么写：变量名=值 
  “=”是赋值符号。两边不能直接跟空格，否则shell将视为命令。
  string是被赋予的变量值。若string中包含空格、制表符和换行符，则string必须用单双引号将其括起来。双引号了允许使用变量替换，单引号内不能。
EOF
}


function var_instead_extend()
{
echo "=============  变量替换扩展 =========="

cat <<EOF
var="hello xiaopeng"
var_empty=
var_empty2=
var_empty3=

EOF

var="hello xiaopeng"
var_empty=
var_empty2=
var_empty3=

cat <<EOF
#== 1. \${var-DEFAULT}:如果var未被声明，则以default作为其值,同\${var=DEFAULT}

##例1. var已被声明,以声明的值作为其值
\${var-default} #<- ${var-default}
\${var=default} #<- ${var=default}

##例2. var未被声明,以default为其值
\${var_no-default} #<- ${var_no-default}
\${var_no=default} #<- ${var_no=default}

#== 2. \${var:-DEFAULT}:如果var未被声明或其值为空，则以DEFAULT作为其值,同\${var:=DEFAULT}

##例1.var为空，以default为其值
\${var_empty:-default} #<- ${var_empty:-default}
\${var_empty:=default} #<- ${var_empty:=default}

##例2. var未被声明，以default为其值
\${var_no:-default} #<- ${var_no:-default}
\${var_no:=default} #<- ${var_no:=default}

##例3. var已被声明,以声明的值作为其值
\${var:-default} #<- ${var:-default}
\${var:=default} #<- ${var:=default}

#== 3. \${var+OTHER}:如果var被声明了，那么其值就是OTHER，否则为空

##例1. var被声明，值为OTHER
\${var+i am other} #<- ${var+i am other}

##例2. var没有被声明,值为空
\${var_nono+i am other} #<- ${var_nono+i am other}

##例3. var为空,值也为OTHER
\${var_empty2+i am other} #<- ${var_empty2+i am other}

#== 4. \${var:+OTHER}:如果var被声明了或其值不为空，那么其值就是OTHER，否则就为空

##例1. var被声明，值为OTHER
\${var:+i am other} #<- ${var:+i am other}

##例2. var没有被声明,值为空
\${var_nonono:+i am other} #<- ${var_nonono:+i am other}

##例3. var为空,值为空
\${var_empty3:+i am other} #<- ${var_empty3:+i am other}

#== 5. \${!varprefix*}:匹配之前所有以varprefix开头进行声明的变量

\${!var*} #<- ${!var*}

#== 6. \${!varprefix@}:匹配之前所有以varprefix开头进行声明的变量

\${!var@} #<- ${!var@}

EOF

}

#var_instead_extend

var_escape