## `collections`模块

`collections` 是 Python 标准库中的一个模块，提供了一些额外的数据类型和数据结构，用于替代内置数据类型，增强了数据处理的灵活性和效率。

下面是一些 `collections` 模块中常用的数据类型和数据结构：

1. `namedtuple(typename, field_names)`
   - 创建一个具名元组，它是一个轻量级的类，用于创建具有命名字段的数据对象。
   - 示例：
     ```python
     from collections import namedtuple
     
     Point = namedtuple('Point', ['x', 'y'])
     p = Point(1, 2)
     print(p.x, p.y)  # 输出：1, 2
     ```

2. `Counter(iterable)`
   - 创建一个计数器，用于统计可迭代对象中元素的出现次数。
   - 示例：
     ```python
     from collections import Counter
     
     data = [1, 2, 2, 3, 3, 3]
     counter = Counter(data)
     print(counter)  # 输出：Counter({3: 3, 2: 2, 1: 1})
     ```

3. `deque(iterable, maxlen=None)`
   - 创建一个双端队列（deque），可以在两端进行高效地插入和删除操作。
   - 示例：
     ```python
     from collections import deque
     
     dq = deque([1, 2, 3])
     dq.append(4)
     dq.appendleft(0)
     print(dq)  # 输出：deque([0, 1, 2, 3, 4])
     ```

4. `defaultdict(default_factory)`
   - 创建一个字典，提供了默认值函数，可以指定默认值的类型和值。
   - 示例：
     ```python
     from collections import defaultdict
     
     d = defaultdict(int)
     d['a'] += 1
     d['b'] += 2
     print(d)  # 输出：defaultdict(<class 'int'>, {'a': 1, 'b': 2})
     ```

5. `OrderedDict`
   - 创建一个有序字典，保持插入顺序，并支持按插入顺序遍历字典。
   - 示例：
     ```python
     from collections import OrderedDict
     
     od = OrderedDict()
     od['a'] = 1
     od['b'] = 2
     od['c'] = 3
     for key, value in od.items():
         print(key, value)  # 输出：a 1, b 2, c 3
     ```

这些只是 `collections` 模块提供的一小部分功能，还有其他更多的数据类型和数据结构可供使用。这些数据类型和数据结构能够更好地满足特定的需求，提供了更方便和高效的数据处理方式。

---

```python
"""
找出序列中出现次数最多的元素
"""
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(3))
```

