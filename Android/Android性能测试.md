# Android内存限制

## java虚拟机有内存使用上限的限制

<br/>
**adb shell进入手机，这此参数被纪录在/system/build.prop中,如果想直接查看可以使用adb shell getprop**


\#单个应用程序最大内存限制,超过这个值会产生OOM

```
dalvik.vm.heapgrowthlimit 
```
\#应用启动后分配的初始内存

```
dalvik.vm.heapstartsize 
```
\#单个java虚拟机最大的内存限制,超过这个值会产生OOM

```
dalvik.vm.heapsize 
```


## 小米2S的一些内存限制
<br/>

```
#查看单个应用程序最大内存限制
bixiaopeng@bixiaopengtekiMacBook-Pro ~$ adb shell getprop|grep heapgrowthlimit
|[dalvik.vm.heapgrowthlimit]: [96m]

#应用启动后分配的初始内存
bixiaopeng@bixiaopengtekiMacBook-Pro ~$ adb shell getprop|grep dalvik.vm.heapstartsize
|[dalvik.vm.heapstartsize]: [8m]

#单个java虚拟机最大的内存限制
bixiaopeng@bixiaopengtekiMacBook-Pro ~$ adb shell getprop|grep dalvik.vm.heapsize
|[dalvik.vm.heapsize]: [384m]
```

# Android内存使用
android程序内存一般限制在16M，当然也有24M的，而android程序内存被分为2部分：

native和dalvik，dalvik就是我们平常说的java堆，我们创建的对象是在这里面分配的，而bitmap是直接在native上分配的，对于内存的限制是 native+dalvik 不能超过最大限制。



用以下命令可以查看程序的内存使用情况：

```
adb shell dumpsys meminfo $package_name or $pid   //使用程序的包名或者进程id
```

查看虾米音乐app的内存占用情况

```
bixiaopeng@bixiaopengtekiMacBook-Pro ~$ adb shell dumpsys meminfo fm.xiami.main
Applications Memory Usage (kB):
Uptime: 71696500 Realtime: 98283758

** MEMINFO in pid 17340 [fm.xiami.main] **
                         Shared  Private     Heap     Heap     Heap
                   Pss    Dirty    Dirty     Size    Alloc     Free
                ------   ------   ------   ------   ------   ------
       Native        0        0        0     1976     1577      226
       Dalvik     2973    13956     2712    18691    10825     7866
       Cursor        0        0        0
       Ashmem        0        0        0
    Other dev        4       44        0
     .so mmap      894     2320      604
    .jar mmap        0        0        0
    .apk mmap      123        0        0
    .ttf mmap        0        0        0
    .dex mmap     2716        0       16
   Other mmap      204      120       96
      Unknown      808      540      804
        TOTAL     7722    16980     4232    20667    12402     8092

 Objects
               Views:        0         ViewRootImpl:        0
         AppContexts:        5           Activities:        0
              Assets:        3        AssetManagers:        3
       Local Binders:        5        Proxy Binders:       13
    Death Recipients:        0
     OpenSSL Sockets:        0

 SQL
         MEMORY_USED:        0
  PAGECACHE_OVERFLOW:        0          MALLOC_SIZE:        0
```


***其中size是需要的内存，而allocated是分配了的内存，对应的2列分别是native和dalvik，当总数也就是total这一列超过单个程序内存的最大限制时，OOM就很有可能会出现了。***

                        Shared  Private     Heap     Heap     Heap
                   Pss    Dirty    Dirty     Size    Alloc     Free
                ------   ------   ------   ------   ------   ------
       Native        0        0        0     1976     1577      226
       Dalvik     2973    13956     2712    18691    10825     7866
        TOTAL     7722    16980     4232    20667    12402     8092

# Cpu使用情况

### top命令如下：

```
adb shell 
$ top -h 
top -h 
Usage: top [-m max_procs] [-n iterations] [-d delay] [-s sort_column] [-t] [-h] 
  -m num  Maximum number of processes to display. // 最多显示多少个进程 
  -n num  Updates to show before exiting. // 刷新次数 
  -d num  Seconds to wait between updates. // 刷新间隔时间（默认5秒） 
  -s col  Column to sort by <cpu,vss,rss,thr> // 按哪列排序 
  -t      Show threads instead of processes. // 显示线程信息而不是进程 
  -h      Display this help screen. // 显示帮助文档 
$ top -n 1 
top -n 1 
```

### 举个例子：
**查看前5个进程cup的使用情况**

``bixiaopeng@bixiaopengtekiMacBook-Pro ~$ adb shell top -m 5 -s cpu``

```
User 33%, System 8%, IOW 0%, IRQ 0%
User 340 + Nice 2 + Sys 83 + Idle 596 + IOW 6 + IRQ 0 + SIRQ 2 = 1029

  PID PR CPU% S  #THR     VSS     RSS PCY UID      Name
27256  1  12% S    37 852340K 220296K  fg u0_a25   fm.xiami.main
  517  0   6% S   100 842940K 118832K  fg system   system_server
  174  0   4% S    13  66532K  14000K  fg media    /system/bin/mediaserver
27767  0   2% S    11 673928K  50516K  bg u0_a58   com.moji.mjweather
  171  0   1% S    13  97904K  51964K  fg system   /system/bin/surfaceflinger
```
### 日志说明：

```
User 35%, System 13%, IOW 0%, IRQ 0% // CPU占用率 
User 109 + Nice 0 + Sys 40 + Idle 156 + IOW 0 + IRQ 0 + SIRQ 1 = 306 // CPU使用情况 
 
PID CPU% S #THR VSS RSS PCY UID Name // 进程属性 
xx  xx% x   xx  xx  xx  xx  xx   xx 
 
CPU占用率： 
User    用户进程 
System  系统进程 
IOW IO等待时间 
IRQ 硬中断时间 
 
CPU使用情况（指一个最小时间片内所占时间，单位jiffies。或者指所占进程数）： 
User    处于用户态的运行时间，不包含优先值为负进程 
Nice    优先值为负的进程所占用的CPU时间 
Sys 处于核心态的运行时间 
Idle    除IO等待时间以外的其它等待时间 
IOW IO等待时间 
IRQ 硬中断时间 
SIRQ    软中断时间 
 
进程属性： 
PID 进程在系统中的ID 
CPU%    当前瞬时所以使用CPU占用率 
S   进程的状态，其中S表示休眠，R表示正在运行，Z表示僵死状态，N表示该进程优先值是负数。 
#THR    程序当前所用的线程数 
VSS Virtual Set Size 虚拟耗用内存（包含共享库占用的内存） 
RSS Resident Set Size 实际使用物理内存（包含共享库占用的内存） 
PCY OOXX，不知道什么东东 
UID 运行当前进程的用户id 
Name    程序名称android.process.media 
 
// ps：内存占用大小有如下规律：VSS >= RSS >= PSS >= USS 
// PSS  Proportional Set Size 实际使用的物理内存（比例分配共享库占用的内存） 
// USS  Unique Set Size 进程独自占用的物理内存（不包含共享库占用的内存）
``` 
***温馨提示：***

我们一般观察Uss来反映一个Process的内存使用情况，Uss 的大小代表了只属于本进程正在使用的内存大小,这些内存在此Process被杀掉之后，会被完整的回收掉， 

Vss和Rss对查看某一Process自身内存状况没有什么价值，因为他们包含了共享库的内存使用，而往往共享库的资源占用比重是很大的，这样就稀释了对Process自身创建内存波动。 而Pss是按照比例将共享内存分割，某一Process对共享内存的占用情况。

**so**

查看USS和PSS可以使用adb shell procrank,前提是手机需要root

```
bixiaopeng@bixiaopengtekiMacBook-Pro ~$ adb shell procrank |grep xiami
```

如果只是查看PSS也可以使用adb shell dumpsys meminfo

```
bixiaopeng@bixiaopengtekiMacBook-Pro ~$ adb shell dumpsys meminfo fm.xiami.main|grep TOTAL
        TOTAL   143070    15312   130020   135179   122279    12667        
```

***温馨提示：***

在取内存数据前可以前判断一下手机是否root, 如果root了取USS比较好一些，如果没有root取PSS也是可以的。




