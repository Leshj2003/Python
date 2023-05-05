## abc库

`abc` 模块是 Python 中用于实现抽象类和接口的标准库。

抽象类是指不能被直接实例化但可以被继承的类。通常用于定义基类中必须实现的方法，强制子类实现这些方法来满足多态要求。使用 `abc` 模块可以方便地定义和使用抽象类，示例如下：

```python
import abc

class Database(abc.ABC):
    @abc.abstractmethod
    def connect(self, host, user, password):
       pass
    
    @abc.abstractmethod
    def query(self, sql):
        pass

class MySQL(Database):
    def connect(self, host, user, password):
        # 实现 MySQL 数据库连接逻辑
        pass
    
    def query(self, sql):
        # 实现 MySQL 查询逻辑
        pass
```

上面的例子中，定义了一个名为 `Database` 的抽象类，其中包含两个抽象方法：`connect()` 和 `query()`。这两个方法都没有实现，需要在子类中进行具体实现。如果一个类继承了 `Database` 类但未实现其中的抽象方法，则无法实例化该子类。

除了抽象类，`abc` 模块还提供了一个重要的辅助函数 `@abstractmethod`，用于声明抽象方法。这个装饰器需要放在抽象方法的前面，以表明该方法是抽象方法。

另外，Python 中并没有直接的接口（interface）机制。但是，通过使用抽象类和 `@abstractmethod` 装饰器可以模拟出接口，将必须实现的方法表示为抽象方法即可。