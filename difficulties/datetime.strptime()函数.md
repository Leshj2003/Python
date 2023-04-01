## `datetime.strptime()`函数

`datetime.strptime()`函数是Python中用于将字符串解析成datetime对象的函数。它的语法为：

```python

datetime.datetime.strptime(date_string, format)
```

其中，`date_string`是待解析的字符串，`format`是`date_string`的格式字符串。函数返回一个对应于`date_string`的datetime对象。

例如，如果要将字符串"2023-02-27 13:30:00"解析为datetime对象，可以使用以下代码：

```python
from datetime import datetime
dt = datetime.strptime("2023-02-27 13:30:00", "%Y-%m-%d %H:%M:%S")
print(dt)
```

输出结果为：

```python

2023-02-27 13:30:00
```

在格式字符串中，各种日期和时间元素的符号有特定的含义。例如，"%Y"表示年份（4位），"%m"表示月份（2位），"%d"表示日期（2位），"%H"表示小时（24小时制，2位），"%M"表示分钟（2位），"%S"表示秒（2位）等等。可以根据需要组合这些元素，生成相应的格式字符串。



---

## 时间差练习

获得用户输入的两个与时间相关的字符串，两个时间用逗号分隔，每个时间字符串格式示例如下：2018年08月01日17点21分21秒。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‫‬ 

计算两个时间差的绝对值，输出相差的完整天数。

```python
from datetime import datetime

# 获取用户输入的两个时间字符串
time_str1, time_str2 = input("请输入两个时间字符串，用逗号分隔：").split(',')

# 将时间字符串转换为 datetime 对象
time1 = datetime.strptime(time_str1, '%Y年%m月%d日%H点%M分%S秒')
time2 = datetime.strptime(time_str2, '%Y年%m月%d日%H点%M分%S秒')

# 计算两个 datetime 对象的差值
delta = abs(time2 - time1)

# 输出相差的完整天数
print(delta.days)

```

可以使用 Python 中的 datetime 模块来解决这个问题。具体实现步骤如下：

1. 使用 `input()` 函数获取用户输入的两个时间字符串。
2. 使用 `strptime()` 函数将时间字符串转换为 datetime 对象。
3. 使用 `timedelta()` 函数计算两个 datetime 对象的差值，取绝对值。
4. 使用 days 属性获取时间差的完整天数，输出结果。

注意，上面代码中的时间字符串格式需要和 `strptime()` 函数的第二个参数保持一致。



---

## abs()函数

在Python中，`abs()`函数是内置函数之一，它用于计算一个数字的绝对值，即返回该数字的正数值。`abs()`函数可以用于整数、浮点数、复数等数字类型。

例如，`abs(-3)`返回值为3，`abs(3.14)`返回值为3.14，`abs(1+2j)`返回值为2.23606797749979，这里`j`表示复数单位。如果传入的参数不是数字类型，`abs()`函数会抛出`TypeError`异常。



---

## `isdigit()`函数

在Python中，`isdigit()`是字符串类型的一个方法，用于判断字符串是否只包含数字字符。其语法格式如下：

```python

str.isdigit()
```

其中，str代表要进行判断的字符串，返回值为布尔类型，如果字符串中只包含数字字符则返回True，否则返回False。

例如，下面的代码演示了`isdigit()`方法的使用：

```python
string1 = "123456"
string2 = "12a34"
print(string1.isdigit())  # True
print(string2.isdigit())  # False
```

在上述代码中，string1只包含数字字符，因此调用`isdigit()`方法返回True；而string2中包含了字母字符，因此调用`isdigit()`方法返回False。



---

## 凯撒密码

```python
import string

def caesar_cipher(text):
    """接收一个字符串为参数，采用字母表和数字中后面第3个字符代替当前字符的方法
    对字符串中的字母和数字进行替换，实现加密效果，返回值为加密的字符串。
    例如：2019 abc 替换为5342 def """
# 定义三个字符串，包含全部的小写字母、大写字母和数字字符
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    digits = string.digits

    # 将每个字符向后偏移3位后替换成密文
    ciphertext = ''
    for c in plaintext:
        if c in lowers:
            ciphertext += lowers[(lowers.index(c) + 3) % 26]
        elif c in uppers:
            ciphertext += uppers[(uppers.index(c) + 3) % 26]
        elif c in digits:
            ciphertext += str((int(c) + 3) % 10)
        else:
            ciphertext += c

    return ciphertext

if __name__ == '__main__':
    plaintext = input()
    print(caesar_cipher(plaintext))
```

在Python中，`string`模块提供了一个字符串常量集合，其中包含各种ASCII字符，如数字、大小写字母、标点符号和空格等。这个模块中定义了三个常量，分别是：

- `string.ascii_lowercase`: 包含所有小写字母的字符串。
- `string.ascii_uppercase`: 包含所有大写字母的字符串。
- `string.digits`: 包含所有数字字符的字符串。

这些常量可以用来进行字符串操作，例如在一个字符串中查找所有的数字或字母，或者用它们来构造一些特定的字符串。在题目中，`lowers`、`uppers`和`digits`分别被赋值为所有小写字母、所有大写字母和所有数字字符的字符串，以便进行凯撒加密。