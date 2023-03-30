## eval()函数

在 Python 中，eval() 函数是一个内置函数，用于计算传入字符串参数的表达式，并返回结果。

eval() 函数可以将字符串作为参数，将其解释为 Python 表达式并执行。例如：

```python
result = eval("2 + 3")
print(result)  # 输出 5
```


在上述代码中，字符串 "2 + 3" 被传递给 eval() 函数，然后将其解释为一个 Python 表达式并计算结果，并将结果存储在变量 result 中。

需要注意的是，eval() 函数执行的字符串应该是合法的 Python 表达式。如果字符串无法解析为合法的表达式，eval() 函数将引发 SyntaxError 异常。

在使用 eval() 函数时，应该小心避免安全问题，因为如果将用户提供的输入直接传递给 eval() 函数，可能会导致代码注入攻击等安全问题。

---

## .format()函数

在 Python 中，`.format()` 是一个字符串方法，用于将值插入到格式化字符串中。它可以用于创建更具可读性的输出，以及动态地构建字符串。



`.format()` 方法使用大括号 `{}` 作为占位符，可以在其中包含要插入的值。这些值可以是任何类型，包括字符串、数字、变量等。例如：



```python
name = "Alice"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
```



输出：



```python
My name is Alice and I am 25 years old.
```



在占位符中还可以指定格式，例如：



```python
pi = 3.141592653589793
print("The value of pi is approximately {:.2f}.".format(pi))
```



输出：



```python

The value of pi is approximately 3.14.
```



在这个例子中，`{:.2f}` 表示要将 `pi` 格式化为保留两位小数的浮点数。



除了使用大括号 `{}` 作为占位符外，还可以使用数字索引来引用要插入的值。例如：



```python
name = "Alice"
age = 25
print("My name is {0} and I am {1} years old. {0} is a nice name.".format(name, age))
```



输出：



```python

My name is Alice and I am 25 years old. Alice is a nice name.
```



在这个例子中，`{0}` 和 `{1}` 分别引用了第一个和第二个参数。

---

