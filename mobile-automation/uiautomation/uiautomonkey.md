## UIAutoMonkey.js下载地址

https://github.com/jonathanpenn/ui-auto-monkey

## UIAutoMonkey.js脚本配置

```
 config: {
        numberOfEvents: 1000,
        delayBetweenEvents: 0.05,    // In seconds

        //各事件的几率.
        // 数字越大，几率越大.
        eventWeights: {
            tap: 30,
            drag: 1,
            flick: 1,
            orientation: 1,
            clickVolumeUp: 1,
            clickVolumeDown: 1,
            lock: 1,
            pinchClose: 10,
            pinchOpen: 10,
            shake: 1
        },

        // Probability that touch events will have these different properties
        touchProbability: {
            multipleTaps: 0.05,
            multipleTouches: 0.05,
            longPress: 0.05
        }
        },
```
## UIAutoMonkey.js参数说明

参数|说明
----|----
numberOfEvents|需要产生随机事件的个数。
delayBetweenEvents|两个事件之间的延迟时间。这个值一般是需要调整的。如果该值为0，那么脚本会尽可能快的向设备发送事件。
eventWeights|每个事件的触发几率。如果tab事件的值为100、orientation事件的值为1，那么tab事件触发的几率就是orientation的100倍。
touchProbability|控制着不同种类的tab事件。默认情况下，tab就是单击事件。调整这些参数可以设置双击、长按事件发生的频率。这些值要界于0、1之间。