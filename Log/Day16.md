## Day16

---

## 类的浅拷贝与深拷贝

* 变量的赋值操作
  * 只是形成两个变量，实际上还是指向同一个对象
* 浅拷贝
  * Python拷贝一般都是浅拷贝，拷贝时，对象包含的子对象内容不拷贝，因此，源对象与拷贝对象会引用同一个子对象
* 深拷贝
  * 使用copy模块的`deepcopy`函数，递归拷贝对象中包含的子对象，源对象和拷贝对象所有的子对象也不相同

```python
class CPU():
    pass

class Disk():
    pass

class Computer():
    def __init__(self,cpu,disk):
        self.cpu = cpu
        self.disk = disk
        
        
#变量的赋值
cpu1 = CPU()
cpu2 = cpu1
print(cpu1)
print(cpu2)
#浅拷贝
disk = Disk()
computer = Computer(cpu1,disk)

print(disk)
import copy
computer2 = copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)

#深拷贝
computer3 = copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)

#拷贝，创建新的对象，id地址变了
```

---

在Python中，浅拷贝和深拷贝都是用来复制对象的方法，但是它们复制的方式有所不同。

浅拷贝（shallow copy）是指创建一个新的对象，但是这个对象中的元素只是原对象中元素的引用。也就是说，新对象中的元素和原对象中的元素指向的是同一块内存空间。在Python中，可以使用copy模块的copy()函数或者列表、字典等对象自带的copy()方法来进行浅拷贝。

例如：

```python
import copy

a = [1, 2, 3]
b = copy.copy(a)

print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3]

a[0] = 0

print(a)  # [0, 2, 3]
print(b)  # [1, 2, 3]
```

可以看到，对原对象a进行修改并不会影响到浅拷贝的对象b。

深拷贝（deep copy）是指创建一个新的对象，并且递归复制原对象中所有的元素，包括嵌套的对象。也就是说，新对象中的元素和原对象中的元素是完全独立的，互不影响。在Python中，可以使用copy模块的`deepcopy()`函数来进行深拷贝。

例如：

```python
import copy

a = [1, 2, [3, 4]]
b = copy.deepcopy(a)

print(a)  # [1, 2, [3, 4]]
print(b)  # [1, 2, [3, 4]]

a[2][0] = 0

print(a)  # [1, 2, [0, 4]]
print(b)  # [1, 2, [3, 4]]
```

可以看到，对原对象a进行修改并不会影响到深拷贝的对象b，并且深拷贝的对象b中的元素也是完全独立的。



---

## 模块

### 什么是模块

* 模块的英文为Modules
  * 函数与模块可以包含N多函数
* 在python中一个扩展名`.py`的文件就是一个模块
* 使用模块的好处
  * 方便其他程序和脚本的导入并使用
  * 避免函数名和变量名冲突
  * 提高代码的可维护性
  * 提高代码的可重用性

```python
def fun1():
    pass
def fun2():
    pass
class Student:
    native_place ='广东'
    def eat(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def cm(cls):
        pass
    @statiCmethod
    def sm():
        pass
    
    
    
a = 10
b = 20
print(a+b)
```

### 模块的导入

* 创建模块
  * 新建一个`.py`文件，名称尽量不要与Python自带的标准模块名称相同
* 导入模块

​		`import 模块名称 [as 别称名]`

​		`from 模块名称 import 函数/变量/类`



```python
import math
print(id(math))
print(type(math))
print(math)
print(math.pi)
print(dir(math))
print(math.pow(2,3))
print(math.ceil(9.001))	#天花板,输出10
print(math.floor(9.999))	#输出9
```

```python
from math import pi
#import math
print(pi)
print(pow(2,3))
print(math.pow(2,3))	#需要导入math
```

### 以主程序形式运行

* 在每个模块的定义中都包括一个记录模块名称的变量`__name__`,程序可以检查该变量，以确定他们在哪个模块中执行。如果一个模块不是被导入到其它程序中执行，那么它可能在解释器的顶级模块中执行。顶级模块的`__name__`变量的值为`__main__`

```python
if __name__ = '__main__':
    pass
```

### Python中的包

* 包是一个分层次的目录结构，它将一组功能相近的模块组织在一个目录下

* 作用：

  * 代码规范
  * 避免模块名称冲突

* 包与目录的区别

  * 包含`__init__.py`文件的目录称为包
  * 目录里通常不包含`__init__.py`文件

* 包的导入

  `import 包名.模块`

  **使用import方式进行导入时，只能包名或模块名**

  **使用from...import...可以导入包、模块、函数、变量**

  

  ---

  ## Python中常用的内容模块

  | 模块名称   | 说明                                             |
  | ---------- | ------------------------------------------------ |
  | `sys`      | 提供了与Python解释器和系统进行交互的函数和变量。 |
  | `os`       | 提供了访问操作系统功能的函数。                   |
  | `math`     | 提供了常用的数学函数，如sin、cos、sqrt等。       |
  | `random`   | 提供了生成随机数和随机序列的函数。               |
  | `time`     | 提供了与时间相关的函数和变量。                   |
  | `datetime` | 提供了处理日期和时间的函数和类。                 |
  | `re`       | 提供了正则表达式的支持。                         |
  | `json`     | 提供了JSON数据的编码和解码功能。                 |
  | `urllib`   | 提供了与URL相关的函数和类。                      |
  | `requests` | 提供了HTTP请求的功能。                           |

  | 模块名称   | 说明                                                       |
  | ---------- | ---------------------------------------------------------- |
  | `calendar` | 提供与日期相关的各种函数的标准库                           |
  | `decimal`  | 用于进行精确控制运算精度、有效数位和四舍五入的十进制进度   |
  | `logginng` | 提供了灵活的记录事件、错误、警告和调试信息等日志信息的功能 |

以下是Python中常用的内容模块的例子：

1. `sys`模块：

```python
import sys

# 获取命令行参数
args = sys.argv

# 获取Python解释器的版本信息
version = sys.version

# 退出Python程序
sys.exit()
```

2. `os`模块：

```python
import os

# 获取当前工作目录
cwd = os.getcwd()

# 创建目录
os.mkdir("new_folder")

# 删除文件
os.remove("file.txt")
```

3. `math`模块：

```python
import math

# 计算正弦值
sin_value = math.sin(0.5)

# 计算平方根
sqrt_value = math.sqrt(4)
```

4. `random`模块：

```python
import random

# 生成随机整数
rand_int = random.randint(1, 10)

# 生成随机浮点数
rand_float = random.uniform(0, 1)

# 生成随机字符串
rand_str = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))
```

5. `time`模块：

```python
import time

# 获取当前时间戳
timestamp = time.time()

# 格式化时间戳
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
```

6. `datetime`模块：

```python
import datetime

# 获取当前日期
today = datetime.date.today()

# 创建日期对象
date_obj = datetime.date(2021, 1, 1)
```

7. `re`模块：

```python
import re

# 匹配字符串
match = re.search(r'\d+', 'abc123def')

# 替换字符串
new_str = re.sub(r'\d+', '456', 'abc123def')
```

8. `json`模块：

```python
import json

# 将Python对象转换为JSON字符串
json_str = json.dumps({'name': 'Tom', 'age': 18})

# 将JSON字符串转换为Python对象
python_obj = json.loads('{"name": "Tom", "age": 18}')
```

9. `urllib`模块：

```python
import urllib.request

# 发送HTTP请求
response = urllib.request.urlopen('https://www.google.com')

# 读取响应内容
content = response.read().decode('utf-8')
```

10. `requests`模块：

```python
import requests

# 发送HTTP请求
response = requests.get('https://www.google.com')

# 读取响应内容
content = response.text
```



---

## 第三方模块的安装

* 第三方模块的安装

  `pip install 模块名`

* 第三方模块的应用

  `import 模块名`

