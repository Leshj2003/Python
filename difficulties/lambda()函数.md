## `lambda()`函数

lambda函数是Python中的一种匿名函数，也称为“lambda表达式”。它可以在一行代码中定义简单的函数，而无需使用def关键字来定义一个函数。

lambda函数的语法格式如下：

```python
lambda arguments: expression
```

其中，arguments是函数的参数，可以是多个，用逗号隔开；expression是函数的返回值，只能有一个。

lambda函数的返回值是一个函数对象，可以将其赋值给一个变量，也可以直接调用。

示例：

使用lambda函数计算两个数的和：

```python
add = lambda x, y: x + y
print(add(3, 5))  # 8
```

使用lambda函数过滤列表中的偶数：

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)  # [2, 4, 6, 8, 10]
```

使用lambda函数对列表进行排序：

```python
students = [('Tom', 80), ('Jerry', 90), ('Alice', 70), ('Bob', 60)]
students.sort(key=lambda x: x[1], reverse=True)
print(students)  # [('Jerry', 90), ('Tom', 80), ('Alice', 70), ('Bob', 60)]
```

lambda函数通常用于简单的函数定义，如果函数体过于复杂，建议使用def关键字定义一个普通函数来实现。