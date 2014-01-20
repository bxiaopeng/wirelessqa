

**源码下载地址:**  https://www.byvoid.com/project/node

## Express框架


**Express框架:**    http://expressjs.com/ 

### 安装Express

为了能够在命令行中直接使用它，我们需要全局模式安装 Express

```
npm install -g express
```

### 查看帮助

```
express --help
```
***结果:***


    bixiaopeng@bixiaopengtekiMacBook-Pro ~$ express --help

    Usage: express [options] [dir]

    Options:

    -h, --help          output usage information
    -V, --version       output the version number
    -s, --sessions      add session support
    -e, --ejs           add ejs engine support (defaults to jade)
    -J, --jshtml        add jshtml engine support (defaults to jade)
    -H, --hogan         add hogan.js engine support
    -c, --css <engine>  add stylesheet <engine> support (less|stylus) (defaults to plain css)
    -f, --force         force on non-empty directory
    


Express 在初始化一个项目的时候需要指定模板引擎,默认支持Jade和ejs



用express新建项目

```
express -e -s project_name
```
使项目支持ejs和sessions

提示：

使用 supervisor 实现监视代码修改和自动重启




