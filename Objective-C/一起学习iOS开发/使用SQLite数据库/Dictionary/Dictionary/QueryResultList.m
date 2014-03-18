//
//  QueryResultList.m
//
#import "QueryResultList.h"

@implementation QueryResultList
@synthesize  mArr;
@synthesize db;
@synthesize searchBar;

- (id)initWithStyle:(UITableViewStyle)style{
    
    self = [super initWithStyle:style];
    
    if (self) {
        mArr  = [[NSMutableArray alloc]init];//表数据源
        db =[[DB alloc]init];//数据库控制器
        searchBar = [[UISearchBar alloc]initWithFrame:CGRectMake(44.0,0,200.0,44)];//搜索控件
        searchBar.delegate=self;//设置搜索控件的委托
        
        self.navigationItem.titleView = searchBar;
    }
    return self;
}

- (void)didReceiveMemoryWarning{
    [super didReceiveMemoryWarning];
}

#pragma mark - View lifecycle
- (void)viewDidLoad{
    [super viewDidLoad];
}

- (void)viewDidUnload{
    [super viewDidUnload];
}

- (void)viewWillAppear:(BOOL)animated{
    [super viewWillAppear:animated];
}

- (void)viewDidAppear:(BOOL)animated{
    [super viewDidAppear:animated];
}

- (void)viewWillDisappear:(BOOL)animated{
    [super viewWillDisappear:animated];
}

- (void)viewDidDisappear:(BOOL)animated{
    [super viewDidDisappear:animated];
}

- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation{
    // Return YES for supported orientations
    return (interfaceOrientation == UIInterfaceOrientationPortrait);
}

#pragma mark - Table view data source

- (NSInteger)numberOfSectionsInTableView:(UITableView *)tableView{
    return 1;//分区数
}

- (NSInteger)tableView:(UITableView *)tableView numberOfRowsInSection:(NSInteger)section{
    return [mArr count];//行数
}

- (UITableViewCell *)tableView:(UITableView *)tableView cellForRowAtIndexPath:(NSIndexPath *)indexPath{
    static NSString *CellIdentifier = @"Cell";
    
    UITableViewCell *cell = [tableView dequeueReusableCellWithIdentifier:CellIdentifier];
    for ( UIView* view in cell.contentView.subviews) {
        [view removeFromSuperview];
    }

    if (cell == nil) {
        cell = [[[UITableViewCell alloc] initWithStyle:UITableViewCellStyleDefault reuseIdentifier:CellIdentifier] autorelease];
    }
    //绘制3个矩形
    UILabel* lblEN = [[UILabel alloc]initWithFrame:CGRectMake(5.0, 5.0, 300.0, 30.0)];//显示英文的文字标签控件
    UILabel* lblCN = [[UILabel alloc]initWithFrame:CGRectMake(5.0, 35.0, 300.0, 30.0)];//中文
    UILabel* lblComment = [[UILabel alloc]initWithFrame:CGRectMake(5.0, 65.0, 300.0, 30.0)];//详细
    
    //给矩形加点颜色
    lblEN.backgroundColor = [UIColor redColor];
    lblCN.backgroundColor = [UIColor yellowColor];
    lblComment.backgroundColor = [UIColor blueColor];

    //从数组中取值
    lblEN.text = [[mArr objectAtIndex:indexPath.row] objectForKey:@"kEN"];
    lblCN.text = [[mArr objectAtIndex:indexPath.row] objectForKey:@"kCN"];
    lblComment.text = [[mArr objectAtIndex:indexPath.row] objectForKey:@"kCOMMENT"];
    
    //加入cell
    [cell.contentView addSubview:lblEN];
    [cell.contentView addSubview:lblCN];
    [cell.contentView addSubview:lblComment];
    
    cell.selectionStyle = UITableViewCellSelectionStyleNone;//选中不要高亮
    
    [lblEN release];
    [lblCN release];
    [lblComment release];
    return cell;
}


- (BOOL)tableView:(UITableView *)tableView canMoveRowAtIndexPath:(NSIndexPath *)indexPath{
    return YES;
}

-(BOOL)tableView:(UITableView *)tableView canEditRowAtIndexPath:(NSIndexPath *)indexPath{
    return YES;
}

//设置tableview的高度
- (CGFloat)tableView:(UITableView *)tableView heightForRowAtIndexPath:(NSIndexPath *)indexPath{
    return 100.0;
}


#pragma mark - Table view delegate

- (void)tableView:(UITableView *)tableView didSelectRowAtIndexPath:(NSIndexPath *)indexPath{
    
}

#pragma mark - UISearchBar delegate
- (void) searchBarSearchButtonClicked:(UISearchBar*)activeSearchbar{
    
    //清空数组
    [mArr removeAllObjects];
    
    NSString* query= searchBar.text;
    NSLog(@"searchBar text : %@",query);
    
    
    NSMutableArray* arr = [db quary:query];
    
    //遍历字典
    for ( NSMutableDictionary* dict in arr) {
        [mArr addObject:dict];
    }
    
    [searchBar resignFirstResponder];
    //加载数据
    [self.tableView reloadData];
}



@end
