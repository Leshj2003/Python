## `pool.map()`

`pool.map`是`multiprocessing.Pool`类中的一个方法，用于并行地执行给定的函数或方法，并返回结果列表。它将可迭代对象（如列表）的每个元素作为输入，并将其分配给进程池中的可用进程进行处理。它将并行执行函数，并收集每个函数调用的结果，最后返回一个结果列表，其中包含函数的返回值。

语法如下：
```python
map(func, iterable, chunksize=None)
```

参数说明：
- `func`：要并行执行的函数或方法。
- `iterable`：可迭代对象，将其中的每个元素作为输入传递给函数。
- `chunksize`：可选参数，用于指定每个子任务的大小。如果指定了`chunksize`，则`iterable`将被分成多个块，每个块将被提交给进程池中的一个进程进行处理。默认情况下，`chunksize`为`None`，表示将整个`iterable`作为一个块进行处理。

示例代码：
```python
import multiprocessing

def square(x):
    return x**2

if __name__ == '__main__':
    with multiprocessing.Pool() as pool:
        numbers = [1, 2, 3, 4, 5]
        results = pool.map(square, numbers)
        print(results)
```

在上面的示例中，我们定义了一个`square`函数，该函数接受一个数值并返回其平方。然后，我们创建了一个进程池`pool`，并使用`map`方法将`square`函数应用于一个数值列表`numbers`。最后，我们打印出返回的结果列表，其中包含每个数值的平方。

`pool.map`方法会自动将任务分配给进程池中的可用进程，并在后台并行执行函数。它提供了一种方便的方式来并行处理大量的输入数据，并获得相应的结果。