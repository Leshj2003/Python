## `queue.put()`

`queue.put()`是`Queue`类中的一个方法，用于将元素放入队列中。它将指定的元素放入队列的末尾，并返回`None`。

语法如下：
```python
put(item, block=True, timeout=None)
```

参数说明：
- `item`：要放入队列的元素。
- `block`：可选参数，指示当队列已满时是否阻塞。如果设置为`True`（默认值），则在队列有空间之前，`put()`方法将一直阻塞。如果设置为`False`，则在队列已满时，`put()`方法将引发`queue.Full`异常。
- `timeout`：可选参数，用于指定阻塞时间的最大秒数。如果指定了`timeout`，并且在指定的时间内队列仍然是满的，则会引发`queue.Full`异常。

示例代码：
```python
import queue

if __name__ == '__main__':
    q = queue.Queue()

    # 将元素放入队列
    q.put(1)
    q.put(2)
    q.put(3)

    # 打印队列中的元素
    while not q.empty():
        print(q.get())
```

在上面的示例中，我们创建了一个队列`q`，并使用`put()`方法将整数`1`、`2`和`3`放入队列中。然后，我们使用`get()`方法从队列中取出元素，并打印出来。`queue`模块提供了线程安全的队列实现，可以在多线程或多进程环境中使用。`put()`方法可以用于向队列中添加元素，而`get()`方法用于从队列中获取元素。