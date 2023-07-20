## heapq.nsmallest和heapq.nlargest

`heapq.nsmallest()` 和 `heapq.nlargest()` 是 Python 标准库中 `heapq` 模块提供的函数，用于从可迭代对象（如列表或集合）中找到最小或最大的元素。

下面是它们的使用方法和示例：

1. ```python
   heapq.nsmallest(n, iterable, key=None)
   ```

   - `n`：要返回的最小元素的数量。
   - `iterable`：可迭代对象，例如列表或集合。
   - `key`：可选参数，用于指定元素排序的关键字函数。
   - 返回一个列表，按照从最小到最大的顺序包含了 `n` 个最小的元素。

示例：

```python
import heapq

numbers = [5, 9, 3, 1, 7]
smallest = heapq.nsmallest(3, numbers)
print(smallest)  # 输出：[1, 3, 5]
```



在上面的示例中，`heapq.nsmallest(3, numbers)` 返回了列表 `numbers` 中最小的三个元素 `[1, 3, 5]`。

1. ```python
   heapq.nlargest(n, iterable, key=None)
   ```

   - `n`：要返回的最大元素的数量。
   - `iterable`：可迭代对象，例如列表或集合。
   - `key`：可选参数，用于指定元素排序的关键字函数。
   - 返回一个列表，按照从最大到最小的顺序包含了 `n` 个最大的元素。

示例：

```python
import heapq

numbers = [5, 9, 3, 1, 7]
largest = heapq.nlargest(2, numbers)
print(largest)  # 输出：[9, 7]
```



在上面的示例中，`heapq.nlargest(2, numbers)` 返回了列表 `numbers` 中最大的两个元素 `[9, 7]`。

这两个函数通过利用堆（heap）的数据结构来高效地找到最小或最大的元素。它们适用于需要在大型集合中找到最小或最大元素的场景，并且具有良好的性能。需要注意的是，调用这两个函数需要额外的空间来存储堆的数据结构。