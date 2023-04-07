## Day14

---

## 菲波那切数列

```python
def fib(n):
	if n==1:
        return 1;
    elif n==2:
        return 1;
    else:
		return fib(n-1)+fib(n-2)
    
#菲波那切数列第六位的数字    
print(fib(6))
print('-------------')
#输出这个数列的前六位数字
for i in range(1,7):
    print(fib(i))

```

* if 终止条件 else



---

## Bug的常见类型

* 语法错误SyntaxError

  ```python
  '''
  age = input()	#是str类型，不能比较，应该转成int()
  print(type(age))
  if age >= 18:
      print('')
      
  '''
      
  '''
  =是赋值，==是比较
  if uname == 'admin' and pwd == 'admin'
  '''
  ```

  

1、漏了末尾的冒号，如if语句，循环语句，else子句等

2、缩进错误

3、英文符号写成中文符号

4、字符串拼接时，把字符串和数字拼在一起

5、没有定义变量，如while的循环条件的变量

6、“==”比较运算符和“=”赋值运算符混用



* 索引越界问题IndexError

```python
lst = [11,22,33,44]
print(lst[4])
```

```python
lst = []
#lst.append('A','B')	#只可以添加一个元素
lst.append('A')
print(lst)
```

### 异常处理

* try-except

  ```python
  a = int(input())
  b = int(input())
  result = a/b
  print(result)
  
  #输入了str或浮点型
  
  try:
      a = int(input())
      b = int(input())
      result = a/b
      print(result)
  except ZeroDivisionError:
      print('除数不可以为零')
  ```

  * 多个except结构

    ```python
    try:
        a = int(input())
        b = int(input())
        result = a/b
        print(result)
    except ZeroDivisionError:
        print('除数不可以为零')
    except ValueError:
        print('只能输入数字')
    ```

    

* try...except..else结构

  * 如果try块中没有抛出异常，则执行else块，如果抛出异常，except块

  ```python
  try:
      a = int(input())
      b = int(input())
      result = a/b
  except BaseException as e:	#不清楚详细错误e
      print('出错了')
      print(e)
  else:
      print(result)
  ```

BaseException是Python中所有异常类的基类，继承自该类的异常都是Python中内置的标准异常的一种，包括系统错误、IO错误、类型错误等。BaseException也可以作为自定义异常类的基类，使得自定义异常类具有与Python内置异常类相同的特性和功能。



* try...except..else...finally结构



```python
try:
    a = int(input())
    b = int(input())
    result = a/b
except BaseException as e:	#不清楚详细错误e
    print('出错了')
    print(e)
else:
    print(result)
finally:
    print('finally是无论是否产生异常，总会被执行的代码')
print('程序结束')
```

在try…except…finally中，finally的作用是无论try和except中的代码是否出现异常，finally代码块总是会被执行。finally常用来进行一些清理工作，比如关闭文件、释放资源等操作，以确保程序不会因为异常而导致资源泄露的情况发生。

例如：

```python
try:
    # 执行一些可能会出现异常的代码
    print("try block")
    a = 1 / 0
except:
    # 如果出现异常，执行这里的代码
    print("except block")
finally:
    # 无论是否出现异常，这里的代码总是会被执行
    print("finally block")
```

无论try中的代码是否出现异常，finally中的代码块总是会被执行。在上面的示例中，由于try中的代码抛出了一个ZeroDivisionError异常，因此会执行except中的代码块。最后，无论是否出现异常，finally中的代码块都会被执行，输出结果为：

```python
try block
except block
finally block
```



---

## 常见异常类型

| 序号 | 异常类型          | 描述                           |
| ---- | ----------------- | ------------------------------ |
| 1    | ZeroDivisionError | 除（或取模）零（所有数据类型） |
| 2    | IndexError        | 序列中没有此索引（index）      |
| 3    | KeyError          | 映射中没有这个键               |
| 4    | NameError         | 未声明/初始化对象（没有属性）  |
| 5    | SyntaxError       | Python语法错误                 |
| 6    | ValueError        | 传入无效的参数                 |



### 扩充

| 异常名称          | 描述                                       |
| ----------------- | ------------------------------------------ |
| TypeError         | 当操作或函数应用于错误类型的对象时触发     |
| ImportError       | 当导入模块失败时触发                       |
| AttributeError    | 当尝试访问对象属性或方法不存在时触发       |
| IndentationError  | 当有缩进错误时触发                         |
| IOError           | 当操作无法执行请求的I / O操作时触发        |
| AssertionError    | 当断言失败时触发                           |
| MemoryError       | 当Python没有足够内存完成所需的操作时触发   |
| OverflowError     | 当数字超过最大限制时触发                   |
| SystemError       | 当Python运行时发生内部错误时触发           |
| KeyboardInterrupt | 当用户中断程序时（通常通过按Ctrl + C）触发 |



* traceback模块

```python
import traceback
try:
	print('---------')
    print(10/0)
except:
    traceback.print_exc()
```



---

## 面向过程—面向对象

|        | 面向过程                                                     | 面向对象                                 |
| ------ | ------------------------------------------------------------ | ---------------------------------------- |
| 区别   | 事物比较简单，可以用线性的思维解决                           | 事物比较复杂，使用简单的线性思维无法解决 |
| 共同点 | 面向过程和面向对象都是解决实际问题的一种思维方式             |                                          |
|        | 二者相辅相成，并不是对立的<br />解决复杂问题，通过面向对象方式便于我们宏观上把握事物之间的复杂关系、方便我们分析整个系统；具体到微观操作，任然使用面向过程方式来处理 ||



---

## 对象与类

* 数据类型

  * 不同的数据类型属于不同的类

  * 使用内置函数查看数据类型

    ```python
    print(type(100))
    ```

    

* 对象

  * 100是int类之下包含的相似的不同个例，这个个例专业术语为实例或对象

**python中一切皆对象**

---

## 类的创建

* 创建类的语法

  ```python
  class Student:
      pass
  ```

  

* 类的组成

  * 类属性
  * 实例方法
  * 静态方法
  * 类方法

```python
class Student:	#Student为类名，由一个或多个单词组成，每个单词首字母必须大写，其余小写
    native_pace = '广东'	#类属性
    def __init__(self,name,age):
        self.name=name	#self.name称为实体属性，进行了一个赋值的操作，将局部变量的name的值赋给实体属性
        self.age=age
    #实例方法
    def eat(self):	#self可以换成其他的，通常是self
        print('学生在吃饭...')
      
    #静态方法
    @staticmethod
    def method():
        print('我使用staticmethod进行修饰，所以我是静态方法')

        
    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法，使用了classmethod进行修饰')
        
def drink():
    print('喝水')
'''
print(id(Student))
print(type(Student))	#类对象
print(Student)
'''
```

def()**在类之外定义的称为函数，类之内的称为方法**



---

## 对象的创建

* 对象的创建又称为类的实例化

* 语法：

  实例名 = 类名()

* 例子：

  stu = Student()

* 意义：有了实例，就可以调用类的内容

```python
class Student:	#Student为类名，由一个或多个单词组成，每个单词首字母必须大写，其余小写
    native_pace = '广东'	#类属性
    def __init__(self,name,age):
        self.name=name	#self.name称为实体属性，进行了一个赋值的操作，将局部变量的name的值赋给实体属性
        self.age=age
    #实例方法
    def eat(self):	#self可以换成其他的，通常是self
        print('学生在吃饭...')
      
    #静态方法
    @staticmethod
    def method():
        print('我使用staticmethod进行修饰，所以我是静态方法')

        
    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法，使用了classmethod进行修饰')
        
def drink():
    print('喝水')
    
    
    
# 创建Student类的对象
stu1 = Student('张三',20)
'''
print(id(stu1))
print(type(stu1))
print(stu1)
print('-------------------')
print(id(Student))
print(type(Student))
print(Student)
'''

stu1.eat()	#对象名.方法名()
print(stu1.name)
print(stu1.age)

print('--------------------')
Student.eat(stu1)	#和stu1.eat()一样，功能相同,类名.方法名()
```

