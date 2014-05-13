## 码上实践 testgetopt.py

```
import getopt, sys

def usage():
	print('帮助: 老毕在逗你玩!>-这里是帮助命令的提示!我就不写了哈')

"""
        1. 使用sys.argv[1:] 过滤掉第一个参数（它是执行脚本的名字，不应算作参数的一部分）
        2. 短格式vho:          :加冒号表示需要跟一个参数，不加就不用
        3. 长格式help,output=  :加等号表示需要跟一个参数，不加就不用
        4. 调用getopt函数。函数返回两个列表：opts 和args 。
                opts 为分析出的格式信息。opts 是一个两元组的列表。每个元素为：( 选项串, 附加参数) 。如果没有附加参数则为空串''
                args 为不属于格式信息的剩余的命令行参数。      
"""
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "vho:", ["version","help", "output=","name=","blog"])
        print('opts: '+ str(opts))
        print('args: '+ str(args))
    except getopt.GetoptError as err:
        # 打印帮助命令然后退出
        print(err) # 打印出错信息
        usage()
        sys.exit(2)

    output = None
    version = '1.0'
    blog = 'http://www.csdn.net/wirelessqa'

    for key, value in opts:

        if key in ("-v","--version"):
            print('version: ' + version)

        elif key in ("-h", "--help"):
            usage()
            sys.exit()
        
        elif key in ("-o", "--output"):
            output = value
            print(value)
        elif key == '--name':
        	print('name: ' + value)
        elif key == '--blog':
        	print('blog: ' + blog)
        else:
            assert False, "未定义些操作"
    # ...

if __name__ == "__main__":
    main()

```

## 运行结果:

```
bixiaopeng@bixiaopengtekiMacBook-Pro ~$ python testgetopt.py --help
opts: [('--help', '')]
args: []
帮助: 老毕在逗你玩!>-这里是帮助命令的提示!我就不写了哈
bixiaopeng@bixiaopengtekiMacBook-Pro ~$ python testgetopt.py -h
opts: [('-h', '')]
args: []
帮助: 老毕在逗你玩!>-这里是帮助命令的提示!我就不写了哈
bixiaopeng@bixiaopengtekiMacBook-Pro ~$ python testgetopt.py -v
opts: [('-v', '')]
args: []
version: 1.0
bixiaopeng@bixiaopengtekiMacBook-Pro ~$ python testgetopt.py -v --version
opts: [('-v', ''), ('--version', '')]
args: []
version: 1.0
version: 1.0
bixiaopeng@bixiaopengtekiMacBook-Pro ~$ python testgetopt.py --name
option --name requires argument
帮助: 老毕在逗你玩!>-这里是帮助命令的提示!我就不写了哈
bixiaopeng@bixiaopengtekiMacBook-Pro ~$ python testgetopt.py --name 老毕
opts: [('--name', '老毕')]
args: []
name: 老毕
bixiaopeng@bixiaopengtekiMacBook-Pro ~$ python testgetopt.py --name 老毕 --blog
opts: [('--name', '老毕'), ('--blog', '')]
args: []
name: 老毕
blog: http://www.csdn.net/wirelessqa
bixiaopeng@bixiaopengtekiMacBook-Pro ~$ python testgetopt.py --null
option --null not recognized
帮助: 老毕在逗你玩!>-这里是帮助命令的提示!我就不写了哈
```

----
####  微信公众帐号: wirelessqa 
![wirelessqa](../img/qrcode_for_gh_fdde1fe2880a_258.jpg)

#### 关于作者：

**作者:** 毕小朋 | 老 毕  **邮箱:** <wirelessqa.me@gmail.com> 

**微博:** [@WirelessQA](http://www.weibo.com/wirelessqa) **博客:** <http://blog.csdn.net/wirelessqa>

----