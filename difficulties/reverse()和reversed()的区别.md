## reverse()和reversed()的区别

`reverse()` 和 `reversed()` 是 Python 中用于反转序列的两个不同函数。

1. `reverse()` 是列表对象的方法，在原地反转列表中的元素顺序。它修改了原始列表，而不返回一个新的反转后的列表。使用方法是通过调用列表对象的 `reverse()` 方法。

   示例：

   ```python
   my_list = [1, 2, 3, 4]
   my_list.reverse()
   print(my_list)  # 输出: [4, 3, 2, 1]
   ```

   

2. `reversed()` 是一个内置函数，它返回一个反转后的迭代器对象，而不修改原始序列。可以将迭代器转换为列表或其他类型的序列。使用方法是将要反转的序列作为参数传递给 `reversed()` 函数。

   示例：

   ```python
   my_list = [1, 2, 3, 4]
   reversed_list = list(reversed(my_list))
   print(reversed_list)  # 输出: [4, 3, 2, 1]
   ```

   

总结：

- `reverse()` 方法用于在原地反转列表，并且不返回新的序列。它是列表对象上的方法。
- `reversed()` 函数返回一个反转后的迭代器，可以根据需要将其转换为其他类型的序列。它是内置函数，对于任何可迭代对象都可用