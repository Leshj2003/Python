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
print(lst[1:6])
print(lst[1:6:])
#start = 1,stop = 6,step = 2
print(lst[1:6:2])
#stop = 6,step = 2,start采用默认
print(lst[:6:2])
#start = 1,step = 2,stop采用默认
print(lst[1::2])
print('--------------步长为负数--------------')
print('原列表',lst)
print(lst[::-1])
#start = 7,stop省略，step=-1
print(lst[7::-1])
#start = 6,stop = 0,step = -2
print(lst[6:0:-2])
```



---

## 列表元素的判断及遍历

* 判断指定元素在列表中是否存在
  * ​	元素 in 列表名
  * ​    元素 not in 列表名
* 列表元素的遍历
  * for 迭代变量 in 列表名

```python
print('p' in 'python')
print('k' not in 'python')

lst = [10,20,'python','hello']
print(10 in lst)
print(100 in lst)
print(10 not in lst)
print(100 not in lst)

for item in lst:
    print(item)
```



---

## 列表元素的添加操作

| 增加操作 | 方法       | 操作描述                             |
| -------- | ---------- | ------------------------------------ |
|          | `append()` | 在列表的末尾添加一个元素             |
|          | `extend()` | 在列表的末尾至少添加一个元素         |
|          | `insert()` | 在列表的任意位置添加一个元素         |
|          | 切片       | 在列表的任意位置添加至少添加一个元素 |

```python
#向列表的末尾添加一个元素
lst = [10,20,30]
print('添加元素之前',lst,id(lst))
lst.append(100)
print('添加元素之后',lst,id(lst))
```

```python
lst2 = ['hello','world']
#lst.append(lst2)	#将lst2作为一个元素添加到列表的末尾,输出[10,20,30,100,['hello','world']]
lst.extend(lst2)	#输出[10,20,30,100,'hello','world']
print(lst)

```

```python
#在任意位置上添加一个元素
lst.insert(1,90)
print(lst)	#输出[10,90,20,30,100,'hello','world']

lst3 = [True,False,'hello']
#任意的位置上田添加N多个元素
lst[1:] = lst3
print(lst)	#输出[10,True,False,'hello']
```



---

## 列表元素的删除操作

| 删除操作 | 方法       | 操作描述                                                     |
| -------- | ---------- | ------------------------------------------------------------ |
|          | `remove()` | 1、一次删除一个元素<br />2、重复元素只删除第一个<br/>3、元素不存在 |
|          | `pop()`    | 1、删除一个指定索引位置上的元素<br/>2、指定索引不存在抛出`IndexError`<br/>3、不限定索引，删除列表中最后一个元素 |
|          | 切片       | 一次至少删除一个元素                                         |
|          | `clear()`  | 清空列表                                                     |
|          | `del`      | 删除列表                                                     |

```python
lst = [10,20,30,40,50,60,30]
lst.remove(30)	#从列表中列表中移除一个元素，如果有重复元素只移除第一个元素
print(lst)
#lst.remove(100)
```

```python
#pop()根据索引移除元素
lst.pop(1)
print(lst)
#lst.pop(5)
lst.pop()	#不指定参数，删除列表中最后一个
```

```python
print(------------切片操作删除至少一个元素，将产生一个新的列表对象------------)
new_list = lst[1:3]
print('原列表',lst)
print('切片后的列表',new_lst)

'''不产生新的列表对象，而是删除原列表中的内容'''
lst[1:3] = []
print(lst)
```



