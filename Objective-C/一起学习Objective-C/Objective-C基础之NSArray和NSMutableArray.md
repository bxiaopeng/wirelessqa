## 码上开始

```
//
//  main.m
//  TestArray
//  本文主要分三部分:1. 不可变数组 2. 可变数组  3. 数组遍历方法
//  Created by bixiaopeng on 14-3-12.
//  Copyright (c) 2014年 bixiaopeng. All rights reserved.
//

#import <Foundation/Foundation.h>

int main(int argc, const char * argv[])
{

    @autoreleasepool {
        
        NSLog(@"=================================================");
        NSLog(@"==================== 1. 不可变数组 ================");
        NSLog(@"=================================================");
        //数组可以一次性添加完全，以nil作为结尾标志。
        NSArray *array =[NSArray arrayWithObjects:@"老毕",@"男",@"码农",@"http://blog.csdn.net/wirelessqa",nil];
        
        NSLog(@"----- 获得数组的长度");
        NSUInteger length = [array count];
        
        NSLog(@"array数组的长度为:%li",length);
        
        NSLog(@"----- 通过index得到数组的值");
        NSLog(@"array数组第一个值为:%@",[array objectAtIndex: 0]);
        NSLog(@"array数组第二个值为:%@",[array objectAtIndex: 1]);
        NSLog(@"array数组第三个值为:%@",[array objectAtIndex: 2]);
        NSLog(@"array数组第四个值为:%@",[array objectAtIndex: 3]);
        
        NSLog(@"----- 某个对象在数组中的位置");
        NSLog(@"\"老毕\"在array数组中的位置:%li",[array indexOfObject:@"老毕"]);
        NSLog(@"\"男\"在array数组中的位置:%li",[array indexOfObject:@"男"]);
        NSLog(@"\"攻城狮\"在array数组中的位置:%li",[array indexOfObject:@"攻城狮"]);
        NSLog(@"\"http://blog.csdn.net/wirelessqa\"在array数组中的位置:%li",[array indexOfObject:@"http://blog.csdn.net/wirelessqa"]);
        
        NSLog(@"----- 判断某个对象是否在数组中");
        if([array indexOfObject:@"微博"] == NSNotFound){
            NSLog(@"\"微博\"没在array数组中");
            
        }
        NSLog(@"----- 如果要添加空的话可以用以下方法");
        NSArray *array_null=[NSArray arrayWithObjects:@"dancer",[NSNull null], nil];
        NSLog(@"null %@",[array_null objectAtIndex:1]);
        
        NSLog(@"----- 遍历数组");
        for (NSObject *object in array) {
            NSLog(@"%@",object);
        }
        NSLog(@"----- 返回该数组内容的字符串,并格式化为属性列表");
        NSLog(@"%@",[array description]);
        NSLog(@"----- 返回数组中的第一个对象");
        NSLog(@"%@",[array firstObject]);
        NSLog(@"----- 返回数组中的最后一个对象");
        NSLog(@"%@",[array lastObject]);
        NSLog(@"----- 判断两个数组是否相等");
        NSLog(@"%i",[array isEqualToArray:array_null]);
        NSLog(@"%i",[array isEqualToArray:array]);
        
        NSArray *halfArray;
        NSRange theRange;
        NSLog(@"----- 获取一个数组中的一个子集");
        theRange.location = 0;
        theRange.length = [array count] / 2;
        
        halfArray = [array subarrayWithRange:theRange];
        //遍历新数组
        for (NSObject *object in halfArray) {
            NSLog(@"%@",object);
        }
        
        NSLog(@"=================================================");
        NSLog(@"==================== 2. 可变数组 =================");
        NSLog(@"=================================================");
        NSLog(@"----- 创建一个可变的数组容量为8,超出8以后NSMutableArray会自动扩充");
        NSMutableArray *mb_array = [NSMutableArray arrayWithCapacity:8];
        
        NSLog(@"----- addObject向可变数组尾部添加数据对象");
        [mb_array addObject:@"小毕"];
        [mb_array addObject:@"bixiaopeng"];
        [mb_array addObject:@"wirelessqa"];
        [mb_array addObject:@"男"];
        [mb_array addObject:@"帅"];
        
        //遍历数组
        for (NSObject *object in mb_array) {
            NSLog(@"%@",object);
        }
        
        
        NSLog(@"----- 用addObjectsFromArray向可变数组尾部添加数据对象");
        [mb_array addObjectsFromArray:array];
        //遍历数组
        for (NSObject *object in mb_array) {
            NSLog(@"%@",object);
        }
        
        NSLog(@"----- [array removeObject:(id)] :无需考虑范围，主要数组中存在这个对象就会直接被删除。");
        [mb_array removeObject:@"小毕"];
        //遍历数组
        for (NSObject *object in mb_array) {
            NSLog(@"%@",object);
        }
        
        NSLog(@"----- [array removeObjectAtIndex:(NSUInteger)]:删除数组中指定脚标索引的数据。");
        
        [mb_array removeObjectAtIndex:0];
        for (NSObject *object in mb_array) {
            NSLog(@"%@",object);
        }
        
        NSLog(@"----- [array removeObjectIdenticalTo:(id)] : 删除数组中指定元素");
        [mb_array removeObjectIdenticalTo:@"wirelessqa"];
        for (NSObject *object in mb_array) {
            NSLog(@"%@",object);
        }
        
        NSRange rang = NSMakeRange(0, 2);
        NSLog(@"----- [array removeObjectIdenticalTo:(id) inRange:(NSRange)] : 在指定范围内删除指定的元素。");
        [mb_array removeObjectIdenticalTo:@"男" inRange:rang];
        
        for (NSObject *object in mb_array) {
            NSLog(@"%@",object);
        }
        
        NSLog(@"----- [array removeObjectsInArray:(NSArray *)] :删除一个数组的元素。");
        [mb_array removeObjectsInArray:array];
        
        for (NSObject *object in mb_array) {
            NSLog(@"%@",object);
        }
        
        NSLog(@"----- 替换脚标元素replaceObjectAtIndex");
        
        NSInteger i =[mb_array indexOfObject:@"帅"];
        [mb_array replaceObjectAtIndex:i withObject:@"老毕非常帅"];
        NSLog(@"%@",[mb_array objectAtIndex:i]);
        
        NSLog(@"----- 向数组中插入一个数据");
        [mb_array insertObject:@"同意" atIndex:i];
        NSLog(@"%@",[mb_array objectAtIndex:i+1]);
        NSLog(@"%@",[mb_array objectAtIndex:i]);
        
        NSLog(@"========================== 3.数组遍历 ==========================");
        
        NSLog(@"--- 遍历数组方法一");
        for (int i = 0; i< [array count]; i++) {
            NSLog(@"%@",[array objectAtIndex:i]);
        }
        
        NSLog(@"--- 遍历数组方法二");
        id obj;
        NSEnumerator *enumerator = [array objectEnumerator];
        while (obj=[enumerator nextObject]) {
            NSLog(@"%@",obj);
        }
        
        NSLog(@"--- 遍历数组方法三");
        for (NSObject *object in array) {
            NSLog(@"%@",object);
        }
        
        
    }
    return 0;
}

```

## 日志输出

```
2014-03-14 16:38:52.519 TestArray[90645:303] =================================================
2014-03-14 16:38:52.520 TestArray[90645:303] ==================== 1. 不可变数组 ================
2014-03-14 16:38:52.520 TestArray[90645:303] =================================================
2014-03-14 16:38:52.521 TestArray[90645:303] ----- 获得数组的长度
2014-03-14 16:38:52.521 TestArray[90645:303] array数组的长度为:4
2014-03-14 16:38:52.521 TestArray[90645:303] ----- 通过index得到数组的值
2014-03-14 16:38:52.522 TestArray[90645:303] array数组第一个值为:老毕
2014-03-14 16:38:52.522 TestArray[90645:303] array数组第二个值为:男
2014-03-14 16:38:52.522 TestArray[90645:303] array数组第三个值为:码农
2014-03-14 16:38:52.522 TestArray[90645:303] array数组第四个值为:http://blog.csdn.net/wirelessqa
2014-03-14 16:38:52.523 TestArray[90645:303] ----- 某个对象在数组中的位置
2014-03-14 16:38:52.523 TestArray[90645:303] "老毕"在array数组中的位置:0
2014-03-14 16:38:52.523 TestArray[90645:303] "男"在array数组中的位置:1
2014-03-14 16:38:52.524 TestArray[90645:303] "攻城狮"在array数组中的位置:9223372036854775807
2014-03-14 16:38:52.524 TestArray[90645:303] "http://blog.csdn.net/wirelessqa"在array数组中的位置:3
2014-03-14 16:38:52.525 TestArray[90645:303] ----- 判断某个对象是否在数组中
2014-03-14 16:38:52.525 TestArray[90645:303] "微博"没在array数组中
2014-03-14 16:38:52.525 TestArray[90645:303] ----- 如果要添加空的话可以用以下方法
2014-03-14 16:38:52.526 TestArray[90645:303] null <null>
2014-03-14 16:38:52.526 TestArray[90645:303] ----- 遍历数组
2014-03-14 16:38:52.526 TestArray[90645:303] 老毕
2014-03-14 16:38:52.527 TestArray[90645:303] 男
2014-03-14 16:38:52.527 TestArray[90645:303] 码农
2014-03-14 16:38:52.527 TestArray[90645:303] http://blog.csdn.net/wirelessqa
2014-03-14 16:38:52.527 TestArray[90645:303] ----- 返回该数组内容的字符串,并格式化为属性列表
2014-03-14 16:38:52.528 TestArray[90645:303] (
    "\U8001\U6bd5",
    "\U7537",
    "\U7801\U519c",
    "http://blog.csdn.net/wirelessqa"
)
2014-03-14 16:38:52.528 TestArray[90645:303] ----- 返回数组中的第一个对象
2014-03-14 16:38:52.528 TestArray[90645:303] 老毕
2014-03-14 16:38:52.529 TestArray[90645:303] ----- 返回数组中的最后一个对象
2014-03-14 16:38:52.529 TestArray[90645:303] http://blog.csdn.net/wirelessqa
2014-03-14 16:38:52.529 TestArray[90645:303] ----- 判断两个数组是否相等
2014-03-14 16:38:52.529 TestArray[90645:303] 0
2014-03-14 16:38:52.530 TestArray[90645:303] 1
2014-03-14 16:38:52.530 TestArray[90645:303] ----- 获取一个数组中的一个子集
2014-03-14 16:38:52.530 TestArray[90645:303] 老毕
2014-03-14 16:38:52.531 TestArray[90645:303] 男
2014-03-14 16:38:52.531 TestArray[90645:303] =================================================
2014-03-14 16:38:52.531 TestArray[90645:303] ==================== 2. 可变数组 =================
2014-03-14 16:38:52.531 TestArray[90645:303] =================================================
2014-03-14 16:38:52.532 TestArray[90645:303] ----- 创建一个可变的数组容量为8,超出8以后NSMutableArray会自动扩充
2014-03-14 16:38:52.532 TestArray[90645:303] ----- addObject向可变数组尾部添加数据对象
2014-03-14 16:38:52.532 TestArray[90645:303] 小毕
2014-03-14 16:38:52.533 TestArray[90645:303] bixiaopeng
2014-03-14 16:38:52.533 TestArray[90645:303] wirelessqa
2014-03-14 16:38:52.533 TestArray[90645:303] 男
2014-03-14 16:38:52.534 TestArray[90645:303] 帅
2014-03-14 16:38:52.534 TestArray[90645:303] ----- 用addObjectsFromArray向可变数组尾部添加数据对象
2014-03-14 16:38:52.534 TestArray[90645:303] 小毕
2014-03-14 16:38:52.534 TestArray[90645:303] bixiaopeng
2014-03-14 16:38:52.535 TestArray[90645:303] wirelessqa
2014-03-14 16:38:52.535 TestArray[90645:303] 男
2014-03-14 16:38:52.535 TestArray[90645:303] 帅
2014-03-14 16:38:52.536 TestArray[90645:303] 老毕
2014-03-14 16:38:52.536 TestArray[90645:303] 男
2014-03-14 16:38:52.536 TestArray[90645:303] 码农
2014-03-14 16:38:52.536 TestArray[90645:303] http://blog.csdn.net/wirelessqa
2014-03-14 16:38:52.537 TestArray[90645:303] ----- [array removeObject:(id)] :无需考虑范围，主要数组中存在这个对象就会直接被删除。
2014-03-14 16:38:52.537 TestArray[90645:303] bixiaopeng
2014-03-14 16:38:52.537 TestArray[90645:303] wirelessqa
2014-03-14 16:38:52.538 TestArray[90645:303] 男
2014-03-14 16:38:52.538 TestArray[90645:303] 帅
2014-03-14 16:38:52.538 TestArray[90645:303] 老毕
2014-03-14 16:38:52.538 TestArray[90645:303] 男
2014-03-14 16:38:52.539 TestArray[90645:303] 码农
2014-03-14 16:38:52.539 TestArray[90645:303] http://blog.csdn.net/wirelessqa
2014-03-14 16:38:52.539 TestArray[90645:303] ----- [array removeObjectAtIndex:(NSUInteger)]:删除数组中指定脚标索引的数据。
2014-03-14 16:38:52.539 TestArray[90645:303] wirelessqa
2014-03-14 16:38:52.540 TestArray[90645:303] 男
2014-03-14 16:38:52.540 TestArray[90645:303] 帅
2014-03-14 16:38:52.540 TestArray[90645:303] 老毕
2014-03-14 16:38:52.541 TestArray[90645:303] 男
2014-03-14 16:38:52.541 TestArray[90645:303] 码农
2014-03-14 16:38:52.541 TestArray[90645:303] http://blog.csdn.net/wirelessqa
2014-03-14 16:38:52.541 TestArray[90645:303] ----- [array removeObjectIdenticalTo:(id)] : 删除数组中指定元素
2014-03-14 16:38:52.542 TestArray[90645:303] 男
2014-03-14 16:38:52.542 TestArray[90645:303] 帅
2014-03-14 16:38:52.542 TestArray[90645:303] 老毕
2014-03-14 16:38:52.542 TestArray[90645:303] 男
2014-03-14 16:38:52.543 TestArray[90645:303] 码农
2014-03-14 16:38:52.543 TestArray[90645:303] http://blog.csdn.net/wirelessqa
2014-03-14 16:38:52.543 TestArray[90645:303] ----- [array removeObjectIdenticalTo:(id) inRange:(NSRange)] : 在指定范围内删除指定的元素。
2014-03-14 16:38:52.544 TestArray[90645:303] 帅
2014-03-14 16:38:52.544 TestArray[90645:303] 老毕
2014-03-14 16:38:52.544 TestArray[90645:303] 男
2014-03-14 16:38:52.544 TestArray[90645:303] 码农
2014-03-14 16:38:52.545 TestArray[90645:303] http://blog.csdn.net/wirelessqa
2014-03-14 16:38:52.545 TestArray[90645:303] ----- [array removeObjectsInArray:(NSArray *)] :删除一个数组的元素。
2014-03-14 16:38:52.545 TestArray[90645:303] 帅
2014-03-14 16:38:52.545 TestArray[90645:303] ----- 替换脚标元素replaceObjectAtIndex
2014-03-14 16:38:52.546 TestArray[90645:303] 老毕非常帅
2014-03-14 16:38:52.546 TestArray[90645:303] ----- 向数组中插入一个数据
2014-03-14 16:38:52.546 TestArray[90645:303] 老毕非常帅
2014-03-14 16:38:52.547 TestArray[90645:303] 同意
2014-03-14 16:38:52.547 TestArray[90645:303] ========================== 3.数组遍历 ==========================
2014-03-14 16:38:52.547 TestArray[90645:303] --- 遍历数组方法一
2014-03-14 16:38:52.547 TestArray[90645:303] 老毕
2014-03-14 16:38:52.548 TestArray[90645:303] 男
2014-03-14 16:38:52.548 TestArray[90645:303] 码农
2014-03-14 16:38:52.548 TestArray[90645:303] http://blog.csdn.net/wirelessqa
2014-03-14 16:38:52.549 TestArray[90645:303] --- 遍历数组方法二
2014-03-14 16:38:52.552 TestArray[90645:303] 老毕
2014-03-14 16:38:52.553 TestArray[90645:303] 男
2014-03-14 16:38:52.553 TestArray[90645:303] 码农
2014-03-14 16:38:52.553 TestArray[90645:303] http://blog.csdn.net/wirelessqa
2014-03-14 16:38:52.553 TestArray[90645:303] --- 遍历数组方法三
2014-03-14 16:38:52.554 TestArray[90645:303] 老毕
2014-03-14 16:38:52.554 TestArray[90645:303] 男
2014-03-14 16:38:52.554 TestArray[90645:303] 码农
2014-03-14 16:38:52.555 TestArray[90645:303] http://blog.csdn.net/wirelessqa
Program ended with exit code: 0
```

----
####  微信公众帐号: wirelessqa 
![wirelessqa](https://github.com/bxiaopeng/wirelessqa/raw/master/img/qrcode_for_gh_fdde1fe2880a_258.jpg)

#### 关于作者：

**作者:** 毕小朋 | 老 毕  **邮箱:** <wirelessqa.me@gmail.com> 

**微博:** [@WirelessQA](http://www.weibo.com/wirelessqa) **博客:** <http://blog.csdn.net/wirelessqa>

----