## 码上开始

```
#import <Foundation/Foundation.h>

int main(int argc, const char * argv[])
{
    
    @autoreleasepool {
        
        //字典可以将数据以键值对儿的形式储存起来，取值的时候通过KEY就可以直接拿到对应的值
        
        NSLog(@"############ 不可变字典 ##############");
        
        NSLog(@"------ 用键值对创建一个字典对象,注意以nil结尾");
        NSDictionary *dic = [NSDictionary dictionaryWithObjectsAndKeys:@"老毕",@"name",@"http://blog.csdn.net/wirelessqa",@"blog", nil];
        
        NSInteger count = [dic count];
        NSLog(@"字典的数量: %li",count);
    
        NSLog(@"------ 将字典的key转成枚举对象，用于遍历");
        NSEnumerator *enuKey = [dic keyEnumerator];
        
        for (NSObject *obj in enuKey) {
            NSLog(@"key: %@",obj);
        }
        
        NSLog(@"------ 得到字典dic中所有的键");
        NSArray *keys = [dic allKeys];
        
        for (NSObject *obj in keys) {
            NSLog(@"key: %@",obj);
        }
        
        NSLog(@"------ 得到字典dic中所有的值");
        NSArray *values = [dic allValues];
        
        for (NSObject *obj in values) {
            NSLog(@"value: %@",obj);
        }
        
        //通过键得到值
        NSObject *objValue = [dic objectForKey:@"name"];
        
        if (objValue != nil) {
            NSLog(@"通过key\"name\"找到的value是: %@",objValue);
        }
        
        NSDictionary *dic2 = [NSDictionary dictionaryWithObject:@"wirelessqa" forKey:@"weibo"];
        
        NSLog(@"------ 通过数组创建一个字典");
        NSArray *arrayValue = [NSArray arrayWithObjects:@"杭州",@"30", nil];
        NSArray *arrayKey = [NSArray arrayWithObjects:@"city",@"age", nil];
        NSDictionary *dic3 = [NSDictionary dictionaryWithObjects:arrayValue forKeys:arrayKey];
        
        //通过key遍历value
        for (NSObject *obj in arrayKey) {
            NSLog(@"%@",[dic3 objectForKey:obj]);
        }
        
        //初始化新字典，新字典包含otherDic
        NSDictionary *dic4 = [NSDictionary dictionaryWithDictionary:dic2];
        for (NSObject *obj in dic4) {
            NSLog(@"dic4: %@",obj);
        }
        //NSDictionary *dic = [NSDictionary dictionaryWithContentsOfFile:path];
        
        NSLog(@"############ 创建可变的字典 ##############");
        
        //创建可变字典
        NSMutableDictionary *mutableDic = [NSMutableDictionary dictionaryWithCapacity:10];
        [mutableDic setObject:@"老毕" forKey:@"name"];
        [mutableDic setObject:@"http://blog.csdn.net/wirelessqa" forKey:@"博客"];
        
        //通过KEY找到value
        NSObject *object = [mutableDic objectForKey:@"name"];
        
        if (object != nil) {
            NSLog(@"key\"name\",value: %@",object);
        }
        
        NSLog(@"------ 向字典mutableDic对象中添加整个字典对象dic");
        [mutableDic addEntriesFromDictionary:dic];
        NSArray *keyArray = [mutableDic allKeys];
        
        for (NSObject *obj in keyArray) {
            NSLog(@"mutableDic: key: %@ , value: %@",obj,[mutableDic objectForKey:obj]);
        }
        
        NSLog(@"------ 向字典mutableDic对象中追加一个键值对");
        [mutableDic setObject:@"http://www.weibo.com/wirelessqa" forKey:@"微博"];

        keyArray = [mutableDic allKeys];
        
        for (NSObject *obj in keyArray) {
            NSLog(@"mutableDic: key: %@ , value: %@",obj,[mutableDic objectForKey:obj]);
        }
        
        NSLog(@"------ 创建一个为空的可变字典");
        NSMutableDictionary *dicEmpty = [NSMutableDictionary dictionary];
        //给空字典赋值
        [dicEmpty setDictionary:mutableDic];
        
        keyArray = [dicEmpty allKeys];
        
        for (NSObject *obj in keyArray) {
            NSLog(@"dicEmpty: key: %@ , value: %@",obj,[mutableDic objectForKey:obj]);
        }
        

    }
    return 0;
}

```

## 运行结果

```
2014-03-15 20:59:39.510 TestArray[96480:303] ############ 不可变字典 ##############
2014-03-15 20:59:39.511 TestArray[96480:303] ------ 用键值对创建一个字典对象,注意以nil结尾
2014-03-15 20:59:39.512 TestArray[96480:303] 字典的数量: 2
2014-03-15 20:59:39.512 TestArray[96480:303] ------ 将字典的key转成枚举对象，用于遍历
2014-03-15 20:59:39.516 TestArray[96480:303] key: name
2014-03-15 20:59:39.517 TestArray[96480:303] key: blog
2014-03-15 20:59:39.517 TestArray[96480:303] ------ 得到字典dic中所有的键
2014-03-15 20:59:39.517 TestArray[96480:303] key: name
2014-03-15 20:59:39.518 TestArray[96480:303] key: blog
2014-03-15 20:59:39.518 TestArray[96480:303] ------ 得到字典dic中所有的值
2014-03-15 20:59:39.518 TestArray[96480:303] value: 老毕
2014-03-15 20:59:39.518 TestArray[96480:303] value: http://blog.csdn.net/wirelessqa
2014-03-15 20:59:39.519 TestArray[96480:303] 通过key"name"找到的value是: 老毕
2014-03-15 20:59:39.519 TestArray[96480:303] ------ 通过数组创建一个字典
2014-03-15 20:59:39.519 TestArray[96480:303] 杭州
2014-03-15 20:59:39.520 TestArray[96480:303] 30
2014-03-15 20:59:39.520 TestArray[96480:303] dic4: weibo
2014-03-15 20:59:39.520 TestArray[96480:303] ############ 创建可变的字典 ##############
2014-03-15 20:59:39.521 TestArray[96480:303] key"name",value: 老毕
2014-03-15 20:59:39.521 TestArray[96480:303] ------ 向字典mutableDic对象中添加整个字典对象dic
2014-03-15 20:59:39.521 TestArray[96480:303] mutableDic: key: 博客 , value: http://blog.csdn.net/wirelessqa
2014-03-15 20:59:39.522 TestArray[96480:303] mutableDic: key: blog , value: http://blog.csdn.net/wirelessqa
2014-03-15 20:59:39.522 TestArray[96480:303] mutableDic: key: name , value: 老毕
2014-03-15 20:59:39.522 TestArray[96480:303] ------ 向字典mutableDic对象中追加一个键值对
2014-03-15 20:59:39.523 TestArray[96480:303] mutableDic: key: 博客 , value: http://blog.csdn.net/wirelessqa
2014-03-15 20:59:39.523 TestArray[96480:303] mutableDic: key: 微博 , value: http://www.weibo.com/wirelessqa
2014-03-15 20:59:39.523 TestArray[96480:303] mutableDic: key: blog , value: http://blog.csdn.net/wirelessqa
2014-03-15 20:59:39.523 TestArray[96480:303] mutableDic: key: name , value: 老毕
2014-03-15 20:59:39.524 TestArray[96480:303] ------ 创建一个为空的可变字典
2014-03-15 20:59:39.524 TestArray[96480:303] dicEmpty: key: name , value: 老毕
2014-03-15 20:59:39.524 TestArray[96480:303] dicEmpty: key: 博客 , value: http://blog.csdn.net/wirelessqa
2014-03-15 20:59:39.525 TestArray[96480:303] dicEmpty: key: blog , value: http://blog.csdn.net/wirelessqa
2014-03-15 20:59:39.525 TestArray[96480:303] dicEmpty: key: 微博 , value: http://www.weibo.com/wirelessqa
Program ended with exit code: 0
```

----
####  微信公众帐号: wirelessqa 
![wirelessqa](https://github.com/bxiaopeng/wirelessqa/raw/master/img/qrcode_for_gh_fdde1fe2880a_258.jpg)

#### 关于作者：

**作者:** 毕小朋 | 老 毕  **邮箱:** <wirelessqa.me@gmail.com> 

**微博:** [@WirelessQA](http://www.weibo.com/wirelessqa) **博客:** <http://blog.csdn.net/wirelessqa>

----