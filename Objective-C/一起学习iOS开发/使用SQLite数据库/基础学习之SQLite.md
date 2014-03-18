
## 创建数据库过程需要3个步骤：

1、使用sqlite3_open函数打开数据库；

2、使用sqlite3_exec函数执行Create Table语句，创建数据库表；

3、使用sqlite3_close函数释放资源。


### 查询数据

数据查询一般会带有查询条件，这个使用SQL语句where子句很容易实现，但是在程序中需要动态绑定参数给where子句。执行查询数据步骤如下：

1、使用sqlite3_open函数打开数据库；

2、使用sqlite3_prepare_v2函数预处理SQL语句；

3、使用sqlite3_bind_text函数绑定参数；

4、使用sqlite3_step函数执行SQL语句，遍历结果集；

5、使用sqlite3_column_text等函数提取字段数据；

6、使用sqlite3_finalize和sqlite3_close函数释放资源。


参考:http://www.cnblogs.com/iOS-Blog/p/3197600.html





## 2.qlite3函数功能简介

1) 基本函数及结构体

```
sqlite3*pdb //数据库句柄，跟文件句柄FILE很类似
sqlite3_stmt  *stmt  //这个相当于ODBC的Command对象，用于保存编译好的SQL语句
sqlite3_open()       //打开数据库
sqlite3_exec()       //执行非查询的sql语句
sqlite3_prepare()    //准备sql语句，执行select语句或者要使用parameter bind时                         用这个函数（封装了sqlite3_exec）.
sqlite3_step()      //在调用sqlite3_prepare后，使用这个函数在记录集中移动。
sqlite3_close()     //关闭数据库文件
```

2）绑定函数

 ```
 int sqlite3_bind_null(sqlite3_stmt*, int);
 int sqlite3_bind_int(sqlite3_stmt*, int, int);
 int sqlite3_bind_text(sqlite3_stmt*, int, const char*, int n, void(*)(void*));
 int sqlite3_bind_blob(sqlite3_stmt*, int, const void*, int n, void(*)(void*));
```
 
3）取值函数

```
sqlite3_column_text() //取text类型的数据
sqlite3_column_blob() //取blob类型的数据
sqlite3_column_int() //取int类型的数据
```
 

## 3. Sqlite3使用步骤

```
1) 首先获取iPhone上Sqlite3的数据库文件的地址
2) 打开Sqlite3的数据库文件
3) 定义SQL文
4) 邦定执行SQL所需要的参数
5) 执行SQL文，并获取结果
6) 释放资源
7) 关闭Sqlite3数据库。
```

查询数据

数据查询一般会带有查询条件，这个使用SQL语句where子句很容易实现，但是在程序中需要动态绑定参数给where子句。执行查询数据步骤如下：

```
1、使用sqlite3_open函数打开数据库；

2、使用sqlite3_prepare_v2函数预处理SQL语句；

3、使用sqlite3_bind_text函数绑定参数；

4、使用sqlite3_step函数执行SQL语句，遍历结果集；

5、使用sqlite3_column_text等函数提取字段数据；

6、使用sqlite3_finalize和sqlite3_close函数释放资源。
```

## 4.Sqlite3数据操作

由于整个例子代码比较繁琐，这里只列出数据库操作的部分代码作为参考：

```
1.添加开发包libsqlite3.0.dylib

首先是设置项目文件，在项目中添加iPhone版的sqlite3的数据库的开发包，在项目下的Frameworks点击右键，然后选择libsqlite3.0.dylib文件。

libsqlite3.0.dylib文件地址: 

/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS2.2.sdk/usr/lib/libsqlite3.0.dylib

2.获取sqlite3的数据库文件地址：

//数据库路径 

-(NSString*)databasePath 

{

NSArray *path = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES); 

NSString *pathname = [path objectAtIndex:0]; 

return [pathname stringByAppendingPathComponent:@”database.sqlite3”]; 

} 


3.打开数据库

- (BOOL)openDatabase  

{ 

    if (sqlite3_open([[self databasePath] UTF8String],&database) != SQLITE_OK) 

    { 

    sqlite3_close(database); 

    printf("failed to open the database"); 

    return NO;

    }

    else 

    {

    printf("open the database successfully"); 

    return YES;

    }

} 

4.创建表

//创建TimerTable表 

 

- (BOOL)createTimerTable 

{ 

if ([self openDatabase]==YES)

{ 

char *erroMsg; 

NSString *createSQL = [NSString stringWithFormat:@"CREATE TABLE IF NOT EXISTS %@(timerid INTEGER PRIMARY KEY AUTOINCREMENT,time INTEGER,remaintime INTEGER,iconuri BLOB,vibrate INTEGER,status INTEGER,message TEXT)",TableName]; 

if (sqlite3_exec(database, [createSQL UTF8String], NULL, NULL, &erroMsg)!= SQLITE_OK)

{ 

sqlite3_close(database); 

printf("create table faild"); 

return NO; 

} 

else 

{ 

printf("table was created"); 

return YES; 

}

} 

else 

return NO;

} 

5.添加数据

//添加Timer  

- (BOOL)insertTimer:(TimerInfo *)timerInfo 

{   

bool isOpen=[self openDatabase]; 

if (isOpen!=YES) 

{ 

  return NO; 

} 

sqlite3_stmt *statement; 

static char *insertTimerSql="INSERT INTO TimerTable(time,remaintime,iconuri,vibrate,status,message,type) VALUES (?,?,?,?,?,?)"; 

if (sqlite3_prepare_v2(database,insertTimerSql,-1,&statement,NULL)!= SQLITE_OK) 

{ 

NSLog(@"Error:Failed to insert timer"); 

return NO; 

} 

sqlite3_bind_int(statement,1,timerInfo.time);//timerInfo是一个封装了相关属性的实体类对象

sqlite3_bind_int(statement,2,timerInfo.remainTime); 

sqlite3_bind_text(statement,3,[timerInfo.iconuri UTF8String],-1,SQLITE_TRANSIENT); 

sqlite3_bind_int(statement,4,timerInfo.vibrate); 

sqlite3_bind_int(statement,5,timerInfo.status); 

sqlite3_bind_text(statement,6,[timerInfo.message UTF8String],-1,SQLITE_TRANSIENT); 

int success=sqlite3_step(statement); 

sqlite3_finalize(statement); 

if(success==SQLITE_ERROR) 

{ 

NSLog(@"Error:fail to insert into the database with message."); 

return NO; 

} 

NSLog(@"inserted one timer"); 

return YES; 

} 

6.查询数据

//查询数据库中所有的TimerInfo，返回一个包含所有TimerInfo的可变数组  

-(NSMutableArray *)getAllTimers 

{ 

NSMutableArray *arrayTimers=[[NSMutableArray alloc] init]; 

NSString *queryStr=@"SELECT * FROM TimerTable"; 

sqlite3_stmt *statement; 

if (sqlite3_prepare_v2(database, [queryStr UTF8String], -1, &statement, NULL)!=SQLITE_OK) 

{ 

printf("Failed to get all timers!
");  

} 

else 

{ 

while (sqlite3_step(statement)==SQLITE_ROW) 

{ 

TimerInfo *timerInfo=[[TimerInfo alloc] init];

timerInfo.timerId =sqlite3_column_int(statement,0);

timerInfo.time =sqlite3_column_int(statement,1); 

timerInfo.remainTime=sqlite3_column_int(statement,2); 

timerInfo.vibrate =sqlite3_column_int(statement,4);

timerInfo.status = sqlite3_column_int(statement,5); 

char *messageChar=sqlite3_column_text(statement,6);

if (messageChar==NULL) 

timerInfo.message=nil; 

else 

timerInfo.message =[NSString stringWithUTF8String:messageChar]; 

[arrayTimers addObject:timerInfo]; 

[timerInfo release]; 

} 

} 
sqlite3_finalize(statement); 

NSLog(@"arrayTimersCount: %i",[arrayTimers count]);

return arrayTimers;

} 

```


----
####  微信公众帐号: wirelessqa 
![wirelessqa](https://github.com/bxiaopeng/wirelessqa/raw/master/img/qrcode_for_gh_fdde1fe2880a_258.jpg)

#### 关于作者：

**作者:** 毕小朋 | 老 毕  **邮箱:** <wirelessqa.me@gmail.com> 

**微博:** [@WirelessQA](http://www.weibo.com/wirelessqa) **博客:** <http://blog.csdn.net/wirelessqa>

----