## 安装selenium 

```
# 方法一: 
bixiaopeng@bixiaopengtekiMacBook-Pro ~$ pip3.4 install selenium
Downloading/unpacking selenium
  Downloading selenium-2.41.0.tar.gz (2.5MB): 2.5MB downloaded
  Running setup.py (path:/private/var/folders/mz/6jbf3bss7f71qvsbtzw17_hc0000gn/T/pip_build_bixiaopeng/selenium/setup.py) egg_info for package selenium

Installing collected packages: selenium
  Running setup.py install for selenium

Successfully installed selenium
Cleaning up...

# 方法二:
bixiaopeng@bixiaopengtekiMacBook-Pro selenium-2.41.0$ sudo easy_install-3.4 selenium
Searching for selenium
Reading https://pypi.python.org/simple/selenium/
Best match: selenium 2.41.0
Downloading https://pypi.python.org/packages/source/s/selenium/selenium-2.41.0.tar.gz#md5=291dbbe220dc18696718fbccb5f0b2fe
Processing selenium-2.41.0.tar.gz
Writing /tmp/easy_install-miptghxl/selenium-2.41.0/setup.cfg
Running selenium-2.41.0/setup.py -q bdist_egg --dist-dir /tmp/easy_install-miptghxl/selenium-2.41.0/egg-dist-tmp-ssxhxojg
Adding selenium 2.41.0 to easy-install.pth file

Installed /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages/selenium-2.41.0-py3.4.egg
Processing dependencies for selenium
Finished processing dependencies for selenium

```

## 使用selenium

*注意：因为我们安装时都是指定了版本的，所以在使用selenium时也要使用对应的python版本，不会会找不到模块*

```
bixiaopeng@bixiaopengtekiMacBook-Pro ~$ python3.4
Python 3.4.0 (v3.4.0:04f714765c13, Mar 15 2014, 23:02:41)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from selenium import webdriver
>>> browser = webdriver.Firefox()
```