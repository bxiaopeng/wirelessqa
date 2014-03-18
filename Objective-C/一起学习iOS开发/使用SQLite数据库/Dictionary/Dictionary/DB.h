//  DB.h
//iukey
#import <Foundation/Foundation.h>
#import "/usr/include/sqlite3.h"
@interface DB : NSObject{

    sqlite3* pdb;//数据库句柄

}

@property(nonatomic,assign)sqlite3* pdb;

- (BOOL)insertRecordWithEN:(NSString*)en CN:(NSString*)cn Comment:(NSString*)comment;//插入一条纪录

- (NSMutableArray*)quary:(NSString*)str;//查询

- (const char*)getFilePath;//获取数据库路径

- (BOOL)createDB;//创建数据库

- (BOOL)createTable;//创建表
@end
