## `@unique`以及`Enum`

`enum` 模块是 Python 3.4 引入的一个新特性，用于创建自定义枚举类型。在 Python 3.4 之前，开发者可以使用 `enum34` 库来实现相同的功能。`unique` 是 `enum` 模块中的装饰器，用于确保枚举类型中的所有枚举成员具有唯一值。

下面是一个使用 `enum` 模块创建自定义枚举类型的例子：

```python
from enum import Enum, unique

@unique
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```

在这个例子中，我们定义了一个名为 `Color` 的枚举类型，它有三个枚举成员：`RED`、`GREEN` 和 `BLUE`。我们使用 `@unique` 装饰器来确保这些枚举成员的值是唯一的。在这个例子中，`RED` 的值是 `1`，`GREEN` 的值是 `2`，`BLUE` 的值是 `3`。

在使用这个枚举类型时，我们可以像下面这样使用它的枚举成员：

```python
c = Color.RED
print(c)
# 输出：<Color.RED: 1>

print(c.name)
# 输出：'RED'

print(c.value)
# 输出：1
```

在这个例子中，我们将 `Color.RED` 赋值给变量 `c`。然后我们可以使用 `name` 属性来访问这个枚举成员的名称，使用 `value` 属性来访问这个枚举成员的值。