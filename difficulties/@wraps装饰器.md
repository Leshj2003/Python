## @wraps装饰器

`@wraps` 是 Python `functools` 模块中的一个装饰器，它用于将被装饰的函数的属性复制给装饰器函数，以使被装饰函数在被调用时能够像正常函数一样，保留其元数据信息（例如函数名、参数列表、文档字符串等）。下面是一个例子：

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # 使用 @wraps 装饰器
    def wrapper(*args, **kwargs):
        """这是文档字符串"""
        print('调用函数')
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def my_function():
    """这是文档字符串"""
    print('函数被调用')

print(my_function.__name__)  # 打印出 'my_function'
print(my_function.__doc__)   # 打印出 '这是文档字符串'
```

在上面的例子中，`my_decorator` 是一个装饰器函数，它将 `my_function` 函数装饰起来。由于在 `my_decorator` 内部对 `my_function` 进行了包裹，因此 `my_function` 的元数据信息（即函数名和文档字符串）被丢失。如果在 `my_decorator` 内部使用了 `@wraps(func)` 装饰器，那么被装饰函数 `my_function` 的元数据信息就会被复制到装饰器函数 `wrapper` 上，从而在 `my_function` 被调用时能够像正常函数一样保留它的元数据信息。