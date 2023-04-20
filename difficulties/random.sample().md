## `random.sample()`

`random.sample()` 是 Python 标准库 `random` 模块中的函数，用于从序列中随机选择若干个元素，返回一个新的列表。它的语法如下：

```python
random.sample(sequence, k)
```

其中：

- `sequence`：表示要从中抽取元素的序列，可以是列表、元组、集合等可迭代对象；
- `k`：表示要从序列中随机选择的元素个数，必须小于等于序列的长度。

`random.sample()` 的特点是不会改变原序列，而是生成一个全新的列表来存储结果，如果 k 超出了 sequence 的范围（即 k>len(sequence)），则会引发 ValueError 异常。

下面是 `random.sample()` 函数的一个简单例子:

```python
import random

lst = [1, 2, 3, 4, 5, 6]
sample_lst = random.sample(lst, 3)
print(sample_lst)   # 输出结果类似于 [6, 2, 4]
```

在这个例子中，我们先定义了一个列表 `lst`，然后使用 `random.sample()` 函数从 `lst` 中随机抽取 3 个元素，并将结果存储在列表 `sample_lst `中输出。由于 `random.sample()` 会生成一个新的列表，因此原来的 `lst` 不受影响。