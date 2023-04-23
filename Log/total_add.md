### 类之间的关系

简单的说，类和类之间的关系有三种：is-a、has-a和use-a关系。

- is-a关系也叫继承或泛化，比如学生和人的关系、手机和电子产品的关系都属于继承关系。
- has-a关系通常称之为关联，比如部门和员工的关系，汽车和引擎的关系都属于关联关系；关联关系如果是整体和部分的关联，那么我们称之为聚合关系；如果整体进一步负责了部分的生命周期（整体和部分是不可分割的，同时同在也同时消亡），那么这种就是最强的关联关系，我们称之为合成关系。
- use-a关系通常称之为依赖，比如司机有一个驾驶的行为（方法），其中（的参数）使用到了汽车，那么司机和汽车的关系就是依赖关系。



---

## Python 中实现抽象基类

Python 中实现抽象基类（Abstract Base Class）一般需要用到 `ABCMeta` 和 `abstractmethod` 两个元素。ABC 即` Abstract Base Class`，它是定义抽象类的 Python 模块，用于检查继承自某个基类的子类是否按照约定完全地实现了所有抽象方法等特性。

以下是一个用 Python 实现抽象基类的例子：

```python
from abc import ABCMeta, abstractmethod

class MyABC(metaclass=ABCMeta):

    @abstractmethod
    def do_something(self):
        pass
    
    @abstractmethod
    def do_another_thing(self):
        pass
    
    def common_method(self):
        # 这是一个普通方法
        print('This is a common method in the base class.')

class MyClass(MyABC):

    def do_something(self):
        # 必须实现父类中声明的所有抽象方法
        print('Doing something...')

    def do_another_thing(self):
        # 必须实现父类中声明的所有抽象方法
        print('Doing another thing...')
        
obj = MyClass()
obj.do_something()  # Doing something...
obj.do_another_thing()  # Doing another thing...
obj.common_method()  # This is a common method in the base class.
```

在这个例子中，我们首先定义了一个抽象基类 `MyABC`，并声明了两个抽象方法 `do_something` 和 `do_another_thing`。这两个方法都没有实际的实现，只是用 `@abstractmethod` 标记了其为抽象方法。`MyABC` 继承于 `ABCMeta` 类，这样可以在子类继承并实现所有抽象方法后，检查是否缺少了一些必须的方法。

接着我们定义了一个 `MyClass` 类，该类继承了`MyABC`。注意，在 `MyClass` 中必须重写 `MyABC` 所有的抽象方法，否则会在运行时引发异常。同时，`MyClass` 实现了一个普通方法 common_method，这个方法不是抽象方法，因此可以被直接子类继承并使用。

最后我们创建了 `MyClass` 的实例对象 obj，并使用其中的方法。在运行过程中，如果忘记实现任何一个抽象方法，Python 解释器就会抛出 `TypeError` 异常。

---

##  `__str__`特殊方法

`__str__`是一个Python中的特殊方法，用于返回对象的字符串表示形式。当使用print函数打印一个对象时，实际上是调用该对象的`__str__`方法来获取其字符串表示形式。

`__str__`方法应该返回一个字符串，描述对象的内容和状态。这个字符串可以是任何格式的，可以包含对象的属性、方法、状态等信息。

例如，我们定义一个Person类：

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."
```

当我们打印一个Person对象时，会调用该对象的`__str__`方法来获取其字符串表示形式：

```python
person = Person("Alice", 25)
print(person)  # 输出：Alice is 25 years old.
```

`__str__`方法在调试时也很有用，因为它可以帮助我们快速了解对象的属性和状态。

---

## GUI应用开发步骤

1. 导入`tkinter`模块中我们需要的东西。
2. 创建一个顶层窗口对象并用它来承载整个GUI应用。
3. 在顶层窗口对象上添加GUI组件。
4. 通过代码将这些GUI组件的功能组织起来。
5. 进入主事件循环(main loop)。

```python
import  tkinter
windows = tkinter.Tk()
windows.title('First windows')
windows.geometry('200x200')
windows.mainloop()
```



```Python
import tkinter
import tkinter.messagebox


def main():
    flag = True

    # 修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!')\
            if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):	#用户点击返回True/False
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry('240x160')
    # 设置窗口标题
    top.title('小游戏')
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # 开启主事件循环
    tkinter.mainloop()


if __name__ == '__main__':
    main()
```

### Tk为控件的摆放提供了三种布局管理器

1. Pack布局管理器：将控件按照添加顺序自动排列，可以设置控件的填充方式和位置。

2. Grid布局管理器：将控件放置在网格中，可以设置控件所占的行数和列数，以及控件的对齐方式和间距。

3. Place布局管理器：通过指定控件的绝对位置和大小来进行布局，适用于需要精确控制控件位置和大小的场合。

---

## `pygame`

`pygame` 是一个基于 Python 的游戏开发库，它提供了许多在开发 2D 游戏时所需的功能，并且易于使用。`pygame` 包含许多模块，例如绘制、输入处理、碰撞检测以及声音等等。



### 开发步骤

下面是一个游戏开发时使用 `pygame` 的基本步骤：

1. 导入 `pygame` 库

```python
import pygame
```

​	2.初始化 `Pygame`

```python
pygame.init()
```

​	3.创建窗口

```python
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
```

​	4.设置窗口标题

```python
pygame.display.set_caption('My Game')
```

​	5.加载资源，如图片、声音或字体文件等

```python
image = pygame.image.load('example.png')
sound = pygame.mixer.Sound('example.wav')
font = pygame.font.Font(None, 40)
```

6. 在屏幕上绘制图形和文本以及处理输入事件

```python
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 绘制背景色
    screen.fill((255, 255, 255))

    # 绘制图形
    screen.blit(image, (0, 0))

    # 绘制文本
    text = font.render('Hello, World!', True, (0, 0, 255))
    screen.blit(text, (200, 200))

    # 更新界面
    pygame.display.flip()
```

7. 运行游戏主循环

```python
if __name__ == '__main__':
    main()
```

需要注意的是，具体实现方式可能因游戏类型和个人开发风格而有所不同，这里只提供了一种基本的框架。通过不断练习和阅读 `pygame` 相关文档和示例代码，可以逐渐掌握 `Pygame` 的使用方法。

### 简单例子

下面是 `pygame` 给出的几个简单例子：

1. 显示一个基本窗口

```python
import pygame, sys
from pygame.locals import *

pygame.init()

# 设置窗口大小
WINDOW_SIZE = (400, 300)

# 创建主窗口
win = pygame.display.set_mode(WINDOW_SIZE)

# 设置窗口标题
pygame.display.set_caption('pygame demo')

# 事件循环
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # 填充背景色
    win.fill((255, 255, 255))

    # 更新屏幕显示
    pygame.display.update()
```

1. 移动图形

```python
import pygame, sys
from pygame.locals import *

pygame.init()

# 设置窗口大小
WINDOW_SIZE = (400, 300)

# 创建主窗口
win = pygame.display.set_mode(WINDOW_SIZE)

# 设置窗口标题
pygame.display.set_caption('pygame demo')

# 绘制图形
rect = pygame.Rect(50, 50, 100, 100)
color = (0, 255, 0)

# 事件循环
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # 填充背景色
    win.fill((255, 255, 255))

    # 绘制图形
    pygame.draw.rect(win, color, rect)

    # 检查用户按键
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        rect.move_ip(-5, 0)
    elif keys[K_RIGHT]:
        rect.move_ip(5, 0)
    elif keys[K_UP]:
        rect.move_ip(0, -5)
    elif keys[K_DOWN]:
        rect.move_ip(0, 5)

    # 更新屏幕显示
    pygame.display.update()
```

1. 声音播放

```python
import pygame, sys
from pygame.locals import *

pygame.init()

# 设置窗口大小
WINDOW_SIZE = (400, 300)

# 创建主窗口
win = pygame.display.set_mode(WINDOW_SIZE)

# 设置窗口标题
pygame.display.set_caption('pygame demo')

# 加载音频文件
sound = pygame.mixer.Sound('example.wav')

# 事件循环
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # 检查空格键
        if event.type == KEYDOWN and event.key == K_SPACE:
            sound.play()

    # 填充背景色
    win.fill((255, 255, 255))

    # 更新屏幕显示
    pygame.display.update()
```

### 大球吃小球



