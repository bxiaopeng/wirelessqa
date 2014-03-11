
## 一. 宏定义是什么

宏定义是C提供的三种预处理功能的其中一种，这三种预处理包括：宏定义、文件包含、条件编译。

## 二. 不带参数的宏定义

### 2.1 不带参数的宏定义
宏定义又称为宏代换、宏替换，简称“宏”。 　　

```
格式：#define 标识符 字符串 　　
```
- 标识符就是所谓的符号常量，也称为“宏名”

- 字符串可以是常数、表达式、格式串等。 

在编译预处理时，对程序中所有出现的“宏名”，都用宏定义中的字符串去代换，这称为“宏代换”或“宏展开”。宏定义是由源程序中的宏定义命令完成的。宏代换是由预处理程序自动完成的。

- 掌握"宏"概念的关键是“换”。 

一切以换为前提、做任何事情之前先要换，准确理解之前就要“换”。 即在对相关命令或语句的含义和功能作具体分析之前就要换： 　　

```
例：#define PI 3.1415926 　　
```

把程序中出现的PI全部换成3.1415926

### 2.2 宏定义需知 　　

```
（1）宏名一般用大写 ；　　
（2）使用宏可提高程序的通用性和易读性，减少不一致性，减少输入错误和便于修改。例如：数组大小常用宏定义 ；　　
（3）预处理是在编译之前的处理，而编译工作的任务之一就是语法检查，预处理不做语法检查； 　　
（4）宏定义末尾不加分号； 　
（5）宏定义写在函数的花括号外边，作用域为其后的程序，通常在文件的最开头； 　　
（6）可以用#undef命令终止宏定义的作用域 ；　　
（7）宏定义可以嵌套； 　　
（8）字符串" "中永远不包含宏； 　　
（9）宏定义不分配内存，变量定义分配内存； 　　
（10）宏定义不存在类型问题，它的参数也是无类型的。
```

## 三.带参数的宏定义（函数式宏定义）：

### 3.1 函数式宏定义

除了一般的字符串替换，还要做参数代换。 若字符串是表达式，我们称之为函数式宏定义。　　

```
#define 宏名（参数表） 字符串
```

### 3.2 函数式替换举例

```
#define S(a,b) a*b 　　

area=S(3,2)；

//第一步被换为area=a*b; ，第二步被换为area=3*2;
```

### 3.3 函数式宏需知


```
　
（1）实参如果是表达式容易出问题 　
　
	#define S(r) r*r 

	 area=S(a+b);

// 第一步换为area=r*r;,第二步被换为area=a+b*a+b;
// 正确的宏定义是#define S(r) ((r)*(r)) 　　

（2）宏名和参数的括号间不能有空格 　　

（3）宏替换只作替换，不做计算，不做表达式求解 　　

（4）函数调用在编译后程序运行时进行，并且分配内存。宏替换在编译前进行，不分配内存 　　

（5）宏的哑实结合不存在类型，也没有类型转换。 　　

（6）函数只有一个返回值，利用宏则可以设法得到多个值 　　

（7）宏展开使源程序变长，函数调用不会 　　

（8）宏展开不占运行时间，只占编译时间，函数调用占运行时间（分配内存、保留现场、值传递、返回值）

```


### 3.4 函数式宏定义和普通函数的区别：


```
函数式宏定义：#define MAX(a,b) ((a)>(b)?(a):(b))
普通函： MAX(a,b) { return a>b?a:b;}
```

```
（1）函数式宏定义的参数没有类型，预处理器只负责做形式上的替换，而不做参数类型检查，所以传参时要格外小心。

（2）调用真正函数的代码和调用函数式宏定义的代码编译生成的指令不同。

如果MAX是个普通函数，那么它的函数体return a > b ? a : b; 要编译生成指令，代码中出现的每次调用也要编译生成传参指令和call指令。

而如果MAX是个函数式宏定义，这个宏定义本身倒不必编译生成指令，但是代码中出现的每次调用编译生成的指令都相当于一个函数体，而不是简单的几条传参指令和call指令。所以，使用函数式宏定义编译生成的目标文件会比较大。

（3）函数式宏定义要注意格式，尤其是括号。

如果上面的函数式宏定义写成 #define MAX(a, b) (a>b?a:b)，省去内层括号，则宏展开就成了k = (i&0x0f>j&0x0f?i&0x0f:j&0x0f)，运算的优先级就错了。

同样道理，这个宏定义的外层括号也是不能省的。若函数中是宏替换为 ++MAX(a,b)，则宏展开就成了 ++(a)>(b)?(a):(b)，运算优先级也是错了。

（4）若函数参数为表达式，则普通函数的调用与函数式宏定义的替换过程是不一样的。

普通函数调用时先求实参表达式的值再传给形参，如果实参表达式有Side Effect，那么这些SideEffect只发生一次。例如MAX(++a, ++b)，如果MAX是普通函数，a和b只增加一次。

但如果MAX函数式宏定义，则要展开成k = ((++a)>(++b)?(++a):(++b))，a和b就不一定是增加一次还是两次了。所以若参数是表达式，替换函数式宏定义时一定要仔细看好。

（5）函数式宏定义往往会导致较低的代码执行效率： 

#define MAX(a, b) ((a)>(b)?(a):(b))

int a[] = { 9, 3, 5, 2, 1, 0, 8, 7, 6, 4 };

int max(int n)
{
    return n == 0 ? a[0] : MAX(a[n], max(n-1));
}

int main(void)
{
    max(9);
    return 0;
}

若是普通函数，则通过递归，可取的最大值，时间复杂度为O（n）。
但若是函数式宏定义，则宏展开为( a[n]>max(n-1)?a[n]:max(n-1) )，其中max(n-1)被调用了两遍，这样依此递归下去，时间复杂度会很高。 
尽管函数式宏定义和普通函数相比有很多缺点，但只要小心使用还是会显著提高代码的执行效率，毕竟省去了分配和释放栈帧、传参、传返回值等一系列工作，因此那些简短并且被频繁调用的函数经常用函数式宏定义来代替实现。

```



## 四.宏定义其他冷门、重点知识 　　


### 4.1 define用法 　　

用无参宏定义一个简单的常量 　　

```
#define LEN 12 　　// 这个是最常见的用法，但也会出错。 　　
```

比如下面几个知识点你会吗？可以看下： 　　

```

（1） #define NAME "zhangyuncong"//程序中有"NAME"，那它会不会被替换呢？ 　　

（2） #define 0x abcd //可以吗？也就是说，可不可以用把标识符的字母替换成别的东西？ 　　

（3） #define NAME "zhang //这个可以吗？ 　　

（4）程序中有上面的宏定义，并且，程序里有句：NAMELIST这样，会不会被替换成"zhangyuncong"LIST 　　
　
```


四个题答案都是十分明确的： 　　

```
第一个，""内的东西不会被宏替换。这一点应该大都知道。 　　

第二个，宏定义前面的那个必须是合法的用户标识符 　　

第三个，宏定义也不是说后面东西随便写，不能把字符串的两个""拆开。 　　

第四个：只替换标识符，不替换别的东西。NAMELIST整体是个标识符，而没有NAME标识符，所以不替换。
```

也就是说，这种情况下记住：

```
  #define 第一位置第二位置 　

（1） 不替换程序中字符串里的东西。 　　

（2） 第一位置只能是合法的标识符（可以是关键字） 　　

（3） 第二位置如果有字符串，必须把""配对。 　　

（4） 只替换与第一位置完全相同的标识符 　　

还有就是老生常谈的话：记住这是简单的替换而已，不要在中间计算结果，一定要替换出表达式之后再算。
 
 ```

### 4.2 带参宏一般用法 　　

```
例: #define MAX(a,b) ((a)>(b)?(a):(b)) 　　
```

则遇到MAX(1+2,value)则会把它替换成：((1+2)>(value)?(1+2):(value)) 　　

注意事项和无参宏差不多,但还是应注意 　　

```
#define FUN(a) "a" 　　//输入FUN(345)会被替换成什么？ 　　
```
其实，如果这么写，无论宏的实参是什么，都不会影响其被替换成"a"的命运。 

也就是说，""内的字符不被当成形参，即使它和一模一样。那么我要是想让这里输入FUN(345)它就替换成"345"该怎么实现呢？ 请看下面关于#的用法 　　

### 4.3 有参宏定义中#的用法 　　

```
#define STR(str) #str 　　
```

用于把宏定义中的参数两端加上字符串的"" 　　

例如，这里STR(my#name)会被替换成"my#name" 　　


一般由任意字符都可以做形参，但以下情况会出错： 　

```
STR())这样，编译器不会把“)”当成STR()的参数。 　　

STR(,)同上，编译器不会把“,”当成STR的参数。 　　

STR(A,B)如果实参过多，则编译器会把多余的参数舍去。（VC++2008为例） 　　STR((A,B))会被解读为实参为：(A,B)，而不是被解读为两个实参，第一个是(A第二个是B)。 
　　
```

### 4.4 有参宏定义中##的用法 　　

```
#define WIDE(str) L##str 　　//会将形参str的前面加上L 　　
// WIDE("abc")就会被替换成L"abc" 　　

#define FUN(a,b) vo##a##b() 　　
// 那么FUN(id ma,in)会被替换成void main() 

```


### 4.5 多行宏定义： 　　

```
#define doit(m,n) for(int i=0;i<(n);++i)\ 　　{\ 　　m+=i;\ 　　}
```

## 五. objective-c宏定义

### 5.1 常用宏定义

```
// 是否高清屏
#define isRetina ([UIScreen instancesRespondToSelector:@selector(currentMode)] ? CGSizeEqualToSize(CGSizeMake(640, 960), [[UIScreen mainScreen] currentMode].size) : NO)
// 是否模拟器
#define isSimulator (NSNotFound != [[[UIDevice currentDevice] model] rangeOfString:@"Simulator"].location)
// 是否iPad
#define isPad (UI_USER_INTERFACE_IDIOM() == UIUserInterfaceIdiomPad)
// 是否iPad
#define someThing (UI_USER_INTERFACE_IDIOM() == UIUserInterfaceIdiomPad)? ipad: iphone

```

### 5.2 基本使用介绍

```
//定义π值 3.1415926  
#define PI 3.1415926   
//则在程序用可以如下使用     
double i=2*PI*3;   
//效果相当于  double i=2*3.1415926*3;  

//预处理命令可以定义任何符合格式的形式，例如判断年份是否闰年
#define  IS_LEAP_YEAR  year%4==0&&year%100!=0||year%400==0  
//使用时则可以直接  
if(IS_LEAP_YEAR)  
 
//或者可以定义一个参数    
#define  IS_LEAP_YEAR(y)  y%4==0&&y%100!=0||y%400==0  
//使用时则可以直接   
int ys=2012;   
if(IS_LEAP_YEAR(ys))     
  
//通常预处理程序定义在一行 如果好分行 比如说太长需要换行  需要使用“/”符号 表示还有下一行，多行分列也是如此，例：  
#Define  IS_LEAP_YEAR  year%4==0&&year%100!=0/  
           ||year%400==0   
//宏定义参数后边放一个# 那么在调用该宏时，预处理程序将根据宏参数创建C风格的常量字符串 例：  
#define STR(x) # x  
//将会使得 随后调用的    

NSLOG(STR(Programming in Objective-c./n));  
//显示结果为 Programming in Objective-c./n

```


### 5.3 宏定义中字符串化操作符#：

\#的功能是将其后面的宏参数进行字符串化操作，意思就是对它所应用的宏变量通过替换后在其左右各加上一个双引号。

```
#define WARN_IF(EXPR)\
do {\
if (EXPR)\
fprintf(stderr, "Warning: " #EXPR "\n");\
} while(0)

上面代码中的反斜线\主要用来转译换行符，即屏蔽换行符。

那么如下的代码调用：
WARN_IF(divider == 0);

将被解析为：
do {\
if (divider == 0)\
fprintf(stderr, "Warning: " "divider == 0" "\n");\
} while(0);
```

注意能够字符串化操作的必须是宏参数，不是随随便便的某个子串（token）都行的。

### 5.4 宏定义中的连接符##：

连接符##用来将两个token连接为一个token，但它不可以位于第一个token之前or最后一个token之后。

注意这里连接的对象只要是token就行，而不一定是宏参数,但是##又必须位于宏定义中才有效，因其为编译期概念（比较绕）。

```
#define LINK_MULTIPLE(a, b, c, d) a##_##b##_##c##_##d
typedef struct _record_type LINK_MULTIPLE(name, company, position, salary);
/*
* 上面的代码将被替换为
* typedef struct _record_type name_company_position_salary;
*/

又如下面的例子：
#define PARSER(N) printf("token" #N " = %d\n", token##N)

int token64 = 64;

如下调用宏：
PARSER(64);

将被解析为：
printf("token" "64" " = %d\n", token64);

在obj-c中，如果我有如下定义：
#define _X(A, B) (A#B)
#define _XX(A, B) _X([NSString stringWithFormat:@"%@_c", A], B)
gcc将报错！
正确的写法为：
#define _XX(A, B) _X(([NSString stringWithFormat:@"%@_c", A]), B)
```

### 5.5 宏定义 object-c 单例

```
#define GTMOBJECT_SINGLETON_BOILERPLATE(_object_name_, _shared_obj_name_)
static _object_name_ *z##_shared_obj_name_ = nil; 
+ (_object_name_ *)_shared_obj_name_ {            
@synchronized(self) {                           
if (z##_shared_obj_name_ == nil) {            
/* Note that ‘self’ may not be the same as _object_name_ */                              
/* first assignment done in allocWithZone but we must reassign in case init fails */     
z##_shared_obj_name_ = [[self alloc] init];                                              
_GTMDevAssert((z##_shared_obj_name_ != nil), @”didn’t catch singleton allocation”);      
}                                             
}                                               
return z##_shared_obj_name_;                    
}                                                 

+ (id)allocWithZone:(NSZone *)zone {              
@synchronized(self) {                           
if (z##_shared_obj_name_ == nil) {            
z##_shared_obj_name_ = [super allocWithZone:zone];
return z##_shared_obj_name_;                
}                                             
}                                               
 
/* We can’t return the shared instance, because it’s been init’d */
_GTMDevAssert(NO, @”use the singleton API, not alloc+init”);       
return nil;                                     
}                                                 

- (id)retain {                                    
return self;                                    
}                                                 

- (NSUInteger)retainCount {                       
return NSUIntegerMax;                           
}                                                 

- (void)release {                                 
}                                                 

- (id)autorelease {                               
return self;                                    
}                                                 

- (id)copyWithZone:(NSZone *)zone {               
return self;                                    
}
```

### 5.6 条件编译

```
#if !defined(FCDebug) || FCDebug == 0
#define FCLOG(...) do {} while (0)
#define FCLOGINFO(...) do {} while (0)
#define FCLOGERROR(...) do {} while (0)
    
#elif FCDebug == 1
#define FCLOG(...) NSLog(__VA_ARGS__)
#define FCLOGERROR(...) NSLog(__VA_ARGS__)
#define FCLOGINFO(...) do {} while (0)
    
#elif FCDebug > 1
#define FCLOG(...) NSLog(__VA_ARGS__)
#define FCLOGERROR(...) NSLog(__VA_ARGS__)
#define FCLOGINFO(...) NSLog(__VA_ARGS__)
#endif
```

## 六. C语言的预处理命令简介 ：

```
#define              定义一个预处理宏
#undef               取消宏的定义
#include            包含文件命令
#include_next   与#include相似, 但它有着特殊的用途
#if                      编译预处理中的条件命令, 相当于C语法中的if语句
#ifdef                判断某个宏是否被定义, 若已定义, 执行随后的语句
#ifndef             与#ifdef相反, 判断某个宏是否未被定义
#elif                  若#if, #ifdef, #ifndef或前面的#elif条件不满足, 则执行#elif之后的语句, 相当于C语法中的else-if
#else                与#if, #ifdef, #ifndef对应, 若这些条件不满足, 则执行#else之后的语句, 相当于C语法中的else
#endif              #if, #ifdef, #ifndef这些条件命令的结束标志.
defined            与#if, #elif配合使用, 判断某个宏是否被定义
#line                标志该语句所在的行号
#                      将宏参数替代为以参数值为内容的字符窜常量
##                   将两个相邻的标记(token)连接为一个单独的标记
#pragma        说明编译器信息#warning       显示编译警告信息
#error            显示编译错误信息
```

#### 参考文档

```
http://www.cnblogs.com/fly1988happy/archive/2012/04/10/2441402.html
http://blog.csdn.net/wangqiuyun/article/details/8104698
```

----
####  微信公众帐号: wirelessqa 
![wirelessqa](http://avatar.csdn.net/5/C/5/1_wirelessqa.jpg)

#### 关于作者：

**作者:** 毕小朋 | 老 毕  **邮箱:** <wirelessqa.me@gmail.com> 

**微博:** [@WirelessQA](http://www.weibo.com/wirelessqa) **博客:** <http://blog.csdn.net/wirelessqa>

----