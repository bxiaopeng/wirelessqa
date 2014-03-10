//
//  SimpleTableViewController.h
//  SimpleTable
//
//  Created by bixiaopeng on 14-2-18.
//  Copyright (c) 2014年 bixiaopeng. All rights reserved.
//

#import <UIKit/UIKit.h>

//UITableView 是表规图幕后的实际类,用来灵活处理不同的数据类型。你可以显示国家列表戒者联系人姓名。
@interface SimpleTableViewController : UIViewController<UITableViewDelegate,UITableViewDataSource>

@end
