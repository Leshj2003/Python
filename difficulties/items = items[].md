## `items = items[:]`

这行代码 `items = items[:]` 是为了创建列表 `items` 的一个副本，以防止对原始列表进行修改。

在函数参数中，我们传入的是一个列表对象 `items`。然而，Python 中的列表是可变对象，如果直接在函数内部对 `items` 进行操作，可能会修改传入的原始列表。为了避免这种情况，我们使用切片操作 `items[:]` 来创建一个新的列表副本。

通过使用切片操作，我们实际上创建了一个与原始列表具有相同元素的新列表。这样，在函数内部对新列表进行排序操作，就不会影响到原始列表。

这种方法称为列表的浅拷贝，它只拷贝了列表的一层，而不是深度拷贝整个对象及其嵌套的元素。对于简单的列表，这样的浅拷贝足够保证在函数内部操作期间不影响原始列表。如果列表中包含嵌套的可变对象（如列表或字典），可能需要进行更深层次的拷贝来确保不会修改原始对象。

总之，`items = items[:]` 这行代码用于创建一个列表副本，以确保在函数内部对列表进行操作时不会影响到原始列表。

```python
def select_sort(item,comp = lambda x,y : x < y):
	items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1,len(items)):
            if comp(items[j],items[min_index]):
                min_index = j
        items[i],items[min_index] = items[min_index],items[i]
    return items
```

