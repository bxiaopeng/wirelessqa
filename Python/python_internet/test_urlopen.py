#!/usr/bin/python
# -*- coding:utf-8 -*-
#---------------------------------------------------------------------------
#  File:
#  Description: urlopen使用的实例
#
#  Date:         14/11/23 下午4:06
#  Author:       bixiaopeng
#  Tags:
#---------------------------------------------------------------------------

from httplib import HTTPConnection
import os
from urllib import urlopen
import urllib

HTTPConnection.debuglevel = 1  

def test_urlopen():
    """
    测试urlopen
    :return:
    """
    response = urlopen('http://www.baidu.com/')

    print u"====================打印http请求的所有内容(源码)===================="
    print response.read()

    print u"====================打印http请求头===================="
    print response.headers

    print u"====================打印http某个请求头===================="
    print response.info().getheader('Content-Type')


def get_env():
    """
    查看环境变量
    :return:
    """
    print u"====================查看环境变量===================="
    print "n".join(["%s = %s" % (k, v) for k, v in os.environ.items()])
    print os.getenv("http_proxy")

def set_env():
    """
    设置环境变量
    :return:
    """
    os.putenv("http_proxy", "http://proxyaddr:<port>")

def set_proxy():
    """
    使用代理
    :return:
    """
    some_url = "www.baidu.com"
    # Use http://www.someproxy.com:3128 for http proxying
    proxies = {'http': 'http://www.someproxy.com:3128'}
    filehandle = urllib.urlopen(some_url, proxies=proxies)
    # Don't use any proxies
    filehandle = urllib.urlopen(some_url, proxies={})
    # Use proxies from environment - both versions are equivalent
    filehandle = urllib.urlopen(some_url, proxies=None)
    filehandle = urllib.urlopen(some_url)

def download_img():
    """
    实例:下载图片
    :return:
    """
    import urllib
    url = r"http://www.iteye.com/images/logo.gif"
    path = r"h:\downloads\1.jpg"
    data = urllib.urlopen(url).read()
    f = file(path,"wb")
    f.write(data)
    f.close()