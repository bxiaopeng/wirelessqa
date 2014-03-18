//
//  SimpleTableCell.h
//  SimpleTable
//
//  Created by bixiaopeng on 14-2-23.
//  Copyright (c) 2014年 bixiaopeng. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface SimpleTableCell : UITableViewCell

/*
说明:
1. weak和nonatomic是property 的特性。
2. UILabel和UIImageView是类型
3. nameLabel、prepTimeLabel是thumbnailImageView 是变量名称。
4. IBOutlet可理解为一个指示符(indicator)。为了关联实例变量和表视图单元格(如 SimpleTableCell.xib)中的元素,我们使用IBOutlet关键字,让Interface Builder知道它们允许建立连接。
 */

//菜谱名
@property(nonatomic,weak) IBOutlet UILabel *nameLabel;

//时间
@property(nonatomic,weak) IBOutlet UILabel *prepTimeLabel;

//缩略图
@property(nonatomic,weak) IBOutlet UIImageView *thumbnailImageView;

@end
