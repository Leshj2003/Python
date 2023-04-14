## sort()函数

`sorted()`是一个Python内置函数，用于对可迭代对象进行排序。它的使用方法如下：

```python
sorted(iterable, key=None, reverse=False)
```

其中，`iterable`指定要排序的可迭代对象，`key`是一个可选的函数，用于为每个元素提供一个用于排序的关键字，如果不指定，则默认使用元素本身。`reverse`用于指定是否要对结果进行反向排序，如果为`True`，则为反向排序，否则为正向排序。

`sorted()`函数返回一个新的列表，其中包含排序后的元素。

下面是一个简单的例子，展示了如何使用`sorted()`函数对列表进行排序：

```python
numbers = [2, 1, 4, 3]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 2, 3, 4]
```

在这个例子中，我们先定义了一个包含四个整数的列表`numbers`，然后使用`sorted()`函数对其进行排序得到了一个新的列表`sorted_numbers`。最后，我们使用`print()`函数输出`sorted_numbers`，确认排序结果正确。