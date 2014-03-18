
## 码上开始

```

#import <Foundation/Foundation.h>

int main(int argc, const char * argv[])
{

    @autoreleasepool {
        
        //常用类型的定义
        int testint =10086;
        NSInteger testNSInteger = 10087;
        BOOL testBOOL=TRUE;
        float testfloat = 3.1415926;
        double testdouble = 500.0;
        char testchar =120;
        char testchar2 = 'b';
        NSString *testNSString =@"http://blog.csdn.net/wirelessqa";
        
        //常用打印语句
        NSLog(@"字符串:%@",testNSString);
        NSLog(@"字符:%c",testchar);
        NSLog(@"字符串:%c",testchar2);
        NSLog(@"布尔值:%i",testBOOL);
        NSLog(@"整形:%i",testint);
        NSLog(@"长整形:%li",testNSInteger);
        NSLog(@"单精度浮点数： %f",testfloat);
        NSLog(@"双精度浮点数: %f",testdouble);
        NSLog(@"精度浮点数,且只保留两位小数:%.2f",testfloat);
        NSLog(@"科学技术法:%e",testfloat);
        NSLog(@"科学技术法(用最简短的方式):%g",testfloat);
        NSLog(@"同时打印两个整数：i＝%i,f=%f",testint,testfloat);    }
    return 0;
}


```

## 执行结果

```
2014-03-14 17:47:08.920 TestArray[90860:303] 字符串:http://blog.csdn.net/wirelessqa
2014-03-14 17:47:08.921 TestArray[90860:303] 字符:x
2014-03-14 17:47:08.921 TestArray[90860:303] 字符串:b
2014-03-14 17:47:08.922 TestArray[90860:303] 布尔值:1
2014-03-14 17:47:08.922 TestArray[90860:303] 整形:10086
2014-03-14 17:47:08.922 TestArray[90860:303] 长整形:10087
2014-03-14 17:47:08.923 TestArray[90860:303] 单精度浮点数： 3.141593
2014-03-14 17:47:08.923 TestArray[90860:303] 双精度浮点数: 500.000000
2014-03-14 17:47:08.923 TestArray[90860:303] 精度浮点数,且只保留两位小数:3.14
2014-03-14 17:47:08.923 TestArray[90860:303] 科学技术法:3.141593e+00
2014-03-14 17:47:08.924 TestArray[90860:303] 科学技术法(用最简短的方式):3.14159
2014-03-14 17:47:08.924 TestArray[90860:303] 同时打印两个整数：i＝10086,f=3.141593
```