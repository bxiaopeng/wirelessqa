//
//  SimpleTableCell.m
//  SimpleTable
//
//  Created by bixiaopeng on 14-2-23.
//  Copyright (c) 2014年 bixiaopeng. All rights reserved.
//

#import "SimpleTableCell.h"

@implementation SimpleTableCell

//@synthesize 关键字告诉编译器自动生成代码,用来讵问前面定义的属性

@synthesize nameLabel = _nameLabel;

@synthesize prepTimeLabel = _prepTimeLabel;

@synthesize thumbnailImageView = _thumbnailImageView;


- (id)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier
{
    self = [super initWithStyle:style reuseIdentifier:reuseIdentifier];
    if (self) {
        // Initialization code
    }
    return self;
}

- (void)setSelected:(BOOL)selected animated:(BOOL)animated
{
    [super setSelected:selected animated:animated];

    // Configure the view for the selected state
}

@end
