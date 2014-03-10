//
//  SimpleTableAppDelegate.m
//  TestButton
//
//  Created by bixiaopeng on 14-3-6.
//  Copyright (c) 2014年 bixiaopeng. All rights reserved.
//

#import "SimpleTableAppDelegate.h"

@implementation SimpleTableAppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
//    self.window = [[UIWindow alloc] initWithFrame:[[UIScreen mainScreen] bounds]];//系统帮你建画框
//    // Override point for customization after application launch.
//    NSLog(@"----- 返回的是带有状态栏的Rect ----- ");
//    CGRect bound = [[UIScreen mainScreen]bounds];
//    NSLog(@"boundwidth:%f    boundheight:%f ",bound.size.width, bound.size.height);
//    NSLog(@"boundx:%f    boundy:%f ",bound.origin.x, bound.origin.y);
//    NSLog(@"----- 返回不包含状态栏的Rect ----- ");
//    CGRect appBound = [[UIScreen mainScreen]applicationFrame];
//    NSLog(@"appBoundwidth:%f appBoundheight:%f "
//          ,appBound.size.width,appBound.size.height);
//    NSLog(@"appBoundx:%f    appBoundy:%f ",appBound.origin.x, appBound.origin.y);
//    
//    //----------------------- 第一个灰色矩形 -----------------------
//    
//    //1. 设置起点
//    CGPoint dark_point = CGPointMake(0.0f, 0.0f);
//    //2. 设置长度和宽度100*100
//    CGSize dark_size = CGSizeMake(100.0f, 100.0f);
//    //3. 绘制矩形
//    CGRect dark_rect = CGRectMake(dark_point.x, dark_point.y, dark_size.width, dark_size.height);
//    //4. 初始化view
//    UIView *dark = [[UIView alloc]initWithFrame:dark_rect];
//    //5. 为矩形视图设置背景色
//    dark.backgroundColor = [UIColor darkGrayColor];
//    //6. 增加一个视图到接收者的子视图列表中
//    [self.window addSubview:dark];
//    
//    NSLog(@"----- 打印几何元素的值 -----");
//    
//    NSLog(@"dark_point: %@", NSStringFromCGPoint(dark_point));
//    
//    NSLog(@"dark_size: %@", NSStringFromCGSize(dark_size));
//    
//    NSLog(@"dark_rect: %@", NSStringFromCGRect(dark_rect));
//    
//    //----------------------- 第二个蓝色矩形 -----------------------
//    //画第一块画布然涂成蓝色，大小是320 X 100
//    CGRect blue_rect = CGRectMake(100.0, 0.0, 320, 100);
//    UIView *blue = [[UIView alloc]initWithFrame:blue_rect];
//    blue.backgroundColor = [UIColor blueColor];
//    [self.window addSubview:blue];
//
//    //----------------------- 第三个红色矩形 -----------------------
//    CGRect red_rect = CGRectMake(0.0, 100, 160, 100);
//    UIView *red = [[UIView alloc]initWithFrame:red_rect];
//    red.backgroundColor = [UIColor redColor];
//    [self.window addSubview:red];
//
//    //----------------------- 第四个红色矩形 -----------------------
//    CGRect CGthree = CGRectMake(160, 100, 160, 100);
//    UIView *v_three = [[UIView alloc]initWithFrame:CGthree];
//    v_three.backgroundColor = [UIColor greenColor];
//    [self.window addSubview:v_three];
//    
//    //----------------------- 第五个橙色矩形 -----------------------
//    CGRect orange_rect = CGRectMake(0.0, 260, 320, 200);
//    UIView *range = [[UIView alloc]initWithFrame:orange_rect];
//    range.backgroundColor = [UIColor orangeColor];
//    [self.window addSubview:range];
//    
//    //----------------------- 第六个黄色矩形 -----------------------
//    CGRect yellow_rect = CGRectMake(100, 150,160, 200);
//    UIView *yello = [[UIView alloc]initWithFrame:yellow_rect];
//    yello.backgroundColor = [UIColor yellowColor];//黄色
//    [self.window addSubview:yello];
//    
//    //设备背景色为白色
//    self.window.backgroundColor = [UIColor whiteColor];
//    //使被使用对象的主窗口显示到屏幕的最前端
//    [self.window makeKeyAndVisible];
    return YES;
}
							
- (void)applicationWillResignActive:(UIApplication *)application
{
    // Sent when the application is about to move from active to inactive state. This can occur for certain types of temporary interruptions (such as an incoming phone call or SMS message) or when the user quits the application and it begins the transition to the background state.
    // Use this method to pause ongoing tasks, disable timers, and throttle down OpenGL ES frame rates. Games should use this method to pause the game.
}

- (void)applicationDidEnterBackground:(UIApplication *)application
{
    // Use this method to release shared resources, save user data, invalidate timers, and store enough application state information to restore your application to its current state in case it is terminated later. 
    // If your application supports background execution, this method is called instead of applicationWillTerminate: when the user quits.
}

- (void)applicationWillEnterForeground:(UIApplication *)application
{
    // Called as part of the transition from the background to the inactive state; here you can undo many of the changes made on entering the background.
}

- (void)applicationDidBecomeActive:(UIApplication *)application
{
    // Restart any tasks that were paused (or not yet started) while the application was inactive. If the application was previously in the background, optionally refresh the user interface.
}

- (void)applicationWillTerminate:(UIApplication *)application
{
    // Called when the application is about to terminate. Save data if appropriate. See also applicationDidEnterBackground:.
}

@end
