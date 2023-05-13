## `Future`对象

`Future` 对象是在 Python3 中引入的一个并发编程工具，用于表示一些异步操作的执行结果，其本质上是一个占位符对象。通常情况下，`Future` 对象在某个线程或协程中被创建，并在另一个线程或协程中被处理。这样可以在不阻塞当前线程或协程的情况下，异步地获取操作的执行结果。

以下是一个简单的例子，展示如何使用 `concurrent.futures` 模块中的 `ThreadPoolExecutor` 来创建一个 `Future` 对象，表示一个耗时的计算任务，然后在另一个线程中异步获取计算结果。

```python
import concurrent.futures

def fibonacci(n):
    """计算斐波那契数列的第n项"""
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(fibonacci, 40)  # 提交耗时的计算任务，得到一个Future对象
    result = future.result()  # 在主线程中异步获取计算结果
    print(result)

if __name__ == '__main__':
    main()
```

在上面的例子中，主线程中创建了一个 `ThreadPoolExecutor` 对象，然后调用 `submit` 方法提交一个耗时的计算任务。`submit` 方法返回一个 `Future` 对象，表示这个任务的执行结果。由于计算任务是在另一个线程中执行的，所以主线程并不会阻塞，而是继续执行后面的代码。在需要获取计算结果的时候，可以使用 `result` 方法来异步获取结果。由于计算任务耗时较长，所以在主线程中调用 `result` 方法时，程序会阻塞一段时间，直到计算任务执行完成并返回结果。