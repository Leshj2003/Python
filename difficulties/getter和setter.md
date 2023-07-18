## getter和setter

在Python中，getter和setter是用于访问和修改对象属性的方法。它们可以帮助我们控制对属性的访问和修改，以实现数据的封装和保护。

Getter方法用于获取对象的属性值，它通常以get开头，后面跟着属性的名称。例如，如果我们有一个名为age的属性，我们可以定义一个名为get_age的方法来获取它的值：

```python
class Person:
    def __init__(self, age):
        self._age = age
    
    def get_age(self):
        return self._age

person = Person(25)
print(person.get_age())  # 输出 25
```

Setter方法用于修改对象的属性值，它通常以set开头，后面跟着属性的名称。例如，如果我们有一个名为age的属性，我们可以定义一个名为set_age的方法来修改它的值：

```python
class Person:
    def __init__(self, age):
        self._age = age
    
    def set_age(self, age):
        self._age = age

person = Person(25)
person.set_age(30)
print(person.get_age())  # 输出 30
```

使用getter和setter方法可以控制对属性的访问和修改。例如，我们可以在setter方法中添加一些条件判断，以确保属性值的有效性：

```python
class Person:
    def __init__(self, age):
        self._age = age
    
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if age >= 0 and age <= 120:
            self._age = age
        else:
            print("年龄必须在0到120之间")

person = Person(25)
person.set_age(150)  # 输出 "年龄必须在0到120之间"
print(person.get_age())  # 输出 25
```

在Python中，还有一种更简洁的方式来定义属性的getter和setter方法，即使用@property装饰器和对应的setter装饰器。这样可以使得属性看起来更像是直接访问的变量，而不是方法调用。例如：

```python
class Person:
    def __init__(self, age):
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        if age >= 0 and age <= 120:
            self._age = age
        else:
            print("年龄必须在0到120之间")

person = Person(25)
person.age = 150  # 输出 "年龄必须在0到120之间"
print(person.age)  # 输出 25
```

使用@property和对应的setter装饰器可以使得代码更加简洁和易读。