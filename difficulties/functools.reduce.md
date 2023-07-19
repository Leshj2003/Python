## `functools.reduce`

`functools.reduce()` 是 Python 的一个内置函数，它位于 `functools` 模块中。这个函数被用于对一个可迭代对象进行累积操作，基于指定的函数规则。

`functools.reduce()` 的语法如下：

```python
functools.reduce(function, iterable, initializer=None)
```



参数说明：

- `function`：要应用于可迭代对象中元素的二元操作函数。它接受两个参数，代表当前的累积结果和可迭代对象中的一个元素，然后返回一个新的累积结果。
- `iterable`：要进行操作的可迭代对象，可以是一个列表、元组或其他可迭代对象。
- `initializer`（可选）：可选的初始值，作为累积的初始结果。如果未提供初始值，则将使用可迭代对象的第一个元素作为初始结果，并从第二个元素开始进行累积操作。

`functools.reduce()` 函数将会按照以下步骤进行操作：

1. 从可迭代对象中取出第一个元素作为初始结果（或使用提供的初始值）。
2. 将初始结果和可迭代对象中下一个元素传递给函数进行操作，得到一个新的累积结果。
3. 将新的累积结果和下一个元素再次传递给函数进行操作，得到另一个新的累积结果。
4. 重复上述步骤，直到处理完可迭代对象中的所有元素。
5. 返回最终的累积结果。

以下是一个示例：

```python
import functools

numbers = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x, y: x + y, numbers)

print(result)
```



运行以上代码，将输出以下结果：

```python
15
```



在这个示例中，我们使用 `functools.reduce()` 函数和加法的匿名函数对列表 `numbers` 进行累积操作。根据加法操作的规则，对列表中的元素逐个相加，得到最终的结果 `15`。

需要注意的是，`functools.reduce()` 函数在 Python 3 中已经从内置函数移动到了 `functools` 模块中，因此需要先导入 `functools` 模块才能使用。另外，累积函数应当是一个纯函数，不应该有副作用，并且内部不应改变任何外部状态，以确保正确的累积结果。



![img](https://ai.chat86.cn/svg/bottomfff-bc27d346.svg)