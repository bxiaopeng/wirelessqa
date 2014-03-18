
## 码上开始
```
#import <Foundation/Foundation.h>

int main(int argc, const char * argv[])
{
    
    @autoreleasepool {
        
        NSLog(@"############ 静态集合 ##############");
        
        NSLog(@"========= 直接创建一个集合");
        //NSSet是一组单值对象的集合,同一个对象只能保存一个
        //下面创建一个集合,并初始化值有6个，有两个相同的值
        NSSet *set1 = [[NSSet alloc] initWithObjects:@"老",@"毕",@"是",@"帅",@"哥",@"哥",nil];
        //查看集合的个数为5个，因为相对的对象只能保存一个
        NSLog(@"集合set1元素个数: %li",[set1 count]);
        
        NSLog(@"-------- NSSet实例中元素是无序的");
        for (NSObject *object in set1) {
            NSLog(@"set1: %@",object);
        }
        
        NSLog(@"========= 通过数组创建一个集合");
        
        NSArray *array = [NSArray arrayWithObjects:@"我",@"有",@"一",@"头",@"小",@"毛",@"驴",nil];
        NSSet *set2 = [[NSSet alloc]initWithArray:array];
        for (NSObject *object in set2) {
            NSLog(@"set2: %@",object);
        }
        
        NSLog(@"========= 通过现有的集合创建一个集合");
        NSSet *set3 = [[NSSet alloc] initWithSet:set1];
        for (NSObject *object in set3) {
            NSLog(@"set3: %@",object);
        }
        
        NSLog(@"========= 判断集合中是否包含某个对象");
        BOOL isContain = [set3 containsObject:@"老"];
        NSLog(@"包含: %i",isContain);
        BOOL isNotContain = [set3 containsObject:@"朋友"];
        NSLog(@"不包含: %i",isNotContain);
        
        NSLog(@"========= 判断两个集合的元素是否有相等的对象");
        BOOL isIntersect = [set3 intersectsSet:set1];
        NSLog(@"有相等的对象: %i",isIntersect);
        BOOL isNotIntersect = [set3 intersectsSet:set2];
        NSLog(@"无相等的对象: %i",isNotIntersect);
        
        NSLog(@"========= 判断两个集合的元素是否完全匹配");
        BOOL isEqual = [set1 isEqualToSet:set3];
        NSLog(@"完全匹配: %i",isEqual);
        BOOL isNotEqual = [set1 isEqualToSet:set2];
        NSLog(@"不完全匹配: %i",isNotEqual);
        
        NSLog(@"========= 判断某个集合是否是另一个集合的子集");
        BOOL isSubset = [set1 isSubsetOfSet:set3];
        NSLog(@"%i",isSubset);
        BOOL isNotSubset = [set1 isSubsetOfSet:set2];
        NSLog(@"%i",isNotSubset);
        
        NSLog(@"========= 通过setByAddingObject创建一个新集合");
        NSSet *set4 = [[NSSet alloc] initWithObjects:@"博客:", nil];
        NSSet *set5 = [set4 setByAddingObject:@"http://blog.csdn.net/wirelessqa"];
        for (NSObject *object in set5) {
            NSLog(@"set5: %@",object);
        }
        
        NSLog(@"========= 通过已有的两个集合创建一个新集合");
        NSSet *set6 = [set1 setByAddingObjectsFromSet:set2];
        for (NSObject *object in set6) {
            NSLog(@"set6: %@",object);
        }
        NSLog(@"========= 通过已有的一个集合和一个数组创建一个新集合");
        NSSet *set7 = [set1 setByAddingObjectsFromArray:array];
        for (NSObject *object in set7) {
            NSLog(@"set7: %@",object);
        }
        NSLog(@"========= 集合转为数组");
        NSArray *array1 = [set7 allObjects];
        for (NSObject *object in array1) {
            NSLog(@"array1: %@",object);
        }
        NSLog(@"========= 返回集合中任意一个对象");
        id obj = [set7 anyObject];
        NSLog(@"set7中任意一个对象: %@",obj);
        
        NSLog(@"========= 遍历集合");
        NSEnumerator *enumerator = [set7 objectEnumerator];
        for (NSObject *object in enumerator) {
            NSLog(@"set7:%@", object);
        }
        
        NSLog(@"############ 动态集合 ##############");
        
        NSLog(@"------ 创建可变集合对象mutableSet，并且初始化长度为8");
        NSMutableSet *mutableSet = [NSMutableSet setWithCapacity:8];
        NSLog(@"------ 向可变集合mutableSet中插入数据");
        [mutableSet addObject:@"微博"];
        [mutableSet addObject:@"http://blog.csdn.net/wirelessqa"];
        //遍历mutableSet
        for (NSObject *obj in mutableSet) {
            NSLog(@"mutable: %@",obj);
        }
        
        NSLog(@"------ 从可变集合mutableSet中删除数据");
        [mutableSet removeObject:@"微博"];
        [mutableSet removeObject:@"http://blog.csdn.net/wirelessqa"];
        for (NSObject *obj in mutableSet) {
            NSLog(@"mutable: %@",obj);
        }
        
        NSLog(@"------ 创建一个不为空的可变集合mutableSet2");
        NSMutableSet *mutableSet2 = [NSMutableSet setWithObjects:@"1",@"2",@"3", nil];
        NSLog(@"------ 将一个集合mutableSet2直接赋值给另一个空集合mutableSet");
        [mutableSet setSet:mutableSet2];
        
        for (NSObject *obj in mutableSet) {
            NSLog(@"mutable: %@",obj);
        }
        NSSet *seta = [NSSet setWithObjects:@"我",@"是",@"不可变数组",nil];
        for (NSObject *obj in seta) {
            NSLog(@"seta:%@",obj);
        }

        NSLog(@"------ mutableSet和seta两个集合取并集");
        [mutableSet unionSet:seta];
        
        for (NSObject *obj in mutableSet) {
            NSLog(@"mutableSet: %@",obj);
        }
        
        NSLog(@"------ 从可变集合mutableSet中删除一个集合seta");
        [mutableSet minusSet:seta];
        
        for (NSObject *obj in mutableSet) {
            NSLog(@"mutableSet:%@",obj);
        }
        
        NSSet *setb = [[NSSet alloc] initWithObjects:@"1",@"HELL", nil];
        
        NSLog(@"------ mutableSet和setb两个集合的交集");
        [mutableSet intersectSet:setb];
        for (NSObject *obj in mutableSet) {
            NSLog(@"%@",obj);
        }
        
        NSLog(@"------ 删除mutableSet中的所有数据");
        [mutableSet removeAllObjects];
        NSLog(@"%li",[mutableSet count]);
        
    }
    return 0;
}


```
## 运行结果:

```
2014-03-15 17:15:39.018 TestArray[95687:303] ############ 静态集合 ##############
2014-03-15 17:15:39.020 TestArray[95687:303] ========= 直接创建一个集合
2014-03-15 17:15:39.020 TestArray[95687:303] 集合set1元素个数: 5
2014-03-15 17:15:39.021 TestArray[95687:303] -------- NSSet实例中元素是无序的
2014-03-15 17:15:39.021 TestArray[95687:303] set1: 老
2014-03-15 17:15:39.021 TestArray[95687:303] set1: 是
2014-03-15 17:15:39.022 TestArray[95687:303] set1: 哥
2014-03-15 17:15:39.022 TestArray[95687:303] set1: 帅
2014-03-15 17:15:39.022 TestArray[95687:303] set1: 毕
2014-03-15 17:15:39.022 TestArray[95687:303] ========= 通过数组创建一个集合
2014-03-15 17:15:39.023 TestArray[95687:303] set2: 毛
2014-03-15 17:15:39.023 TestArray[95687:303] set2: 头
2014-03-15 17:15:39.023 TestArray[95687:303] set2: 有
2014-03-15 17:15:39.024 TestArray[95687:303] set2: 一
2014-03-15 17:15:39.024 TestArray[95687:303] set2: 我
2014-03-15 17:15:39.024 TestArray[95687:303] set2: 小
2014-03-15 17:15:39.024 TestArray[95687:303] set2: 驴
2014-03-15 17:15:39.025 TestArray[95687:303] ========= 通过现有的集合创建一个集合
2014-03-15 17:15:39.025 TestArray[95687:303] set3: 老
2014-03-15 17:15:39.034 TestArray[95687:303] set3: 是
2014-03-15 17:15:39.034 TestArray[95687:303] set3: 哥
2014-03-15 17:15:39.035 TestArray[95687:303] set3: 帅
2014-03-15 17:15:39.035 TestArray[95687:303] set3: 毕
2014-03-15 17:15:39.035 TestArray[95687:303] ========= 判断集合中是否包含某个对象
2014-03-15 17:15:39.036 TestArray[95687:303] 包含: 1
2014-03-15 17:15:39.036 TestArray[95687:303] 不包含: 0
2014-03-15 17:15:39.036 TestArray[95687:303] ========= 判断两个集合的元素是否有相等的对象
2014-03-15 17:15:39.037 TestArray[95687:303] 有相等的对象: 1
2014-03-15 17:15:39.037 TestArray[95687:303] 无相等的对象: 0
2014-03-15 17:15:39.037 TestArray[95687:303] ========= 判断两个集合的元素是否完全匹配
2014-03-15 17:15:39.037 TestArray[95687:303] 完全匹配: 1
2014-03-15 17:15:39.038 TestArray[95687:303] 不完全匹配: 0
2014-03-15 17:15:39.038 TestArray[95687:303] ========= 判断某个集合是否是另一个集合的子集
2014-03-15 17:15:39.038 TestArray[95687:303] 1
2014-03-15 17:15:39.039 TestArray[95687:303] 0
2014-03-15 17:15:39.039 TestArray[95687:303] ========= 通过setByAddingObject创建一个新集合
2014-03-15 17:15:39.039 TestArray[95687:303] set5: 博客:
2014-03-15 17:15:39.039 TestArray[95687:303] set5: http://blog.csdn.net/wirelessqa
2014-03-15 17:15:39.040 TestArray[95687:303] ========= 通过已有的两个集合创建一个新集合
2014-03-15 17:15:39.040 TestArray[95687:303] set6: 毛
2014-03-15 17:15:39.040 TestArray[95687:303] set6: 有
2014-03-15 17:15:39.041 TestArray[95687:303] set6: 一
2014-03-15 17:15:39.041 TestArray[95687:303] set6: 头
2014-03-15 17:15:39.041 TestArray[95687:303] set6: 毕
2014-03-15 17:15:39.041 TestArray[95687:303] set6: 我
2014-03-15 17:15:39.042 TestArray[95687:303] set6: 哥
2014-03-15 17:15:39.042 TestArray[95687:303] set6: 小
2014-03-15 17:15:39.042 TestArray[95687:303] set6: 是
2014-03-15 17:15:39.042 TestArray[95687:303] set6: 老
2014-03-15 17:15:39.043 TestArray[95687:303] set6: 驴
2014-03-15 17:15:39.043 TestArray[95687:303] set6: 帅
2014-03-15 17:15:39.043 TestArray[95687:303] ========= 通过已有的一个集合和一个数组创建一个新集合
2014-03-15 17:15:39.044 TestArray[95687:303] set7: 有
2014-03-15 17:15:39.044 TestArray[95687:303] set7: 一
2014-03-15 17:15:39.044 TestArray[95687:303] set7: 我
2014-03-15 17:15:39.044 TestArray[95687:303] set7: 头
2014-03-15 17:15:39.045 TestArray[95687:303] set7: 毕
2014-03-15 17:15:39.045 TestArray[95687:303] set7: 毛
2014-03-15 17:15:39.045 TestArray[95687:303] set7: 哥
2014-03-15 17:15:39.045 TestArray[95687:303] set7: 小
2014-03-15 17:15:39.046 TestArray[95687:303] set7: 是
2014-03-15 17:15:39.046 TestArray[95687:303] set7: 老
2014-03-15 17:15:39.046 TestArray[95687:303] set7: 驴
2014-03-15 17:15:39.047 TestArray[95687:303] set7: 帅
2014-03-15 17:15:39.047 TestArray[95687:303] ========= 集合转为数组
2014-03-15 17:15:39.047 TestArray[95687:303] array1: 有
2014-03-15 17:15:39.047 TestArray[95687:303] array1: 一
2014-03-15 17:15:39.048 TestArray[95687:303] array1: 我
2014-03-15 17:15:39.048 TestArray[95687:303] array1: 头
2014-03-15 17:15:39.048 TestArray[95687:303] array1: 毕
2014-03-15 17:15:39.048 TestArray[95687:303] array1: 毛
2014-03-15 17:15:39.049 TestArray[95687:303] array1: 哥
2014-03-15 17:15:39.049 TestArray[95687:303] array1: 小
2014-03-15 17:15:39.049 TestArray[95687:303] array1: 是
2014-03-15 17:15:39.050 TestArray[95687:303] array1: 老
2014-03-15 17:15:39.050 TestArray[95687:303] array1: 驴
2014-03-15 17:15:39.050 TestArray[95687:303] array1: 帅
2014-03-15 17:15:39.051 TestArray[95687:303] ========= 返回集合中任意一个对象
2014-03-15 17:15:39.051 TestArray[95687:303] set7中任意一个对象: 有
2014-03-15 17:15:39.051 TestArray[95687:303] ========= 遍历集合
2014-03-15 17:15:39.055 TestArray[95687:303] set7:有
2014-03-15 17:15:39.055 TestArray[95687:303] set7:一
2014-03-15 17:15:39.055 TestArray[95687:303] set7:我
2014-03-15 17:15:39.056 TestArray[95687:303] set7:头
2014-03-15 17:15:39.056 TestArray[95687:303] set7:毕
2014-03-15 17:15:39.056 TestArray[95687:303] set7:毛
2014-03-15 17:15:39.057 TestArray[95687:303] set7:哥
2014-03-15 17:15:39.057 TestArray[95687:303] set7:小
2014-03-15 17:15:39.057 TestArray[95687:303] set7:是
2014-03-15 17:15:39.058 TestArray[95687:303] set7:老
2014-03-15 17:15:39.058 TestArray[95687:303] set7:驴
2014-03-15 17:15:39.058 TestArray[95687:303] set7:帅
2014-03-15 17:15:39.058 TestArray[95687:303] ############ 动态集合 ##############
2014-03-15 17:15:39.059 TestArray[95687:303] ------ 创建可变集合对象mutableSet，并且初始化长度为8
2014-03-15 17:15:39.059 TestArray[95687:303] ------ 向可变集合mutableSet中插入数据
2014-03-15 17:15:39.059 TestArray[95687:303] mutable: http://blog.csdn.net/wirelessqa
2014-03-15 17:15:39.060 TestArray[95687:303] mutable: 微博
2014-03-15 17:15:39.060 TestArray[95687:303] ------ 从可变集合mutableSet中删除数据
2014-03-15 17:15:39.060 TestArray[95687:303] ------ 创建一个不为空的可变集合mutableSet2
2014-03-15 17:15:39.060 TestArray[95687:303] ------ 将一个集合mutableSet2直接赋值给另一个空集合mutableSet
2014-03-15 17:15:39.061 TestArray[95687:303] mutable: 3
2014-03-15 17:15:39.061 TestArray[95687:303] mutable: 1
2014-03-15 17:15:39.061 TestArray[95687:303] mutable: 2
2014-03-15 17:15:39.061 TestArray[95687:303] seta:我
2014-03-15 17:15:39.062 TestArray[95687:303] seta:是
2014-03-15 17:15:39.062 TestArray[95687:303] seta:不可变数组
2014-03-15 17:15:39.062 TestArray[95687:303] ------ mutableSet和seta两个集合取并集
2014-03-15 17:15:39.063 TestArray[95687:303] mutableSet: 是
2014-03-15 17:15:39.063 TestArray[95687:303] mutableSet: 3
2014-03-15 17:15:39.063 TestArray[95687:303] mutableSet: 不可变数组
2014-03-15 17:15:39.063 TestArray[95687:303] mutableSet: 1
2014-03-15 17:15:39.064 TestArray[95687:303] mutableSet: 我
2014-03-15 17:15:39.064 TestArray[95687:303] mutableSet: 2
2014-03-15 17:15:39.064 TestArray[95687:303] ------ 从可变集合mutableSet中删除一个集合seta
2014-03-15 17:15:39.064 TestArray[95687:303] mutableSet:3
2014-03-15 17:15:39.065 TestArray[95687:303] mutableSet:1
2014-03-15 17:15:39.065 TestArray[95687:303] mutableSet:2
2014-03-15 17:15:39.065 TestArray[95687:303] ------ mutableSet和setb两个集合的交集
2014-03-15 17:15:39.066 TestArray[95687:303] 1
2014-03-15 17:15:39.066 TestArray[95687:303] ------ 删除mutableSet中的所有数据
2014-03-15 17:15:39.066 TestArray[95687:303] 0
Program ended with exit code: 0
```

----
####  微信公众帐号: wirelessqa 
![wirelessqa](https://github.com/bxiaopeng/wirelessqa/raw/master/img/qrcode_for_gh_fdde1fe2880a_258.jpg)

#### 关于作者：

**作者:** 毕小朋 | 老 毕  **邮箱:** <wirelessqa.me@gmail.com> 

**微博:** [@WirelessQA](http://www.weibo.com/wirelessqa) **博客:** <http://blog.csdn.net/wirelessqa>

----