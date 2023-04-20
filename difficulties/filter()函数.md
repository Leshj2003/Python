## `filter()`函数

filter()函数是Python内置函数之一，用于过滤序列中的元素，返回一个符合条件的新的序列。

filter()函数的语法如下：

filter(function, iterable)

其中，function是一个函数，接受一个参数，返回True或False；iterable是一个可迭代对象，如列表、元组、字典、集合等。

filter()函数的返回值是一个迭代器，需要用list()函数将其转换为列表或其他序列。

示例：

过滤出列表中的偶数：

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter(lambda x: x % 2 == 0, nums)
print(list(result))  # [2, 4, 6, 8, 10]
```

过滤出字典中值为偶数的键：

```python
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
result = filter(lambda x: x[1] % 2 == 0, d.items())
print(list(dict(result).keys()))  # ['b', 'd']
```