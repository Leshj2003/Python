## Day08

---

## 获取多个列表的多个元素—切片操作

列表名[`start`:`stop`:`step`]

* 切片的结果：原列表的拷贝
* 切片的范围：[start,stop)
* step默认为1
* step为正数：
  * [:`stop`:`step`]	第一个元素默认列表第一个元素
  * [`start`::`step`]    最后一个元素默认列表最后一个元素
* step为负数：
  * [:`stop`:`step`]	最后一个元素默认列表最后一个元素
  * [`start`::`step`]    第一个元素默认列表第一个元素

```python
lst = [10,20,30,40,50,60,70,80]
print(lst[1:6:1])
print('原列表',id(lst))
lst2 = lst[1:6:1]
print('切的片段',id(lst2))

```

