//  DB.m
//iukey
#import "DB.h"
@implementation DB
@synthesize pdb;

#define FIRSTINIT 1
#define DBNAME    @"dictionary.sqlite"

- (id)init{
    self = [super init];
    
    if (self!=nil) {
        
#if FIRSTINIT
        [self createDB];
        [self createTable];
        [self insertRecordWithEN:@"cctv1" CN:@"央视1套" Comment:@"SB电视台1"];
        [self insertRecordWithEN:@"cctv2" CN:@"央视2套" Comment:@"SB电视台2"];
        [self insertRecordWithEN:@"cctv3" CN:@"央视3套" Comment:@"SB电视台3"];
        [self insertRecordWithEN:@"cctv4" CN:@"央视4套" Comment:@"SB电视台4"];
        [self insertRecordWithEN:@"cctv5" CN:@"央视5套" Comment:@"SB电视台5"];
        [self insertRecordWithEN:@"cctv6" CN:@"央视6套" Comment:@"SB电视台6"];
        [self insertRecordWithEN:@"cctv7" CN:@"央视7套" Comment:@"SB电视台7"];
        [self insertRecordWithEN:@"cctv8" CN:@"央视8套" Comment:@"SB电视台8"];
        [self insertRecordWithEN:@"cctv9" CN:@"央视9套" Comment:@"SB电视台9"];
        [self insertRecordWithEN:@"cctv10" CN:@"央视10套" Comment:@"SB电视台10"];
        [self insertRecordWithEN:@"cctv11" CN:@"央视11套" Comment:@"SB电视台11"];
        [self insertRecordWithEN:@"cctv12" CN:@"央视12套" Comment:@"SB电视台12"];
#endif
        
    }
    return self;
}

//获取数据库路径
- (const char*)getFilePath{
    NSLog(@"//获取数据库路径");
    return [[NSString stringWithFormat:@"%@/Documents/dictionary.sqlite",NSHomeDirectory() ] UTF8String];
}

//创建数据库
- (BOOL)createDB{
    
    NSLog(@"CREATEDB");
    
    //打开数据库，数据库不存在则创建
    int ret = sqlite3_open([self getFilePath ], &pdb);
    
    if (SQLITE_OK == ret) {//创建成功
        sqlite3_close(pdb);//关闭
        return YES;
    }else{
        return NO;//创建失败
    }
}

//创建表
- (BOOL)createTable{
    
    NSLog(@"//创建表");
    char* err;
    
    //准备创建表sql语句
    char* sql = "create table dictionary(ID integer primary key autoincrement,en nvarchar(64),cn nvarchar(128),comment nvarchar(256))";
    
    if (sql == NULL) {
        return NO;
    }
    
    //1. 使用sqlite3_open打开数据库
    if (SQLITE_OK != sqlite3_open([self getFilePath ], &pdb)){
        return NO;
    }
    
    //2. 执行创建表语句成功
    if (SQLITE_OK == sqlite3_exec(pdb, sql, NULL, NULL, &err)) {
        sqlite3_close(pdb);
        return YES;
        
    }else{//创建表失败
        
        return NO;
    }
}

//插入数据
- (BOOL)insertRecordWithEN:(NSString*)en CN:(NSString*)cn Comment:(NSString*)comment{
    
    int ret = 0;
    
    //1. 使用sqlite3_open打开数据库
    if (SQLITE_OK != sqlite3_open([self getFilePath ], &pdb)){
        return NO;
    }
    
    char* sql = "insert into dictionary(en,cn,comment) values(?,?,?);";//2. 准备插入语句，有3个参数
    
    sqlite3_stmt* stmt; //3. 这个相当于ODBC的Command对象，用于保存编译好的SQL语句
    
    //4. 使用sqlite3_prepare_v2函数预处理SQL语句；
    if (sqlite3_prepare_v2(pdb, sql, -1, &stmt, nil) == SQLITE_OK) {
        
        //5. 使用sqlite3_bind_text函数绑定参数；
        sqlite3_bind_text(stmt, 1, [en UTF8String], -1, NULL);
        sqlite3_bind_text(stmt, 2, [cn UTF8String], -1, NULL);
        sqlite3_bind_text(stmt, 3, [comment UTF8String], -1, NULL);
        
    }else{
        
        return NO;
        
    }
    
    //6. 使用sqlite3_step函数执行SQL语句，遍历结果集；
    if (SQLITE_DONE == (ret = sqlite3_step(stmt))) {
        
        //7. 使用sqlite3_finalize和sqlite3_close函数释放资源
        
        sqlite3_finalize(stmt);
        
        sqlite3_close(pdb);
        
        return YES;
        
    }else{
        
        return NO;
    }
}

//数据查询
- (NSMutableArray*)quary:(NSString *)str{
    
    //创建一个空的可变数组
    NSMutableArray* arr =[[NSMutableArray alloc]init];
    
    //1. 打开数据库
    if (SQLITE_OK != sqlite3_open([self getFilePath ], &pdb)){
        return NO;
    }
    
    //2. 准备查询语句
    char* sql = "select * from dictionary where en like ? or cn like ? or comment like ?;";
    
    //3. 这个相当于ODBC的Command对象，用于保存编译好的SQL语句
    sqlite3_stmt* stmt;
    
    
    //4. 使用sqlite3_prepare_v2函数预处理SQL语句；
    if (sqlite3_prepare_v2(pdb, sql, -1, &stmt, NULL) == SQLITE_OK) {
        
        NSLog(@"stmt ready");
        //3. 使用sqlite3_bind_text函数绑定参数；
        sqlite3_bind_text(stmt, 1,[[NSString stringWithFormat:@"%%%@%%",str]UTF8String], -1, NULL);
        sqlite3_bind_text(stmt, 2, [[NSString stringWithFormat:@"%%%@%%",str]UTF8String], -1, NULL);
        sqlite3_bind_text(stmt, 3, [[NSString stringWithFormat:@"%%%@%%",str]UTF8String], -1, NULL);
        
    }else{
        
        return nil;
        
    }
    
    //5. 使用sqlite3_step函数执行SQL语句，遍历结果集；
    while( SQLITE_ROW == sqlite3_step(stmt) ){

        NSLog(@"RUN");
        //使用sqlite3_column_text等函数提取字段数据；
        char* _en = (char*)sqlite3_column_text(stmt, 1);
        NSLog(@"en: %s",_en);
        
        char* _cn = (char*)sqlite3_column_text(stmt, 2);
        char* _comment = (char*)sqlite3_column_text(stmt, 3);
        
        NSMutableDictionary* dict = [[NSMutableDictionary alloc]init];//单条纪录
        
        [dict setObject:[NSString stringWithCString:_en encoding:NSUTF8StringEncoding] forKey:@"kEN"];
        [dict setObject:[NSString stringWithCString:_cn encoding:NSUTF8StringEncoding] forKey:@"kCN"];
        [dict setObject:[NSString stringWithCString:_comment encoding:NSUTF8StringEncoding] forKey:@"kCOMMENT"];
        [arr addObject:dict];//插入到结果数组
    }
    
    sqlite3_finalize(stmt);
    sqlite3_close(pdb);
    
    return [arr autorelease];//返回查询结果数组
}

@end
