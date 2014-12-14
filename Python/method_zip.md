# zip就是把2个数组揉在一起


## 1. zip举例

```
>>> x=[1, 2, 3, 4, 5 ]
>>> y=[6, 7, 8, 9, 10]
>>> zip(x,y)
[(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]

# 如果你有2组坐标，你想两两对应的相加，那么zip函数就很有用了
```

## 2. zip创建字典

```
>>> name=['bob','tom','kitty']
>>> score=[99,88,77]
>>> achiev_dic=dict(zip(name,score))
>>> print achiev_dic
{'bob': 99, 'kitty': 77, 'tom': 88}
```