### 类之间的关系

简单的说，类和类之间的关系有三种：is-a、has-a和use-a关系。

- is-a关系也叫继承或泛化，比如学生和人的关系、手机和电子产品的关系都属于继承关系。
- has-a关系通常称之为关联，比如部门和员工的关系，汽车和引擎的关系都属于关联关系；关联关系如果是整体和部分的关联，那么我们称之为聚合关系；如果整体进一步负责了部分的生命周期（整体和部分是不可分割的，同时同在也同时消亡），那么这种就是最强的关联关系，我们称之为合成关系。
- use-a关系通常称之为依赖，比如司机有一个驾驶的行为（方法），其中（的参数）使用到了汽车，那么司机和汽车的关系就是依赖关系。



---

## Python 中实现抽象基类

Python 中实现抽象基类（Abstract Base Class）一般需要用到 `ABCMeta` 和 `abstractmethod` 两个元素。ABC 即` Abstract Base Class`，它是定义抽象类的 Python 模块，用于检查继承自某个基类的子类是否按照约定完全地实现了所有抽象方法等特性。

以下是一个用 Python 实现抽象基类的例子：

```python
from abc import ABCMeta, abstractmethod

class MyABC(metaclass=ABCMeta):

    @abstractmethod
    def do_something(self):
        pass
    
    @abstractmethod
    def do_another_thing(self):
        pass
    
    def common_method(self):
        # 这是一个普通方法
        print('This is a common method in the base class.')

class MyClass(MyABC):

    def do_something(self):
        # 必须实现父类中声明的所有抽象方法
        print('Doing something...')

    def do_another_thing(self):
        # 必须实现父类中声明的所有抽象方法
        print('Doing another thing...')
        
obj = MyClass()
obj.do_something()  # Doing something...
obj.do_another_thing()  # Doing another thing...
obj.common_method()  # This is a common method in the base class.
```

在这个例子中，我们首先定义了一个抽象基类 `MyABC`，并声明了两个抽象方法 `do_something` 和 `do_another_thing`。这两个方法都没有实际的实现，只是用 `@abstractmethod` 标记了其为抽象方法。`MyABC` 继承于 `ABCMeta` 类，这样可以在子类继承并实现所有抽象方法后，检查是否缺少了一些必须的方法。

接着我们定义了一个 `MyClass` 类，该类继承了`MyABC`。注意，在 `MyClass` 中必须重写 `MyABC` 所有的抽象方法，否则会在运行时引发异常。同时，`MyClass` 实现了一个普通方法 common_method，这个方法不是抽象方法，因此可以被直接子类继承并使用。

最后我们创建了 `MyClass` 的实例对象 obj，并使用其中的方法。在运行过程中，如果忘记实现任何一个抽象方法，Python 解释器就会抛出 `TypeError` 异常。