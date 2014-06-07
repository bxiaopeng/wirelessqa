## Appium运行需要注意：

### 1. 注意运行用例前必须启动appium,IP地址也要核对


## Appium踩过的坑一:

### 运行appium报错:Appium will not work if used or installed with sudo

```
bixiaopeng@bixiaopengtekiMacBook-Pro ~$ error: Appium will not work if used or installed with sudo. Please rerun/install as a non-root user. If you had to install Appium using `sudo npm install -g appium`, the solution is to reinstall Node using a method (Homebrew, for example) that doesn't require sudo to install global npm packages.

[1]+  Exit 1                  appium

```
### 出错原因:

权限问题,无法使用sudo来运行appium


### 解决办法:

#### 步骤1. 改变node的所有者

```
cd /usr/local/lib
sudo chown -R bixiaopeng node_modules

```

#### 步骤2. 卸载appium

```
npm uninstall appium -g

```

#### 步骤3. 重新安装appium

```
npm install -g appium
```

#### 步骤4. 启动

```
appium &
```

#### 步骤5. 查看是否运行成功

浏览器打开：

http://0.0.0.0:4723/

显示：

That URL did not map to a valid JSONWP resource


说明成功


## Appium踩过的坑二:

### 运行iOS用例报错:We don't have write access to /Applications/Xcode.app..

```
org.openqa.selenium.SessionNotCreatedException: A new session could not be created. (Original error: We don't have write access to /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator7.1.sdk/Applications/MobileSafari.app, please re-run authorize as bixiaopeng) (WARNING: The server did not provide any stacktrace information)
Command duration or timeout: 308 milliseconds
Build info: version: '2.41.0', revision: '3192d8a6c4449dc285928ba024779344f5423c58', time: '2014-03-27 11:29:39'
---------com.intellij.rt.execution.junit.JUnitStarter.prepareStreamsAndStart(JUnitStarter.java:202)
	at com.intellij.rt.execution.junit.JUnitStarter.main(JUnitStarter.java:65)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:39)
	at com.intellij.rt.execution.application.AppMain.main(AppMain.java:120)


Process finished with exit code 255

```
### 问题原因：

又是权限问题

### 解决办法：更改Xcode.app的权限

```
bixiaopeng@bixiaopengtekiMacBook-Pro Applications$ sudo chown -R bixiaopeng Xcode.app
Password:
```

### 再次运行：

OK


####  微信公众帐号: wirelessqa 
![wirelessqa](../img/qrcode_for_gh_fdde1fe2880a_258.jpg)

#### 关于作者：

**作者:** 毕小朋 | 老 毕  **邮箱:** <wirelessqa.me@gmail.com> 

**微博:** [@WirelessQA](http://www.weibo.com/wirelessqa) **博客:** <http://blog.csdn.net/wirelessqa>