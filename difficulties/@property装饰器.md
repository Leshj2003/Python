## @property装饰器

@property 是 Python 中用于定义属性的装饰器，可以将一个方法转换为只读（read-only）属性。使用 @property 装饰器定义的属性，在调用时不需要加括号，像访问实例变量一样直接访问即可。

@property 装饰器通常与 @property.setter 装饰器搭配使用，用于定义对象属性的 getter 和 setter 方法。例如：

```python
class MyClass:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
```

上面的代码定义了一个 MyClass 类，其中 x 属性被定义为使用 @property 和 @x.setter 装饰器的方法。这样，MyClass 对象的 x 属性就可以被访问和修改了，例如：

```python
>>> obj = MyClass(5)
>>> print(obj.x)
5
>>> obj.x = 10
>>> print(obj.x)
10
```

---



```python
class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def main():
    person = Person('王大锤', 12)
    person.play()
    person.age = 22
    person.play()
    # person.name = '白元芳'  # AttributeError: can't set attribute


if __name__ == '__main__':
    main()
```



---

## __slots__

`__slots__` 是一个在 Python 类中用来限定实例属性（instance attribute）的特殊变量，它是一个元组或列表，包含了当前类允许的属性名。

使用 `__slots__` 变量可以有效减少对象的内存消耗和提高访问速度，因为这样每个实例对象只需要绑定在 `__slots__` 中出现过的属性名即可，而不需要像普通对象那样动态生成实例属性的字典。但是，要注意的是，一旦定义了 `__slots__`，就不能再动态添加新的属性了。

以下是一个例子：

```python
class MyClass:
    __slots__ = ('x', 'y')

obj = MyClass()
obj.x = 1
obj.y = 2
obj.z = 3  # 这里会抛出 AttributeError 异常，因为 z 不在 __slots__ 中
```

上面的例子定义了一个 MyClass 类，并指定了 `__slots__` 变量为 ('x', 'y')。在创建 MyClass 的实例对象时，该对象只能有 x 和 y 两个属性；当我们尝试给 obj 实例对象添加 z 属性时，由于 z 不在 `__slots__` 中，所以会抛出 AttributeError 异常