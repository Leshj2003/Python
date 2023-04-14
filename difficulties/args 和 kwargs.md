## *args 和 **kwargs 

在 Python 中，`*args` 和 `**kwargs` 是常用的可变参数形式。它们允许我们传入任意数量的参数（包括 0 个参数），使得函数处理更加灵活。

`*args` 允许我们将任意数量的非关键字参数传递给函数，这些参数会被封装成一个元组。下面是一个例子：

```python
def foo(a, b, *args):
    print(f'a={a}, b={b}, args={args}')

foo(1, 2, 3, 4, 5)
```

输出结果如下所示：

```
a=1, b=2, args=(3, 4, 5)
```

在调用 `foo` 函数时，传入了3个参数（1，2，3）。由于 `foo` 函数中定义了 `*args`，所以所有额外的参数都被封装到一个元组 `args` 中，输出结果表明 a=1， b=2， args=(3, 4, 5)。

同样地，`**kwargs` 允许我们传递任意数量的关键字参数，这些参数将被封装为一个字典。下面是一个例子：

```python
def bar(a, b, **kwargs):
    print(f'a={a}, b={b}, kwargs={kwargs}')

bar(1, 2, x=3, y=4, z=5)
```

输出结果如下所示：

```python
a=1, b=2, kwargs={'x': 3, 'y': 4, 'z': 5}
```

在调用 `bar` 函数时，传入了 2 个参数（1，2）和3个关键字参数（x=3，y=4，z=5）。由于 `bar` 函数中定义了 `**kwargs`，因此所有额外的关键字参数都被封装到一个字典 `kwargs` 中。

需要注意的是，`*args` 和 `**kwargs` 的顺序必须是先 `*args`，再 `**kwargs`。因此，正确的函数定义形式应该是：

```python
def func(a, b, *args, **kwargs):
    pass
```