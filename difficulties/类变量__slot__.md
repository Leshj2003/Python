## 类变量`__slot__`

`__slots__` 是一个特殊的类变量（class variable）在 Python 中用于限制实例的属性。它指定了一个类的实例可以拥有的属性的列表。

当使用 `__slots__` 变量时，Python 解释器会优化实例内存，仅为指定的属性分配空间，从而减少内存使用并提高访问速度。

下面是一个示例：

```python
class MyClass:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = MyClass('John', 25)
print(obj.name)  # 输出 'John'
print(obj.age)  # 输出 25

obj.address = '123 Main St'  # 抛出 AttributeError: 'MyClass' object has no attribute 'address'
```



在上面的示例中，`__slots__` 变量定义了 `MyClass` 类实例可以拥有的属性只能是 `'name'` 和 `'age'`。当我们尝试给实例设置 `'address'` 属性时，会引发 `AttributeError`，因为此属性未在 `__slots__` 中定义。

使用 `__slots__` 的主要优势是减少了每个实例的内存占用，特别是在创建大量实例时。但要注意，它也有一些限制：

1. 只有被定义在 `__slots__` 中的属性可以存在于实例中，任何不在列表中的属性赋值将引发 `AttributeError`。
2. `__slots__` 只对当前类实例起作用，不会影响继承自该类的子类实例。
3. `__dict__` 属性不可用于带有 `__slots__` 的类，因为 `__dict__` 通常用于动态添加属性。

总结起来，`__slots__` 是一个用于控制实例属性和内存优化的特殊类变量，通过限制实例可以拥有的属性列表来提高性能。然而，它也会带来一些限制和注意事项。在大多数情况下，使用基本的类属性定义即可，只有在确实需要优化内存使用时才考虑使用 `__slots__`。