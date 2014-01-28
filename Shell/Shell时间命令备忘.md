
### date命令的用法

http://blog.csdn.net/wirelessqa/article/details/9026367


### 获取当前时间

```
cur_time=`date +%Y-%m-%d-%H-%M-%S`
```

### 倒计时功能实现

```
！ /bin/bash

if [ $# -ne 1 ];then
  echo "Usage: $0 time"
  exit -1
fi

tput sc

count=$1

while true
do
  if [ $count -eq 0 ]
    then
      echo
      exit 0
    else
     let count--
   fi
   sleep 1
   tput rc
   tput ed
   echo -n $count
done
```

### 统计程序运行时间

```

starttimeH=`date +%H`
starttimeM=`date +%M`
...........
endtimeH=`date +%H`
endtimeM=`time +%M`
realtimeM=`expr $endtimeM - $starttimeM`
realtimeH=`expr $endtimeH - $starttimeH`
realtimeH1=`expr realtimeH \* 60`
reatime=`expr realtimeH1 + realtimeM`
echo "$realtime"

```

