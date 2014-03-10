//
//  SimpleTableViewController.m
//  SimpleTable
//
//  Created by bixiaopeng on 14-2-18.
//  Copyright (c) 2014年 bixiaopeng. All rights reserved.
//

#import "SimpleTableViewController.h"
#import "SimpleTableCell.h"

@interface SimpleTableViewController ()

@end

@implementation SimpleTableViewController
{

    //定义一个实例变量用来存放数组
    NSArray *tableData;
    //定义一个数组来存放缩略图名称列表
    NSArray *thumbnails;
    //定义准备时间数组
    NSArray *preTime;
}

- (void)viewDidLoad
{
    //在控制器的视图装载到内存中完成之后,调用该方法
    [super viewDidLoad];
	
    //用arrayWithObjects来实例化一个NSArray对象
    tableData = [NSArray arrayWithObjects:@"Egg Benedict",
                 @"Mushroom Risotto", @"Full Breakfast", @"Hamburger", @"Ham and Egg Sandwich", @"Creme Brelee", @"White Chocolate Donut", @"Starbucks Coffee", @"Vegetable Curry", @"Instant Noodle with Egg", @"Noodle with BBQ Pork", @"Japanese Noodle with Pork", @"GreenTea", @"Thai Shrimp Cake", @"Angry Birds Cake", @"Ham and Cheese Panini", nil];
    //实例化数组thumbnails
    //图片名称的顸序和tableData数组的顺序保持一致,这样才能一一对应
    thumbnails = [NSArray arrayWithObjects:@"egg_benedict.jpg", @"mushroom_risotto.jpg", @"full_breakfast.jpg", @"hamburger.jpg", @"ham_and_egg_sandwich.jpg", @"creme_brelee.jpg", @"white_chocolate_donut.jpg", @"starbucks_coffee.jpg", @"vegetable_curry.jpg", @"instant_noodle_with_egg.jpg", @"noodle_with_bbq_pork.jpg", @"japanese_noodle_with_pork.jpg", @"green_tea.jpg", @"thai_shrimp_cake.jpg", @"angry_birds_cake.jpg", @"ham_and_cheese_panini.jpg", nil];
     preTime = [NSArray arrayWithObjects:@"10分钟", @"11分钟", @"12分钟", @"13分钟", @"14分钟", @"15分钟", @"16分钟", @"17分钟", @"18分钟", @"19分钟", @"20分钟", @"21分钟", @"22分钟", @"23分钟", @"24分钟", @"25分钟", nil];
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

//用来通知表规图选择了多少条数据行
-(NSInteger) tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section
{
    return [tableData count];
}

/*
 每一次数据行显示的时候,都会调用 cellForeRowAtIndexPath方法
 请求数据源,在表规图的特定位置插入一个单元格。表规图中可见的每一行都会触发该事件。
 事件中包含的参数之一是 NSIndexPath类型。
 NSIndexPath类表示数组集合中的某个特定项的路径。
 要知道当前填充的是哪一行,叧需要调用 NSIndexPath 对象(indexPath)的 row 属性,然后使用行号来引用 tableData 数组中的元素即可。
 得到的值被用来设置表规图中该行的文本值

 */
-(UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath
{
    static NSString *simpleTableIdentifier = @"SimpleTableItem";

    /*
     //------- old code
     //使用 UITableView 类的dequeueReusableCellWithIdentifer: 方法获取 UITableViewCell 类的一个实例。
     //下面的方法返回的是一个可重用的表规图单元格对象。
     //因为如果表非常大,为每一行都创建一个单独的UITableViewCell对象会产生严重的性能问题,会占用大量的内存。
     //此外,由于表视图在某一个时刻只显示固定数量的行，因此重用那些已经滚到屏幕外面的那些单元格将非常有意义
     //这正是dequeueReusableCellWithIdentifier要完成的事情
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:simpleTableIdentifier];
        if (cell == nil) {
           cell = [[UITableViewCell alloc]
                    initWithStyle:UITableViewCellStyleDefault reuseIdentifier:simpleTableIdentifier];
        }
     
     cell.imageView.image = [UIImage imageNamed:@"wirelessqa.jpg"];
     objectAtIndex:indexPath.row该代码行负责为特定行检索缩略图的文件名
     cell.imageView.image = [UIImage imageNamed:[thumbnails objectAtIndex:indexPath.row]];
     */

    //使用 UITableView 类的dequeueReusableCellWithIdentifer: 方法获取 SimpleTableCell 类的一个实例。
    SimpleTableCell *cell = (SimpleTableCell *)[tableView dequeueReusableCellWithIdentifier:simpleTableIdentifier];
    if (cell == nil) {
        //设置加载的nib
        NSArray *nib = [[NSBundle mainBundle] loadNibNamed:@"SimpleTableCell" owner:self options:nil];
        cell = [nib objectAtIndex:0];
    }
    cell.nameLabel.text = [tableData objectAtIndex:indexPath.row];
    cell.thumbnailImageView.image = [UIImage imageNamed:[thumbnails objectAtIndex:indexPath.row]];
    cell.prepTimeLabel.text = [preTime objectAtIndex:indexPath.row];
    return cell;
}

- (CGFloat)tableView:(UITableView *)tableView heightForRowAtIndexPath:(NSIndexPath *)indexPath
{
    return 78;
}

@end
