## split()函数

在 Python 中，split() 函数可以将一个字符串根据指定的分隔符分割成一个列表。

split() 函数的基本语法为：
```python
str.split(sep=None, maxsplit=-1)
```

其中，sep 参数为分隔符，默认为 None，表示使用空格或者多个空格作为分隔符；maxsplit 参数表示最多分割次数，默认为 -1，表示不限制分割次数。

下面是一个简单的例子，演示了如何使用 split() 函数将字符串分割成列表：

```python
str = "hello world"
list = str.split()
print(list)  # 输出: ['hello', 'world']
```

另外，也可以使用 split() 函数指定自定义的分隔符，例如：

```python
str = "a,b,c,d"
list = str.split(",")
print(list)  # 输出: ['a', 'b', 'c', 'd']
```

---

## map()函数

在 Python 中，`map()` 是一个内置函数，它接受两个参数：一个函数和一个可迭代对象。`map()` 将传入的函数应用于可迭代对象中的每个元素，并返回一个新的可迭代对象，其中包含每个元素被函数处理后的结果。

下面是一个简单的例子，演示如何使用 `map()` 函数将一个列表中的每个元素平方：

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))  # 输出 [1, 4, 9, 16, 25]
```

在上面的例子中，我们首先定义了一个列表 `numbers`，其中包含整数 1 到 5。然后，我们使用 `map()` 函数和一个 lambda 函数来创建一个新的可迭代对象 `squared_numbers`，其中包含 `numbers` 列表中每个元素的平方。最后，我们将 `squared_numbers` 转换为一个列表，并使用 `print()` 函数将其打印出来。

需要注意的是，`map()` 函数返回的是一个迭代器对象，而不是一个列表。如果需要将其转换为列表，可以使用 `list()` 函数。

---

## 鸡兔同笼

鸡兔同笼问题是一个经典的数学问题，它涉及到代数方程和整数解的求解。假设一个笼子里面有若干只鸡和兔子，它们的总数量为 `n`，总腿数为 `m`。问笼子里面分别有多少只鸡和兔子？



我们可以使用 Python 编写一个解决鸡兔同笼问题的函数，如下所示：



```python
def chicken_rabbit(n, m):
    for i in range(n+1):
        j = n - i
        if 2*i + 4*j == m:
            return i, j
    return None
```



该函数接受两个参数 `n` 和 `m`，分别表示鸡兔总数和总腿数。函数使用一个 for 循环来枚举鸡的数量 `i`，然后计算出兔子的数量 `j`。接着，函数检查当前的 `i` 和 `j` 是否满足总腿数的条件，如果满足，则返回 `i` 和 `j` 的值。如果循环结束后仍然没有找到合适的解，则返回 `None`。



下面是一个使用该函数的例子：



```python
result = chicken_rabbit(10, 32)
if result:
    print("鸡的数量为 %d，兔子的数量为 %d" % result)
else:
    print("无解")
```



在上面的例子中，我们调用 `chicken_rabbit()` 函数来求解鸡兔同笼问题，其中鸡兔总数为 10，总腿数为 32。如果函数返回了一个非空的结果，则打印出鸡和兔子的数量。否则，打印出“无解”。