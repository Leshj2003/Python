## assert关键字

`assert`是Python中的一个关键字，用于断言某个条件是真的，如果条件不成立就会抛出异常。`assert`通常用于在代码中加入调试信息，用于检查程序的运行状态，如果发现某个条件不成立，程序就会抛出异常，停止运行。

assert的语法格式如下：

```
assert expression [, arguments]
```

其中，`expression`是要检查的条件，如果该条件为False，则抛出`AssertionError`异常；`arguments`是可选的错误信息，用于在抛出异常时输出提示信息。

下面是一个简单的示例：

```python
def divide(x, y):
    assert y != 0, "除数不能为0"
    return x / y

print(divide(10, 0))
```

在这个示例中，`assert`语句检查除数是否为0，如果是，则抛出异常，并输出错误信息"除数不能为0"。如果除数不为0，则程序正常运行，返回10/2的结果5.0。

注意，`assert`语句在生产环境中并不适合使用，因为它会中断程序的执行。在生产环境中，我们应该使用`try...except...`语句来处理异常。