## 不可变集合`frozenset`

`frozenset` 是 Python 中的一个内置不可变集合类型。与普通的集合（`set`）不同，`frozenset` 对象是不可变的，即无法添加、删除或修改其元素。因此，`frozenset` 对象在创建后其元素是不可变的，但可以对其进行一些集合操作，例如交集、并集和差集等。

以下是一些关于 `frozenset` 的基本特点和用法：

1. 创建 `frozenset`：
   `frozenset` 可以通过使用 `frozenset()` 内置函数来创建，其参数可以是可迭代对象（如列表、元组、集合等）。

   示例：

   ```python
   fs1 = frozenset([1, 2, 3, 4])
   print(fs1)
   # 输出: frozenset({1, 2, 3, 4})
   
   fs2 = frozenset({3, 4, 5, 6})
   print(fs2)
   # 输出: frozenset({3, 4, 5, 6})
   ```

   

2. 不可变性：
   `frozenset` 对象是不可变的，一旦创建，就无法添加、删除或修改其元素。

   示例：

   ```python
   fs = frozenset([1, 2, 3])
   fs.add(4)  # 引发 AttributeError
   fs.remove(2)  # 引发 AttributeError
   ```

   

3. 集合操作：
   虽然 `frozenset` 本身是不可变的，但可以对它们进行集合操作，例如求交集、并集、差集和对称差等。

   示例：

   ```python
   fs1 = frozenset([1, 2, 3, 4])
   fs2 = frozenset([3, 4, 5, 6])
   
   intersection = fs1.intersection(fs2)
   print(intersection)
   # 输出: frozenset({3, 4})
   
   union = fs1.union(fs2)
   print(union)
   # 输出: frozenset({1, 2, 3, 4, 5, 6})
   
   difference = fs1.difference(fs2)
   print(difference)
   # 输出: frozenset({1, 2})
   
   symmetric_difference = fs1.symmetric_difference(fs2)
   print(symmetric_difference)
   # 输出: frozenset({1, 2, 5, 6})
   ```

   

`frozenset` 常用于需要使用不可变集合的情况，例如作为字典的键或在其他需要不可变性的上下文中。由于其不可变性，`frozenset` 对象可以被哈希，因此可用于在其他集合类型中进行查询、查找和比较