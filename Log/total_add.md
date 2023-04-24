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

#### 制作游戏窗口

```python
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('大球吃小球')
    runnning = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QIUT:
                running = False
                
if __name__ == '__main__':
    main()
```

#### 在窗口中绘图

```python
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('大球吃小球')
    
    # 设置背景颜色
    screen.fill((242,242,242))
    # 绘制一个圆，参数分别为，屏幕，颜色，圆心位置，半径，0表示填充圆
    pygame.draw.circle(screen,(225,0,0),(100,100),30,0)
    # 刷新当前窗口
    pygame.display.flip()
    
    runnning = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QIUT:
                running = False
                
if __name__ == '__main__':
    main()
```

#### 加载图像

```python
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('大球吃小球')
    screen.fill((255,255,255))
    
    # 通过指定的文件名加载图像
    ball_image = pygame.load(./res/ball.png)
    # 刷新当前窗口
    screen.blit(ball_image,(50,50))
    
    pygame.display.flip()
    runnning = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QIUT:
                running = False
                
if __name__ == '__main__':
    main()
```

#### 实现动画效果

```python
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('大球吃小球')
    
    # 定义变量来表示小球在屏幕上的位置
    x,y = 50,50
    
    runnning = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QIUT:
                running = False
        screen.fill((255,255,255))
        pygame.draw.circle(screen,(255,0,0),(x,y),30,0)
        pygame.display.flip()
        # 每隔50ms就改变小球的位置在刷新窗口
        pygame.time.deplay(50)
        x,y = x+5,y+5
                
if __name__ == '__main__':
    main()
```

#### 碰撞检测

```python
from enum import Enum,unique
from math import sqrt
from random import randint

import pygame

@unique
class Color(Enum):
    """颜色"""
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)
    
    @staticmethod
    def random_color():
        '''获取随机颜色'''
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        return (r,g,b)
    
class Ball(object):
    '''球'''
    def __init__(self,x,y,radius,sx,sy,color = Color.RED):
        '''初始化方法'''
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True
        
    def move(self,screen):
        '''移动'''
        self.x += self.sx
        self.y += self.sy
        
```

#### 事件处理

```python
```



### `pygame.draw()`

`pygame.draw()`是`Pygame`中用于绘制各种形状的函数，它包含了许多可选参数，下面是一些常用参数的说明：

- `Surface`：要绘制形状的目标Surface。
- `color`：表示颜色的元组（R，G，B）或（R，G，B，A），其中R、G、B和A的值均为0-255。
- `width`：线条的宽度，默认值为1。
- `pointlist`：表示线条或多边形各个点坐标的列表。
- `radius`：圆的半径。
- `rect`：表示矩形左上角坐标和宽高的元组或`Rect`对象。
- `start_angle`：起始角度（用弧度表示），从3点钟方向开始逆时针计算。
- `end_angle`：结束角度（用弧度表示）。

下面是一个简单的例子，使用pygame.draw()绘制一个蓝色圆形和一个红色矩形：

```python
import pygame

pygame.init()

# 设置屏幕大小和标题
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Draw Shapes')

# 绘制蓝色圆形和红色矩形
pygame.draw.circle(screen, (0, 0, 255), (200, 200), 50)
pygame.draw.rect(screen, (255, 0, 0), (150, 150, 100, 100))

# 刷新屏幕
pygame.display.update()

# 事件循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
```

运行以上代码，将会显示一个蓝色圆形和一个红色矩形。



在 `Pygame` 中，`pygame.draw` 模块提供了多种绘制图形和几何形状的函数。以下是一些例子：

1. 绘制线段：使用 `pygame.draw.line` 函数可以绘制直线，需要提供起点和终点坐标，线条宽度和颜色等参数。

```python
import pygame

# 初始化 Pygame
pygame.init()

# 设置窗口尺寸
screen = pygame.display.set_mode((400, 300))

# 绘制红色直线
pygame.draw.line(screen, (255, 0, 0), (50, 50), (200, 100), 5)

# 刷新屏幕
pygame.display.flip()

# 等待退出
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
```

2. 绘制矩形：使用 `pygame.draw.rect` 函数可以绘制矩形，需要提供矩形左上角坐标，矩形宽度和高度，以及颜色等参数。

```python
import pygame

# 初始化 Pygame
pygame.init()

# 设置窗口尺寸
screen = pygame.display.set_mode((400, 300))

# 绘制蓝色矩形
pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(50, 50, 100, 80), 3)

# 刷新屏幕
pygame.display.flip()

# 等待退出
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
```

3. 绘制圆形：使用 `pygame.draw.circle` 函数可以绘制圆形，需要提供圆心坐标，半径，以及颜色等参数。

```python
import pygame

# 初始化 Pygame
pygame.init()

# 设置窗口尺寸
screen = pygame.display.set_mode((400, 300))

# 绘制黄色圆形
pygame.draw.circle(screen, (255, 255, 0), (200, 150), 50, 2)

# 刷新屏幕
pygame.display.flip()

# 等待退出
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
```

4. 绘制多边形：使用 `pygame.draw.polygon` 函数可以绘制多边形，需要提供多边形的顶点坐标，以及颜色等参数。

```python
import pygame

# 初始化 Pygame
pygame.init()

# 设置窗口尺寸
screen = pygame.display.set_mode((400, 300))

# 绘制绿色三角形
pygame.draw.polygon(screen, (0, 255, 0), [(50, 50), (200, 50), (125, 150)], 2)

# 刷新屏幕
pygame.display.flip()

# 等待退出
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
```

### `pygame.image()`

`pygame.image`是``Pygame`中用于加载、创建和处理图像的模块。它提供了一些函数，可以加载各种不同格式的图像文件，例如PNG、JPG和BMP等。此外，它还提供了一些用于对图像进行转换、缩放和剪切的函数，以及一些用于绘制图像的函数。

以下是一些简单的例子：

1. 加载一张图片并在窗口中显示它

```python
import pygame

# 初始化pygame
pygame.init()

# 创建一个窗口
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)

# 加载一张图片
image = pygame.image.load('example.png')

# 在窗口中显示图片
screen.blit(image, (0, 0))

# 更新窗口
pygame.display.update()

# 等待用户关闭窗口
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
```

2. 将一张图片缩放并显示在窗口中

```python
import pygame

# 初始化pygame
pygame.init()

# 创建一个窗口
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)

# 加载一张图片并缩放
image = pygame.image.load('example.png')
image = pygame.transform.scale(image, (320, 240))

# 在窗口中显示图片
screen.blit(image, (0, 0))

# 更新窗口
pygame.display.update()

# 等待用户关闭窗口
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
```

3. 将一张图片剪切并显示在窗口中

```python
import pygame

# 初始化pygame
pygame.init()

# 创建一个窗口
window_size = (640, 480)
screen = pygame.display.set_mode(window_size)

# 加载一张图片并剪切
image = pygame.image.load('example.png')
rect = pygame.Rect(0, 0, 160, 120)
image = image.subsurface(rect)

# 在窗口中显示图片
screen.blit(image, (0, 0))

# 更新窗口
pygame.display.update()

# 等待用户关闭窗口
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
```

以上示例展示了如何加载、缩放、剪切并在窗口中显示一张图片。在实际应用中，还可以使用`pygame.image`模块提供的其他函数对图像进行更复杂的处理，例如旋转、翻转、颜色调整等。

###  `pygame`实现动画

`Pygame`实现动画的原理通常是通过循环在屏幕上不断更新图像，使其看起来像是动起来的。这里简单介绍一下实现动画的一般步骤：

1. 初始化`Pygame`：在程序开始时，需要初始化`Pygame`，以便可以创建窗口和其他对象。可以使用`pygame.init()`函数进行初始化。

2. 创建窗口：创建一个窗口并设置其尺寸。可以使用`pygame.display.set_mode()`函数创建窗口。

3. 加载图像：使用`pygame.image.load()`函数加载图像。

4. 绘制图像：使用`pygame.Surface.blit()`函数将图像绘制在屏幕上。

5. 刷新屏幕：在绘制完图像后，需要使用`pygame.display.flip()`函数更新屏幕。

6. 循环更新图像：在主循环中使用`pygame.time.Clock()`函数控制游戏帧率，使用`pygame.event.get()`函数获取事件，以便在窗口中对输入作出响应。同时，在每个循环迭代中更新图像。

下面是一个简单的`Pygame`动画示例，其中创建了一个窗口，加载了一个图像，然后在窗口中循环显示图像，使其看起来像是动起来的：

```python
import pygame

pygame.init()

# 创建窗口
screen = pygame.display.set_mode((400, 400))

# 加载图像
image = pygame.image.load("image.png")

# 设置图像位置
x, y = 0, 0

# 主循环
running = True
while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 绘制图像
    screen.blit(image, (x, y))

    # 更新屏幕
    pygame.display.flip()

    # 增加位置
    x += 1
    y += 1

    # 控制帧率
    pygame.time.Clock().tick(60)

# 关闭Pygame
pygame.quit()
```

在这个示例中，我们加载了一个名为“image.png”的图像，并将其绘制在窗口中。我们使用`x`和`y`变量来控制图像的位置，并在每次循环迭代中增加它们的值，以便使图像在窗口中移动。我们还使用`pygame.time.Clock().tick(60)`函数来控制游戏帧率，以确保动画不会过快或过慢。最后，在关闭窗口之前，我们使用`pygame.quit()`函数关闭`Pygame`。

### `pygame.sprite()`

`pygame.sprite` 是一个用于管理精灵（Sprites）的模块。在游戏开发中，精灵通常指的是游戏中可以移动、可以与其他物体交互的游戏对象。`pygame.sprite` 提供了一个基础类 `Sprite`，并支持精灵组（Sprite Groups），可以将多个精灵添加到精灵组中进行管理和操作。精灵组提供了很多有用的方法和属性，例如精灵碰撞检测等。

下面是一个简单的示例，展示了如何使用 `pygame.sprite` 创建和管理精灵：

```python
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += 5

pygame.init()

screen = pygame.display.set_mode((800, 600))

player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    all_sprites.update()

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)
```

在这个示例中，我们创建了一个 `Player` 类，继承自 `pygame.sprite.Sprite`。在 `__init__` 方法中，我们创建了一个白色的矩形作为玩家精灵的图像，并将其添加到了精灵的矩形中。在 `update` 方法中，我们每次更新玩家精灵的位置。在主循环中，我们将玩家精灵添加到精灵组中，并在每一帧中更新和绘制所有精灵。这个示例中玩家精灵每次更新时会向右移动。

`pygame.sprite` 提供了很多有用的方法和属性，例如 `collide_rect`、`collide_mask` 等，可以用于检测精灵之间的碰撞等操作。在实际的游戏开发中，我们通常会继承自 `pygame.sprite.Sprite` 创建自己的精灵类，并根据游戏需求添加自定义的属性和方法。
