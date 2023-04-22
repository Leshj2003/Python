## python中函数上的`->`

在Python中，箭头符号 -> 被用来指定函数的返回值类型。在这个函数中，箭头符号 -> int 表示这个函数将返回一个整数类型的值。这个函数的完整定义是：

```python
def romanToInt(self, s: str) -> int:
```

其中 `self` 表示类的实例本身，`s` 是传递给函数的参数，`: str` 指定了参数 `s` 的类型为字符串类型，`-> int` 指定了函数的返回值类型为整数类型。

---

## `s:str`

在Python函数中，输入参数可以用“:”后面的数据类型进行注释。这个功能称为“函数注释”或“类型提示”。在这个函数中，“s: str”表示输入参数s的类型为str字符串类型。这种类型提示可以提高代码的可读性，并帮助IDE或静态类型检查器检测代码错误。

---



### 例题

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000
        }
        highestLevel = 1
        result = 0
        for ch in s[::-1]:
            level = mapping[ch]
            if level >= highestLevel:
                result += level
                highestLevel = level
            else:
                result -= level
        return result
```

