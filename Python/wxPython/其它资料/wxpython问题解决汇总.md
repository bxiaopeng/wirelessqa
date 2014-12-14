
## 1. ImportError: No module named images  

```
说明: images 只不过是wxpython自带demo中的一个文件

体验wxpython IN action的时候报错:

ImportError: No module named images

解决办法

第一步:
import images
替换为
import wx.py.images as images

第二步:
images.getVippiBitmap()
替换为
images.getPyBitmap()
```