
## 多线程简单举例

```
import threading，time

def test(str,n):
    for i in range(n):
    print(str,i)
    time.sleep(1)

#target是调用的函数，args是给函数传的参数
t=threading.Thread(target=test,args=('线程1',3))
t2=threading.Thread(target=test,args=('线程2',3))
t.start()
t2.start()
```

### 运行结果:

```
bixiaopeng@bixiaopengtekiMacBook-Pro Python$ python test_thread2.py
线程1 0
线程2 0
线程1 1
线程2 1
线程1 2
线程2 2
```


# python多线程(2)–互斥锁

多线程提升了程序执行效率的同时，也产生了资源的利用问题。假如有两条线程，同时操作一个变量，就会造成结果不准确的现象。看下面代码

```
import threading

count = 0

def addone():
 	global count
 	for i in range(100000):
 		count += 1

threads=[]

for i in range(5):
 	threads.append(threading.Thread(target=addone))

for j in threads:
 	j.start()
 	print(j.getName())

for k in threads:
 	k.join()

print(count)	
```
### 运行结果

在这里我创建了5条线程，每条线程要做的就是把count加1，每条线程加10W次，5条线程执行完毕之后count的结果应该是50W，但事实上运行结果如下：


```
bixiaopeng@bixiaopengtekiMacBook-Pro Python$ python test_thread.py
Thread-1
Thread-2
Thread-3
Thread-4
Thread-5
432860
```

事实上，多条线程操作同一个变量时，可能某条线程修改变量后，其他的线程并没有获得该变量的最新结果，从而出现结果不准确的现象。

因此，为了解决这个问题，我们可以使用互斥锁。在某条线程对变量进行操作时，可以给变量加锁，其他线程只能等待锁释放后才可以操作该变量，这样确保每次取到的变量都是准确的。下面是修改后的代码：

```
import threading

count = 0

def addone():
 	global count,lock
 	for i in range(100000):
 		#如果count+1的时候不加锁，多个线程同时作用于count上，会导致有的线程没加到
 		lock.acquire() 
 		count += 1
 		lock.release()

threads=[]

lock = threading.Lock() #创建锁
for i in range(5):
 	threads.append(threading.Thread(target=addone))

for j in threads:
 	j.start() #所有子线程执行
 	print(j.getName())

for k in threads:
 	k.join() #等待所有子线程执行完毕

print(count)	
```

### 运行结果:

```
bixiaopeng@bixiaopengtekiMacBook-Pro Python$ python test_thread.py
Thread-1
Thread-2
Thread-3
Thread-4
Thread-5
500000
```

# python多线程(3)–可重入锁

http://zzpei.sinaapp.com/?p=33

----
####  微信公众帐号: wirelessqa 
![wirelessqa](../img/qrcode_for_gh_fdde1fe2880a_258.jpg)

#### 关于作者：

**作者:** 毕小朋 | 老 毕  **邮箱:** <wirelessqa.me@gmail.com> 

**微博:** [@WirelessQA](http://www.weibo.com/wirelessqa) **博客:** <http://blog.csdn.net/wirelessqa>

----