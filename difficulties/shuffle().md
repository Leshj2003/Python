## shuffle()

`shuffle()`是Python内置的random模块中的一个函数，用于原地随机打乱可变序列（如列表）。它将列表的元素顺序进行随机排列，从而改变原始列表的排列顺序。

以下是使用`shuffle()`函数对列表进行随机打乱的示例代码：

```python
import random

my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)
```



运行上述代码，会输出一个随机顺序的列表，例如`[3, 2, 5, 1, 4]`。

需要注意的是，`shuffle()`函数会直接修改原始列表，不会返回新的打乱顺序的列表。因此，在对列表进行打乱操作之前，最好先创建原始列表的副本，以便保留原始顺序。

`shuffle()`函数可以用于多种可变序列类型，如列表、bytearray等。但请注意，对于字符串（str）等不可变序列类型，无法直接使用`shuffle()`函数。

如果需要对字符串进行乱序操作，可以先将其转换为可变序列（如列表），然后再使用`shuffle()`函数。例如：

```python
import random

my_string = "Hello"
my_list = list(my_string)
random.shuffle(my_list)
shuffled_string = ''.join(my_list)
print(shuffled_string)
```



运行上述代码，会输出一个随机打乱顺序的字符串，例如`lHleo`。

总之，`shuffle()`函数是一个方便的方法，可用于将可变序列的元素进行随机排列，实现打乱顺序的效果。