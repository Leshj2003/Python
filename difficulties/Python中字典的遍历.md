## Python中字典的遍历

Python中遍历字典有以下几种方法：

1. 使用for-in循环遍历键

```python
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
```

输出：

```python
a
b
c
```

1. 使用for-in循环遍历值

```python
d = {'a': 1, 'b': 2, 'c': 3}
for value in d.values():
    print(value)
```

输出：

```python
1
2
3
```

1. 使用items()方法同时遍历键和值

```python
d = {'a': 1, 'b': 2, 'c': 3}
for key, value in d.items():
    print(key, value)
```

输出：

```python
a 1
b 2
c 3
```

1. 使用enumerate()方法同时遍历键和值的下标

```python
d = {'a': 1, 'b': 2, 'c': 3}
for i, (key, value) in enumerate(d.items()):
    print(i, key, value)
```

输出：

```python
0 a 1
1 b 2
2 c 3
```

在遍历字典时，需要注意的是字典是无序的，遍历时键值对的顺序可能会发生变化。如果需要按照键的顺序遍历字典，可以使用sorted()函数。例如：

```python
d = {'a': 1, 'b': 2, 'c': 3}
for key in sorted(d.keys()):
    print(key, d[key])
```

输出：

```python
a 1
b 2
c 3
```