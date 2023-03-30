## Day07

---

## 为什么需要列表

* 变量可以存储一个元素，而列表可以存储n个元素的”引用“
* 相当于其他语言的数组

```python
a = 10
lst = ['hello','world',98]
print(id(lst))
print(type(lst))
print(lst)
```

---

## 列表对象的创建

``` python
# 使用[]创建
lst1 = ['hello','world',98]
print(lst1)	#有序排序
print(lst[0]，lst[-3])	#索引映射
# 使用内置函数list()
lst2 = list(['hello','world',98])
```

| id:123       | id:456       | id:789    |
| ------------ | ------------ | --------- |
| type :str    | type :str    | type :int |
| value :hello | value :world | value :98 |

### 列表的特点

* 列表元素按顺序有序排序
* 索引映射唯一一个数据
* 列表可以存储重复的数据
* 任意数据类型混存
* 根据需要动态分配和回收内存

---

## 获取指定元素的索引

* index()

  * 如列表中存在n个相同，只返回相同元素中的第一个元素的索引
  * 如果查询的元素在列表中不存在，则会抛出`ValueError`
  * 还可以在指定的start和stop之间进行查找

* 获取单个元素

  * 正向索引从0到N-1  eg: `lst[0]`
  * 逆向索引-N到-1   eg: `lst[-N]`
  * 指定索引不存在，抛出`indexError`

  

```python
lst = ['hello','world',98.'hello']
print(lst.index('hello'))
#报错ValueError
#print(lst.index('Python'))
#print(lst.index('hello',1,3))
```

```python
lst = ['hello','world',98.'hello','world',234]
print(lst[2])
print(lst[-3])
#print(lst[10])
```

