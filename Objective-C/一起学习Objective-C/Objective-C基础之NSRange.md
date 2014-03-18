
## 码上开始

```

#import <Foundation/Foundation.h>

int main(int argc, const char * argv[])
{
    
    @autoreleasepool {
        
        NSLog(@"------ 从字符串中获取指定范围的字符");
        NSString *str = @"bixiaopeng is a (帅哥)";
        NSRange range = NSMakeRange (17, 2);
        NSLog (@"bixiaopeng is a : %@", [str substringWithRange:range]);
        NSLog(@"------ 截取从指定位置开始到最后的字符串");
        NSLog(@"%@",[str substringFromIndex:range.location]);
        NSLog(@"------ 截取从0到指定位置的字符串");
        NSLog(@"%@",[str substringToIndex:range.location]);
        
        NSLog(@"------ 在字符串中搜索字符");
        NSRange range2 = [str rangeOfString:@"帅哥"];
        if (range2.length > 0) {
            NSLog(@"range is :%@",NSStringFromRange(range2));
        }
        
        NSLog(@"------ 反向查找");
        NSRange range3 = [str rangeOfString:@"peng" options:NSBackwardsSearch];
        
        if (range3.length > 0) {
            NSLog(@"range is :%@",NSStringFromRange(range3));
        }
        
        NSLog(@"------ 获取一个数组的子符");
        NSArray *array = [NSArray arrayWithObjects:@"老毕",@"是",@"一",@"个",@"帅",@"哥",@"哥",nil];
        NSRange theRange = NSMakeRange(2, 5);
        NSArray *subArray =[array subarrayWithRange:theRange];
        for (NSObject *ob in subArray) {
            NSLog(@"%@",ob);
        }
        


        
    }
    return 0;
}


```

## 运行结果

```
2014-03-15 10:00:26.932 TestArray[94407:303] ------ 从字符串中获取指定范围的字符
2014-03-15 10:00:26.933 TestArray[94407:303] bixiaopeng is a : 帅哥
2014-03-15 10:00:26.934 TestArray[94407:303] ------ 截取从指定位置开始到最后的字符串
2014-03-15 10:00:26.934 TestArray[94407:303] 帅哥)
2014-03-15 10:00:26.934 TestArray[94407:303] ------ 截取从0到指定位置的字符串
2014-03-15 10:00:26.935 TestArray[94407:303] bixiaopeng is a (
2014-03-15 10:00:26.935 TestArray[94407:303] ------ 在字符串中搜索字符
2014-03-15 10:00:26.936 TestArray[94407:303] range is :{17, 2}
2014-03-15 10:00:26.936 TestArray[94407:303] ------ 反向查找
2014-03-15 10:00:26.936 TestArray[94407:303] range is :{6, 4}
2014-03-15 10:00:26.936 TestArray[94407:303] ------ 获取一个数组的子符
2014-03-15 10:00:26.937 TestArray[94407:303] 一
2014-03-15 10:00:26.937 TestArray[94407:303] 个
2014-03-15 10:00:26.937 TestArray[94407:303] 帅
2014-03-15 10:00:26.938 TestArray[94407:303] 哥
2014-03-15 10:00:26.938 TestArray[94407:303] 哥
Program ended with exit code: 0
```

----
####  微信公众帐号: wirelessqa 
![wirelessqa](https://github.com/bxiaopeng/wirelessqa/raw/master/img/qrcode_for_gh_fdde1fe2880a_258.jpg)

#### 关于作者：

**作者:** 毕小朋 | 老 毕  **邮箱:** <wirelessqa.me@gmail.com> 

**微博:** [@WirelessQA](http://www.weibo.com/wirelessqa) **博客:** <http://blog.csdn.net/wirelessqa>

----