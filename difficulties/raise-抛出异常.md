## raise-抛出异常

`raise` 用于抛出异常，可以使用不同类型的异常类来表达不同种类的错误。语法如下：

```python
raise [Exception [, args [, traceback]]]
```

其中，`Exception` 是要抛出的异常类，`args` 是异常类初始化参数的元组（可选），`traceback` 是引发异常时的跟踪信息（可选）。

举例来说，以下代码演示了如何通过 `raise` 抛出一个自定义异常类的对象：

```python
class CustomError(Exception):
    pass

def function_with_error():
    raise CustomError("Something went wrong.")

try:
    function_with_error()
except CustomError as e:
    print(e) # 输出 "Something went wrong."
```

当某些情况下检测到错误时，可以使用 `raise` 抛出异常并停止当前函数或程序的执行，转而由上层调用者处理该异常。在使用 `raise` 抛出异常时，需要选择适当的异常类型以及提供足够精确的异常消息，以便调试和排除错误。