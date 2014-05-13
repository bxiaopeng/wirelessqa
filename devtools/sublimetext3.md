参考: http://www.cnblogs.com/bananaplan/p/Sublime-Text-3-Powerful.html

## Sublime Text 3下载地址

http://www.sublimetext.com/3

我下载的是OS X

## 安装Package Control

安装代码地址：https://sublime.wbond.net/installation

使用的是python3

```
import urllib.request,os,hashlib; 
h = '7183a2d3e96f11eeadd761d777e62404' + 'e330c659d4bb41d3bdf022e94cab3cd0'; 
pf = 'Package Control.sublime-package'; 
ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) );
by = urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ', '%20')).read();
dh = hashlib.sha256(by).hexdigest(); 
print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
```

## 安装插件

安装完Package Control以后,我们可以使用快捷键Command + Shift + P 打开PackageControl来安装插件了.

步骤： 

1.  打开Package Control (Command + Shift + P)
2.  输入install ,选择Install Package,等待另一个输入框显示(可能会要几秒种)
3.  输入你要安装的插件,选择后会开始安装
4.  安装完成后提示安装成功

## 常用插件

插件名|说明
----|----
SublimeCodeIntel|为部分语言增强自动完成功能，包括了 Python 。这个插件同时也可以让你跳转到符号定义的地方，通过按住 alt 并点击符号。非常方便。  For Mac OS X:<br> Jump to definition = ``Control+Click``<br> Jump to definition = ``Control+Command+Alt+Up``<br> Go back = ``Control+Command+Alt+Left``<br> Manual CodeIntel = ``Control+Shift+space``<br>更多: https://github.com/SublimeCodeIntel/SublimeCodeIntel
SublimeREPL |允许你在编辑界面直接运行 Python 解释器。我倾向于在单独的终端窗口用 bpython 来运行，但有时 SublimeREPL 是很有帮助的
Pylinter |这个插件提供了目前我所见到的最好的 pylint 编辑器整合。它自动检查 .py 文件，无论其何时被保存，并且会直接在编辑界面显示 pylint 违规。它还有一个快捷方式来禁用局部的 pylint 检查，通过插入一个 #pylint: 禁用注释。这个插件对于我确实非常有用
Color Scheme - Tomorrow Night Color| schemes 决定了编辑器界面语法高亮的字体颜色。这是一个非常酷的暗黑系样式。
All Autocomplete Sublime|默认的自动完成只关注当前文件的单词。这个插件扩展了其自动完成的单词列表到所有打开的文件。
ConvertToUTF8　|支持 GBK, BIG5, EUC-KR, EUC-JP, Shift_JIS 等编码的插件
Bracket Highlighter　|用于匹配括号，引号和html标签。对于很长的代码很有用。安装好之后，不需要设置插件会自动生效
DocBlockr　|DocBlockr可以自动生成PHPDoc风格的注释。它支持的语言有Javascript, PHP, ActionScript, CoffeeScript, Java, Objective C, C, C++
Emmet(Zen Coding)　|快速生成HTML代码段的插件，强大到无与伦比，不知道的请自行google
SideBar Enhancements|这个插件提供了侧边栏附加的上下文菜单选项，例如"New file"，"New Floder"等。这些本应当默认就该有的，却没有。
Themr|主题管理，切换主题的时候，不用自己修改配置文件了，用这个可以方便的切换主题
GitGutter| 在编辑器的凹槽区，依照 Git ，增加小图标来标识一行是否被插入、修改或删除。在 GitGutter 的 readme 中有说明如何更改颜色图标来更新你的配色方案文件。


  

## 通用快捷键

快捷键|说明
----|----
Ctrl+Shift+P|打开Package Control
Ctrl+P|根据文件名打开文件。比如你想打开login/func/funtion.php，你只要在输入框中输入login/func/funtion.php即可，也可以用模糊匹配，如login/function等，模糊匹配还是自己去体验吧。
Ctrl+R|找到了我们要查看的源码文件后，想找函数方法怎么办？输入log，能找到所有名带log的方法，输入loginout，则能定位到loginout()。大家可能会注意到，Ctrl+R后，在输入框中会自动有一个@，这就是要匹配方法的意思。那么，除此之外，还有些有用的匹配符号，就一并说了。
Ctrl+G|定位到行，Ctrl+G，或Ctrl+P后，在框中输入:行数，如:58，则要跳转到58行去。
Ctrl+P|查找标识，Ctrl+P后，#标识。
Ctrl+D|多处同步编辑
Ctrl+F|查找，Ctrl+F后，Enter查找下一个，Shift+Enter，查找上一个
Ctrl+H|查找替换
Ctrl+Shift+F|这个得加粗，飘红，就指着它活着呢。怎么说呢，可以叫全项目查找，就是在你当前打开的项目中，根据你输入的字符查找。



