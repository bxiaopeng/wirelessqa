//  QueryResultList.h
//  iukey

#import <UIKit/UIKit.h>
#import "DB.h"

@interface QueryResultList : UITableViewController<UISearchBarDelegate>{
    NSMutableArray* mArr;//tableView数据源
    DB* db ;//数据库对象
    UISearchBar* searchBar ;//搜索框
}
@property(nonatomic,retain)NSMutableArray* mArr;
@property(nonatomic,retain)DB* db;
@property(nonatomic,retain)UISearchBar* searchBar ;
@end
