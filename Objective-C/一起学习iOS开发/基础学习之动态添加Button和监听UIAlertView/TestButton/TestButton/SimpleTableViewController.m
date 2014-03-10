//
//  SimpleTableViewController.m
//  TestButton
//
//  Created by bixiaopeng on 14-3-6.
//  Copyright (c) 2014年 bixiaopeng. All rights reserved.
//

#import "SimpleTableViewController.h"

@interface SimpleTableViewController ()

@end

@implementation SimpleTableViewController

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (IBAction)addButton:(id)sender {
    //画一个矩形,起点: x = 70,y = 220 ,大小: width = 200, high = 60;
    CGRect frame = CGRectMake(140, 32, 150, 40);
    //设置BUtton的形状，此处为圆角按钮
    UIButton *button = [UIButton buttonWithType:UIButtonTypeRoundedRect];
    //Button背景色
    button.backgroundColor = [UIColor clearColor];
    //设置Button名字，和他的状态，此处是一般的状态
    [button setTitle:@"弹出两个按钮选择框" forState:UIControlStateNormal];
    button.frame = frame;
    /* 给button添加事件，事件有很多种按下按钮，并且手指离开屏幕的时候触发这个事件,触发了这个事件以后，执行butClick:这个方法，addTarget:self 的意思是说，这个方法在本类中也可以传入其他类的指针*/
    [button addTarget:self action:@selector(buttonClicked) forControlEvents:UIControlEventTouchUpInside];
    //把Button添加到视图之上
    [self.view addSubview:button];
}


-(void) buttonClicked{
    //获取或设置UIAlertView上的消息
    UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"欢迎关注老毕的博客"
                                                    message:@"http://blog.csdn.net/wirelessqa"
                                                   delegate:self
                                          cancelButtonTitle:@"喜欢"
                                          otherButtonTitles:@"很喜欢",nil];
    [alert show];
}

- (IBAction)addButton2:(id)sender {
    CGRect frame = CGRectMake(140, 100, 180, 40);
    //自定义风络的button
    UIButton *button2 = [UIButton buttonWithType:UIButtonTypeCustom];
    button2.backgroundColor = [UIColor redColor];
    [button2 setTitle:@"弹出多个按钮选择框" forState:UIControlStateNormal];
    button2.frame = frame;
    [button2 addTarget:self action:@selector(button2Clicked) forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:button2];
}

-(void) button2Clicked{
    UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"提示"
                                                    message:@"老毕帅不帅！"
                                                   delegate:self
                                          cancelButtonTitle:@"帅"
                                          otherButtonTitles:@"很帅",@"非常帅",@"帅到掉渣",@"帅到无法想象",nil];
    [alert show];
}



- (IBAction)addButton3:(id)sender {
    CGRect frame = CGRectMake(140, 155, 180, 40);
    UIButton *button3 = [UIButton buttonWithType:UIButtonTypeDetailDisclosure];
    button3.backgroundColor = [UIColor yellowColor];
    [button3 setTitle:@"登录提示框" forState:UIControlStateNormal];
    button3.frame = frame;
    [button3 addTarget:self action:@selector(button3Clicked) forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:button3];
    
}
-(void) button3Clicked{
    
UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"登录" message:@"请输入用户名和密码" delegate:nil cancelButtonTitle:@"取消"otherButtonTitles:@"确定", nil];
    
    alert.alertViewStyle = UIAlertViewStyleLoginAndPasswordInput;
    [alert show];
}


- (IBAction)addButton4:(id)sender {
    CGRect frame = CGRectMake(140, 215, 180, 40);
    UIButton *button4 = [UIButton buttonWithType:UIButtonTypeInfoLight];
    button4.backgroundColor = [UIColor greenColor];
    [button4 setTitle:@"弹出普通文本输入框" forState:UIControlStateNormal];
    button4.frame = frame;
    [button4 addTarget:self action:@selector(button4Clicked) forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:button4];
}

-(void) button4Clicked{
    
    UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"文本输入" message:@"请输入文本" delegate:nil cancelButtonTitle:@"取消"otherButtonTitles:@"确定", nil];
    
    alert.alertViewStyle = UIAlertViewStylePlainTextInput;
    [alert show];
}

- (IBAction)addButton5:(id)sender {
    CGRect frame = CGRectMake(140, 269, 180, 40);
    UIButton *button5 = [UIButton buttonWithType:UIButtonTypeInfoDark];
    button5.backgroundColor = [UIColor grayColor];
    [button5 setTitle:@"弹出密码输入框" forState:UIControlStateNormal];
    /* 下面的这个属性设置为yes的状态下，按钮按下会发光*/
    button5.showsTouchWhenHighlighted = YES;
    button5.frame = frame;
    [button5 addTarget:self action:@selector(button5Clicked) forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:button5];
    
}

-(void) button5Clicked{
    
    UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"安全输入" message:@"请输入密码" delegate:nil cancelButtonTitle:@"取消"otherButtonTitles:@"确定", nil];
    
    alert.alertViewStyle = UIAlertViewStyleSecureTextInput;
    [alert show];
}



- (IBAction)addButton6:(id)sender {
    CGRect frame = CGRectMake(140, 333, 180, 40);
    UIButton *button6 = [UIButton buttonWithType:UIButtonTypeContactAdd];
    button6.backgroundColor = [UIColor orangeColor];
    [button6 setTitle:@"弹出密码输入框" forState:UIControlStateNormal];
    button6.frame = frame;
    [button6 addTarget:self action:@selector(button5Clicked) forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:button6];

    
}

- (IBAction)addButton7:(id)sender {
     CGRect frame = CGRectMake(140, 370, 150, 150);
    UIButton *button7 = [UIButton buttonWithType:UIButtonTypeRoundedRect];
    button7.backgroundColor = [UIColor clearColor];
    [button7 setTitle:@"点我呀" forState:UIControlStateNormal];
    button7.frame = frame;
    //设置button背景图
    [button7 setBackgroundImage:[UIImage imageNamed:@"wirelessqa.png"] forState:UIControlStateNormal];
    //这个是设置button前景图片,好像不起作用
//  [button7 setImage:[UIImage imageNamed:@"wirelessqa.png"] forState:UIControlStateNormal];
    [button7 addTarget:self action:@selector(button2Clicked) forControlEvents:UIControlEventTouchUpInside];
    [self.view addSubview:button7];
}

-(void)alertView:(UIAlertView *)alertView clickedButtonAtIndex:(NSInteger)buttonIndex
{
    NSLog(@"提示框上有%d个按钮",alertView.numberOfButtons);
    NSLog(@"你点击了第%d个按钮(index)", buttonIndex);
    NSLog(@"按钮上的文字是:%@",[alertView buttonTitleAtIndex:buttonIndex]);
    //获得第一个其他按钮的索引
    NSLog(@"第一个按钮的索引:%d",alertView.firstOtherButtonIndex);
    //通过给定标题添加按钮
    [alertView addButtonWithTitle:@"addButton"];
}

//AlertView已经消失时
- (void)alertView:(UIAlertView *)alertView didDismissWithButtonIndex:(NSInteger)buttonIndex {
	NSLog(@"--------------- didDismissWithButtonIndex");
}
//AlertView即将消失时
- (void)alertView:(UIAlertView *)alertView willDismissWithButtonIndex:(NSInteger)buttonIndex {
	NSLog(@"willDismissWithButtonIndex");
}

- (void)alertViewCancel:(UIAlertView *)alertView {
	NSLog(@"alertViewCancel");
}
//AlertView已经显示时
- (void)didPresentAlertView:(UIAlertView *)alertView {
	NSLog(@"didPresentAlertView");
}
//AlertView即将显示时
- (void)willPresentAlertView:(UIAlertView *)alertView {
	NSLog(@"-------------- willPresentAlertView");
}



@end
