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
        if self.x - self.radius <= 0 or self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or self.y + self.radius >= screen.get_height():
            self.sy = -self.sy
            
    def eat(self,other):
        if self.alive and other.alive and self != orther:
            dx,dy = self.x - other.x,self.y-other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)
                
                
    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius,0)
```

* move方法

这段代码是一个小球类中的移动方法，用于控制小球在屏幕上移动。

首先，球的位置根据球的速度（`self.sx`和`self.sy`）进行更新，也就是小球向前移动。

然后，通过判断小球的位置是否超出屏幕边界来控制小球的反弹。具体来说，如果小球的左边缘（`self.x - self.radius`）触碰到了屏幕左边缘（0），或者小球的右边缘（`self.x + self.radius`）触碰到了屏幕右边缘（`screen.get_width()`），则小球在水平方向上的速度要反向（`self.sx = -self.sx`）。

同样地，如果小球的上边缘（self.y - self.radius）触碰到了屏幕上边缘（0），或者小球的下边缘（self.y + self.radius）触碰到了屏幕下边缘（screen.get_height()），则小球在竖直方向上的速度要反向（self.sy = -self.sy）。

这样，小球就能在屏幕上自由运动，并且在碰到边缘时能够反弹。

* eat方法

这段代码实现了球类之间的碰撞检测和吃掉其他球的操作。

首先判断两个球是否都存活且不是同一个球，然后计算两球中心点之间的距离，如果距离小于两球半径之和并且当前球的半径大于被吃掉的球的半径，就将被吃掉的球的状态设置为死亡状态，并将当前球的半径增加一个比例因子。

这里用到了球体积和半径的关系：两个球体积之和等于它们的半径的立方和，即$V_1+V_2 = \frac{4}{3} \pi (r_1^3+r_2^3)$，将此式变形可得$\frac{r_1^3}{r_2^3}=\frac{V_1}{V_2}$。由于被吃掉的球的体积是当前球体积的$14.6\%$，所以$\frac{r_1^3}{r_2^3}=\frac{V_1}{0.146V_1}=6.8493$，因此有$r_1=1.5487r_2$，即当前球的半径增加了被吃掉的球半径的$54.87\%$。

#### 事件处理

```python
def main():
    # 定义用来装所有球的容器
    balls = []
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # 处理鼠标事件的代码
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 获得点击鼠标的位置
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                # 在点击鼠标的位置创建一个球(大小、速度和颜色随机)
                ball = Ball(x, y, radius, sx, sy, color)
                # 将球添加到列表容器中
                balls.append(ball)
        screen.fill((255, 255, 255))
        # 取出容器中的球 如果没被吃掉就绘制 被吃掉了就移除
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()
        # 每隔50毫秒就改变球的位置再刷新窗口
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            # 检查球有没有吃到其他的球
            for other in balls:
                ball.eat(other)


if __name__ == '__main__':
    main()
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

### `event.type`

在 `Pygame`  中，事件(Event) 是指由用户或操作系统引起的可感知的操作，例如键盘按键按下或鼠标移动等。当 `Pygame`  接收到这些事件时，它们被封装成一些特定类型的事件(Event)。在处理 `Pygame` 事件时，我们通常使用 `pygame.event.get()` 来获取当前所有的事件(Event)，然后使用循环遍历每一个事件(Event)并对其进行处理。

在 `Pygame`  中，每个事件(Event)都有一个 `type` 属性，该属性指示事件(Event)的类型。`type` 可以是预定义的常量，例如 `pygame.QUIT` 表示用户请求关闭 `Pygame`  程序的窗口，或者是用户自定义的事件(Event)类型。根据事件(Event)的类型，我们可以进行不同的操作来处理它们。

以下是一些常见的`Pygame`  事件类型：

- `pygame.QUIT`：用户请求关闭 `Pygame`  程序的窗口。
- `pygame.KEYDOWN`：键盘按键按下事件。
- `pygame.KEYUP`：键盘按键释放事件。
- `pygame.MOUSEBUTTONDOWN`：鼠标按键按下事件。
- `pygame.MOUSEBUTTONUP`：鼠标按键释放事件。
- `pygame.MOUSEMOTION`：鼠标移动事件。

除了上述常见的事件类型，`Pygame` 还支持用户自定义事件(Event)类型，使用方式与预定义事件(Event)类型相同。

### `event.pos`

在 `Pygame` 中，事件对象（`event`）代表着用户执行的某个操作，例如按下键盘、移动鼠标等。当`Pygame` 接收到一个事件后，会在事件对象中存储该事件的各种信息，其中 `event.pos` 表示该事件发生的位置。

具体来说，`event.pos` 是一个包含两个整数的元组，表示事件发生的坐标（x，y）。通常情况下，该坐标指的是相对于 `Pygame` 窗口左上角的位置，单位是像素。因此，当我们想要响应鼠标点击等事件时，可以使用 `event.pos` 来获取鼠标点击的位置。

例如，以下代码片段可以在 `Pygame` 窗口中显示鼠标点击的位置：

```python
import pygame

pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            print('Clicked at', event.pos)

    pygame.display.flip()
```

在上述代码中，我们使用 `Pygame`中的 `MOUSEBUTTONUP` 事件来响应鼠标点击事件，并通过 `event.pos` 获取鼠标点击的位置。

---

## 读取JSON文件

* 把一个列表或一个字典中的数据保存到文件中

```json
{
    "name" : "青梦",
    "age" : 20,
    "qq" : 10086
    "friends" : ["及言","雪莉"],
	"cars" : [
        {"brand": "BYD", "max_speed": 180},
        {"brand": "Audi", "max_speed": 280},
        {"brand": "Benz", "max_speed": 320},
    ]
}
```

* JSON和字典的区别

| JSON                | Python       |
| ------------------- | ------------ |
| object              | dict         |
| array               | list         |
| string              | str          |
| number (int / real) | int / float  |
| true / false        | True / False |
| null                | None         |

| Python                                 | JSON         |
| -------------------------------------- | ------------ |
| dict                                   | object       |
| list, tuple                            | array        |
| str                                    | string       |
| int, float, int- & float-derived Enums | number       |
| True / False                           | true / false |
| None                                   | null         |

* 示例

```python
import json

def main():
    mydict = {
    "name" : "青梦",
    "age" : 20,
    "qq" : 10086
    "friends" : ["及言","雪莉"],
	"cars" : [
        {"brand": "BYD", "max_speed": 180},
        {"brand": "Audi", "max_speed": 280},
        {"brand": "Benz", "max_speed": 320},
    	]
	}
    try:
        with open('data.json','w',encoding='utf-8') as fs:
            json.dump(mydict,fs)
        except IOError as e:
            print(e)
        print('保存数据成功！')
        
        
if __name__ == '__main__':
    main()
    
```

### json模块常用函数

Python的`json`模块提供了许多用于处理JSON数据的函数。下面是一些常用函数及其例子：

1. `json.loads()`：将JSON格式的字符串转换为Python对象。
```python
import json

json_string = '{"name": "Alice", "age": 25, "is_student": true}'
python_object = json.loads(json_string)
print(python_object)
# 输出：{'name': 'Alice', 'age': 25, 'is_student': True}
```

2. `json.dumps()`：将Python对象转换为JSON格式的字符串。
```python
import json

python_object = {'name': 'Alice', 'age': 25, 'is_student': True}
json_string = json.dumps(python_object)
print(json_string)
# 输出：'{"name": "Alice", "age": 25, "is_student": true}'
```

3. `json.load()`：从文件中读取JSON数据并将其转换为Python对象。
```python
import json

with open('data.json', 'r') as f:
    python_object = json.load(f)
print(python_object)
```

4. `json.dump()`：将Python对象转换为JSON格式并将其写入文件。
```python
import json

python_object = {'name': 'Alice', 'age': 25, 'is_student': True}
with open('data.json', 'w') as f:
    json.dump(python_object, f)
```

5. `json.JSONEncoder`和`json.JSONDecoder`：使用自定义的编码器和解码器来转换数据。
```python
import json

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {'name': obj.name, 'age': obj.age}
        return json.JSONEncoder.default(self, obj)

class PersonDecoder(json.JSONDecoder):
    def decode(self, s):
        obj = super().decode(s)
        return Person(obj['name'], obj['age'])

person = Person('Alice', 25)
json_string = json.dumps(person, cls=PersonEncoder)
print(json_string)
# 输出：'{"name": "Alice", "age": 25}'

person2 = json.loads(json_string, cls=PersonDecoder)
print(person2.name, person2.age)
# 输出：Alice 25
```

## Python实现序列化和反序列化

在 Python 中实现序列化和反序列化的方法很多，最常用的是使用 `pickle` 和 `json` 库。

`pickle` 库可以将 Python 对象序列化为字节流，也可以将字节流反序列化为 Python 对象。它支持大多数 Python 内置对象类型，包括列表、元组、字典、集合等等。以下是一个序列化和反序列化 Python 列表的例子：

```python
import pickle

mylist = [1, 2, 3, 4]
# 序列化
with open('data.pkl', 'wb') as f:
    pickle.dump(mylist, f)
# 反序列化
with open('data.pkl', 'rb') as f:
    loaded_list = pickle.load(f)
print(loaded_list)
```

`json` 库则可以将 Python 对象转换为 JSON 格式的字符串，也可以将 JSON 格式的字符串转换为 Python 对象。它支持的 Python 对象类型相对较少，但可以在 Python 和其他语言之间传递数据。以下是一个将 Python 字典转换为 JSON 格式字符串的例子：

```python
import json

mydict = {"name": "John", "age": 30, "city": "New York"}
# 序列化
json_string = json.dumps(mydict)
print(json_string)
# 反序列化
loaded_dict = json.loads(json_string)
print(loaded_dict)
```

需要注意的是，`pickle` 序列化的结果只能在 Python 中使用，而 `json` 序列化的结果则可以在多种语言之间共享。在使用 `pickle` 序列化时要谨慎，避免安全风险。

### shelve模块

`shelve` 模块是 Python 内置的对象持久化模块，它实现了对象的序列化和反序列化，可将 Python 中的任意对象存储到磁盘上，然后再从磁盘上加载并还原成原始对象。使用 `shelve` 模块可以方便地将 Python 中的对象持久化，而无需手动实现序列化和反序列化的过程。

`shelve` 模块的主要特点如下：

- 可以将任意类型的 Python 对象序列化并保存到磁盘上。
- 支持基本的 CRUD 操作：创建、读取、更新、删除。
- 使用字典样式的 API。
- 可以对同一个文件进行多次操作，即不必一次性将所有数据都读入内存，这对于大型数据集非常有用。

`shelve` 模块使用起来非常简单，以下是一个示例：

```python
import shelve

# 创建一个 shelve 文件并写入数据
with shelve.open('mydata') as db:
    db['spam'] = {'name': 'spam', 'age': 3, 'color': 'white'}
    db['eggs'] = {'name': 'eggs', 'age': 2, 'color': 'brown'}

# 从 shelve 文件中读取数据
with shelve.open('mydata') as db:
    print(db['spam'])  # {'name': 'spam', 'age': 3, 'color': 'white'}
    print(db['eggs'])  # {'name': 'eggs', 'age': 2, 'color': 'brown'}
```

在上面的示例中，我们首先使用 `with` 语句打开一个 shelve 文件 `mydata`，然后向其中写入两个字典数据，接着再次打开文件并读取数据。在 shelve 中，数据是以键值对的形式存储的，因此我们可以通过键来读取相应的值。需要注意的是，在读取数据时，如果使用的是不存在的键，`shelve` 会抛出 `KeyError` 异常。

---

## 正则表达式-re模块

Python中的re模块是用于正则表达式操作的模块。正则表达式是一种强大的字符串处理工具，可以用于字符串的匹配、搜索、替换等操作。re模块提供了很多方法来进行正则表达式的操作，包括模式匹配、查找、替换等功能。

下面是一些常用的re模块方法：

1. match()方法：尝试从字符串的起始位置匹配一个模式，如果匹配成功返回一个匹配对象，否则返回None。

示例代码：

```python
import re

pattern = 'hello'
string = 'hello world'
result = re.match(pattern, string)
if result:
    print(result.group())  # 输出匹配结果'hello'
else:
    print('匹配失败')
```

2. search()方法：在字符串中搜索匹配给定的正则表达式的第一个位置，并返回相应的匹配对象。如果没有匹配成功，则返回None。

示例代码：

```python
import re

pattern = 'world'
string = 'hello world'
result = re.search(pattern, string)
if result:
    print(result.group())  # 输出匹配结果'world'
else:
    print('匹配失败')
```

3. findall()方法：在字符串中查找所有匹配正则表达式的字符串，并以列表形式返回。

示例代码：

```python
import re

pattern = '\d+'
string = '1a2b3c4d5e'
result = re.findall(pattern, string)
print(result)  # 输出匹配结果['1', '2', '3', '4', '5']
```

4. sub()方法：使用给定的替换字符串替换匹配正则表达式的字符串，并返回替换后的字符串。

示例代码：

```python
import re

pattern = 'world'
string = 'hello world'
result = re.sub(pattern, 'Python', string)
print(result)  # 输出替换结果'hello Python'
```

5. split()方法：使用正则表达式指定的模式分隔字符串，并返回分隔后的子字符串列表。

示例代码：

```python
import re

pattern = '[,;.]'
string = 'a,b;c.d'
result = re.split(pattern, string)
print(result)  # 输出分隔后的子字符串列表['a', 'b', 'c', 'd']
```

除了以上方法外，re模块还提供了很多其他的方法和属性，可以根据具体需求进行选择和使用。在使用re模块时，要注意正则表达式的语法和规则，避免出现不必要的错误。

---

## 正则表达式基本符号

| 符号         | 解释                             | 示例             | 说明                                                         |
| ------------ | -------------------------------- | ---------------- | ------------------------------------------------------------ |
| .            | 匹配任意字符                     | b.t              | 可以匹配bat / but / b#t / b1t等                              |
| \w           | 匹配字母/数字/下划线             | b\wt             | 可以匹配bat / b1t / b_t等 但不能匹配b#t                      |
| \s           | 匹配空白字符（包括\r、\n、\t等） | love\syou        | 可以匹配love you                                             |
| \d           | 匹配数字                         | \d\d             | 可以匹配01 / 23 / 99等                                       |
| \b           | 匹配单词的边界                   | \bThe\b          |                                                              |
| ^            | 匹配字符串的开始                 | ^The             | 可以匹配The开头的字符串                                      |
| $            | 匹配字符串的结束                 | .exe$            | 可以匹配.exe结尾的字符串                                     |
| \W           | 匹配非字母/数字/下划线           | b\Wt             | 可以匹配b#t / b@t等 但不能匹配but / b1t / b_t等              |
| \S           | 匹配非空白字符                   | love\Syou        | 可以匹配love#you等 但不能匹配love you                        |
| \D           | 匹配非数字                       | \d\D             | 可以匹配9a / 3# / 0F等                                       |
| \B           | 匹配非单词边界                   | \Bio\B           |                                                              |
| []           | 匹配来自字符集的任意单一字符     | [aeiou]          | 可以匹配任一元音字母字符                                     |
| [^]          | 匹配不在字符集中的任意单一字符   | [^aeiou]         | 可以匹配任一非元音字母字符                                   |
| *            | 匹配0次或多次                    | \w*              |                                                              |
| +            | 匹配1次或多次                    | \w+              |                                                              |
| ?            | 匹配0次或1次                     | \w?              |                                                              |
| {N}          | 匹配N次                          | \w{3}            |                                                              |
| {M,}         | 匹配至少M次                      | \w{3,}           |                                                              |
| {M,N}        | 匹配至少M次至多N次               | \w{3,6}          |                                                              |
| \|           | 分支                             | foo\|bar         | 可以匹配foo或者bar                                           |
| (?#)         | 注释                             |                  |                                                              |
| (exp)        | 匹配exp并捕获到自动命名的组中    |                  |                                                              |
| (?<name>exp) | 匹配exp并捕获到名为name的组中    |                  |                                                              |
| (?:exp)      | 匹配exp但是不捕获匹配的文本      |                  |                                                              |
| (?=exp)      | 匹配exp前面的位置                | \b\w+(?=ing)     | 可以匹配I'm dancing中的danc                                  |
| (?<=exp)     | 匹配exp后面的位置                | (?<=\bdanc)\w+\b | 可以匹配I love dancing and reading中的第一个ing              |
| (?!exp)      | 匹配后面不是exp的位置            |                  |                                                              |
| (?<!exp)     | 匹配前面不是exp的位置            |                  |                                                              |
| *?           | 重复任意次，但尽可能少重复       | a.*b a.*?b       | 将正则表达式应用于aabab，前者会匹配整个字符串aabab，后者会匹配aab和ab两个字符串 |
| +?           | 重复1次或多次，但尽可能少重复    |                  |                                                              |
| ??           | 重复0次或1次，但尽可能少重复     |                  |                                                              |
| {M,N}?       | 重复M到N次，但尽可能少重复       |                  |                                                              |
| {M,}?        | 重复M次以上，但尽可能少重复      |                  |                                                              |

* 如果需要匹配的字符是正则表达式中的特殊字符，那么可以使用\\进行转义处理，例如想匹配小数点可以写成\\.就可以了，因为直接写.会匹配任意字符；同理，想匹配圆括号必须写成\\(和\\)，否则圆括号被视为正则表达式中的分组。

---

## re模块核心函数

| 函数                                         | 说明                                                         |
| -------------------------------------------- | ------------------------------------------------------------ |
| compile(pattern, flags=0)                    | 编译正则表达式返回正则表达式对象                             |
| match(pattern, string, flags=0)              | 用正则表达式匹配字符串 成功返回匹配对象 否则返回None         |
| search(pattern, string, flags=0)             | 搜索字符串中第一次出现正则表达式的模式 成功返回匹配对象 否则返回None |
| split(pattern, string, maxsplit=0, flags=0)  | 用正则表达式指定的模式分隔符拆分字符串 返回列表              |
| sub(pattern, repl, string, count=0, flags=0) | 用指定的字符串替换原字符串中与正则表达式匹配的模式 可以用count指定替换的次数 |
| fullmatch(pattern, string, flags=0)          | match函数的完全匹配（从字符串开头到结尾）版本                |
| findall(pattern, string, flags=0)            | 查找字符串所有与正则表达式匹配的模式 返回字符串的列表        |
| finditer(pattern, string, flags=0)           | 查找字符串所有与正则表达式匹配的模式 返回一个迭代器          |
| purge()                                      | 清除隐式编译的正则表达式的缓存                               |
| re.I / re.IGNORECASE                         | 忽略大小写匹配标记                                           |
| re.M / re.MULTILINE                          | 多行匹配标记                                                 |

Python的re模块提供了一组用于处理正则表达式的函数。以下是常用的方法及其例子：

1. re.compile(pattern, flags=0)

将正则表达式的字符串形式编译为正则表达式对象。

```python
import re

pattern = re.compile(r'\d+')
result = pattern.findall('hello123world456')
print(result)  # ['123', '456']
```

2. re.match(pattern, string, flags=0)

尝试从字符串的起始位置匹配正则表达式，返回匹配对象，如果匹配失败返回None。

```python
import re

match = re.match(r'[a-z]+\d+', 'hello123world')
if match:
    print(match.group())  # hello123
else:
    print('No match')
```

3. re.search(pattern, string, flags=0)

在字符串中查找匹配正则表达式的第一个位置，返回匹配对象，如果匹配失败返回None。

```python
import re

match = re.search(r'[a-z]+\d+', 'hello123world')
if match:
    print(match.group())  # hello123
else:
    print('No match')
```

4. re.findall(pattern, string, flags=0)

返回所有匹配正则表达式的子串列表。

```python
import re

result = re.findall(r'[a-z]+\d+', 'hello123world456')
print(result)  # ['hello123', 'world456']
```

5. re.sub(pattern, repl, string, count=0, flags=0)

用于替换字符串中所有匹配正则表达式的子串。

```python
import re

result = re.sub(r'\d+', '888', 'hello123world456')
print(result)  # hello888world888
```

6. re.split(pattern, string, maxsplit=0, flags=0)

使用正则表达式分割字符串，返回分割后的列表。

```python
import re

result = re.split(r'\s+', 'hello  world')
print(result)  # ['hello', 'world']
```

### 例子1：验证输入用户名和QQ号是否有效并给出对应的提示信息

```python
import re

def main():
    username = input('请输入用户名')
    qq = input('请输入QQ号')
    
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$',username)
    if not m1:
        print('请输入有效的用户名')
        
    m2 = re.match(r'^[1-9]\d{4,11}$',qq)
    if not m2:
        print('请输入有效qq')
        
    if m1 and m2:
        print('你输入信息有效')
        
        
if __name__ == '__main__':
    main()
```

### 例子2：从一段文字提取出国内手机号码

```python
import re

def main():
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    
    mylist = re.findall(pattern,sentence)
    print(mylist)
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence,m.end())
        
if __name__ == '__main__':
    main()
```

该正则表达式中包含以下符号：

- `(?<=\D)`: 零宽度正回顾后发断言，表示要匹配的手机号前面必须是一个非数字字符，但这个字符并不属于匹配结果的一部分。这个符号的含义是“匹配后面紧接着这个表达式的位置，前面是一个非数字字符”。
- `1`: 匹配一个字符，表示手机号码的第一位数字必须是1。
- `[34578]`: 字符集合，匹配一个字符，表示手机号码的第二位数字必须是3、4、5、7、8中的一个。
- `\d{9}`: 匹配9个数字字符，表示手机号码的后面9位数字。
- `(?=\D)`: 零宽度正预测先行断言，表示要匹配的手机号后面必须是一个非数字字符，但这个字符并不属于匹配结果的一部分。这个符号的含义是“匹配前面紧接着这个表达式的位置，后面是一个非数字字符”。

综上，该正则表达式匹配一个字符串中的中国大陆手机号码，这个手机号码前后必须是一个非数字字符，第一位数字是1，第二位数字是3、4、5、7、8中的一个，后面跟着9个数字字符。

这段代码使用正则表达式搜索字符串 `sentence` 中符合模式 `pattern` 的子串，并将每个匹配到的子串打印出来。具体的步骤如下：

使用 `m.end()` 获取当前匹配子串的结尾位置，将这个位置作为第二个参数传递给 `pattern.search()`，继续搜索剩余的子串。

### 例子3：替换字符串中的不良内容

```python
import re

def main():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔','*',sentence,flags=re.IGNORECASE)
    
    print(purified)
    
if __name__ == '__main__':
    main()
```

`flags`参数是`re`模块中函数的一个可选参数，用于控制正则表达式的匹配模式。其中，`re.IGNORECASE`表示匹配时忽略大小写。

例如，如果要查找字符串中所有的"hello"，并且忽略大小写，可以使用如下代码：

```python
import re

sentence = "Hello world! hello Python! hEllo everyone!"
pattern = re.compile("hello", flags=re.IGNORECASE)
m = pattern.search(sentence)
while m:
    print(m.group())
    m = pattern.search(sentence, m.end())
```

这段代码将输出：

```python
Hello
hello
hEllo
```

可以看到，由于使用了`re.IGNORECASE`标志，所以不区分大小写地匹配了所有的"hello"。

### 例子：拆分长字符串

```python
import re

def main():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。, .]',poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)
    
    
if __name__ == '__main__':
    main()
```



---

## 多进程

```python
# 不使用进程
from random import randint
from time import time,sleep

def download_task(filename):
    print(f'开始下载{filename}')
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print(f'{filename}下载完成，耗时{time_to_download}')
    
def main():
    start = time()
    download_task('asdf.pdf')
    download_task('hjkl.pdf')
    end = time()
    print('总共耗%.2f秒' % (end - start))
    
if __name__ == '__main__':
    main()
```

```python
# 使用多进程
from multiprocessing import Process
from os import getpid
from random import randint
from time import time,sleep

def download_task(filename):
    print('启动下载进程，进程号[%d]' % getpid())
    print(f'开始下载{filename}')
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print(f'{filename}下载完成，耗时{time_to_download}')
    
def main():
    start = time()
    p1 = process(target = download_task,args=('asdf.pdf',))
    p1.start()
    p1 = process(target = download_task,args=('hjkl.pdf',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('总共耗%.2f秒' % (end - start))
    
if __name__ == '__main__':
    main()
```

### multiprocessing模块

`multiprocessing`模块提供了多个常用方法，用于创建、管理和通信进程。下面是一些常用方法的说明及示例：

1. `Process(target, args=(), kwargs={})`：创建一个新的进程对象，并指定进程的目标函数、参数和关键字参数。

```python
import multiprocessing

def worker(num):
    print('Worker:', num)

if __name__ == '__main__':
    process = multiprocessing.Process(target=worker, args=(10,))
    process.start()
```

2. `current_process()`：返回当前进程的`Process`对象。

```python
import multiprocessing

def worker():
    print('Worker:', multiprocessing.current_process().name)

if __name__ == '__main__':
    process = multiprocessing.Process(target=worker)
    process.start()
```

3. `Queue()`：创建一个进程间通信的队列。

```python
import multiprocessing

def producer(queue):
    for i in range(5):
        queue.put(i)

def consumer(queue):
    while not queue.empty():
        item = queue.get()
        print('Consumed:', item)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process1 = multiprocessing.Process(target=producer, args=(queue,))
    process2 = multiprocessing.Process(target=consumer, args=(queue,))
    process1.start()
    process2.start()
```

4. `Pool(processes=None)`：创建一个进程池，用于并行执行任务。

```python
import multiprocessing

def worker(num):
    return num * 2

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(worker, range(10))
        print(results)
```

5. `Lock()`：创建一个进程间的锁，用于确保对共享资源的互斥访问。

```python
import multiprocessing

def worker(lock, count):
    with lock:
        print('Acquired lock:', count)
        print('Released lock:', count)

if __name__ == '__main__':
    lock = multiprocessing.Lock()
    processes = []
    for i in range(3):
        process = multiprocessing.Process(target=worker, args=(lock, i))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
```

以上是`multiprocessing`模块的一些常用方法和示例，通过这些方法可以实现多进程的创建、通信和并行执行任务。根据实际需求，可以选择适合的方法来完成相应的任务。

## 多线程

```python
from random import randint
from threading import Thread
from time import time, sleep


def download(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('%s下载完成! 耗费了%d秒' % (filename, time_to_download))


def main():
    start = time()
    t1 = Thread(target=download, args=('Python从入门到住院.pdf',))
    t1.start()
    t2 = Thread(target=download, args=('Peking Hot.avi',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.3f秒' % (end - start))


if __name__ == '__main__':
    main()
```

**继承Thread类创建线程**

```python
from random import randint
from threading import Thread
from time import time, sleep


class DownloadTask(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s...' % self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成! 耗费了%d秒' % (self._filename, time_to_download))


def main():
    start = time()
    t1 = DownloadTask('Python从入门到住院.pdf')
    t1.start()
    t2 = DownloadTask('Peking Hot.avi')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('总共耗费了%.2f秒.' % (end - start))


if __name__ == '__main__':
    main()
```

**线程锁**

```python
from time import sleep
from threading import Thread, Lock


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先获取锁才能执行后续的代码
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()
```



### threading模块

`threading` 模块是 Python 中用于多线程编程的模块，可以通过创建线程来实现多任务并发执行。在 `threading` 模块中，每个线程都是一个 `Thread` 类的实例对象，可以通过创建多个 `Thread` 对象来创建多个线程。

下面是一个简单的示例，演示了如何使用 `threading` 模块创建线程：

```python
import threading

def worker(num):
    """线程的执行函数"""
    print("Thread %s is running..." % num)

# 创建两个线程
thread1 = threading.Thread(target=worker, args=(1,))
thread2 = threading.Thread(target=worker, args=(2,))

# 启动两个线程
thread1.start()
thread2.start()

# 等待两个线程执行完毕
thread1.join()
thread2.join()

print("All threads finished.")
```

在这个例子中，首先定义了一个函数 `worker`，这个函数是每个线程的执行函数。然后创建了两个线程 `thread1` 和 `thread2`，分别使用 `Thread` 类的构造函数创建，并指定线程的执行函数和参数。接着，分别启动这两个线程，并使用 `join` 方法等待这两个线程执行完毕，最后输出一条消息表示所有线程都执行完毕。

`threading` 模块中的一些常用方法和属性如下：

- `Thread(target, args=(), kwargs={})`：创建一个新线程，指定线程的执行函数、参数和关键字参数；
- `start()`：启动一个线程；
- `join([timeout])`：等待线程执行完毕，如果设置了 `timeout` 参数，则最多等待 `timeout` 秒；
- `is_alive()`：判断线程是否还在运行；
- `name`：获取或设置线程的名称；
- `enumerate()`：获取当前正在运行的所有线程；
- `active_count()`：获取当前正在运行的线程数量。

以上是 `threading` 模块的一些常用方法和属性，使用这些方法和属性可以实现线程的创建、启动、等待和管理。

## 异步

异步编程是一种编程模式，旨在提高程序的并发性和响应性，特别适用于处理IO密集型操作和并发任务。

传统的同步编程模型中，代码执行是按照顺序依次执行的，如果遇到阻塞操作（如IO操作），程序会等待操作完成后再继续执行下一步。这种模型在遇到多个阻塞操作时，会导致程序的执行效率低下。

异步编程模型通过使用异步任务和回调函数来解决这个问题。在异步编程中，任务的执行是非阻塞的，即任务提交后会立即返回，不会等待任务完成。当任务完成时，会通过回调函数或其他机制通知调用者，从而实现并发执行其他任务。

在Python中，异步编程通常使用协程（coroutine）和事件循环（event loop）来实现。协程是一种特殊的函数，可以在其中使用`await`关键字暂停执行，等待其他任务完成后再继续执行。事件循环负责管理协程的调度和执行，确保协程在合适的时机被调用。

Python提供了`asyncio`库，用于支持异步编程。`asyncio`提供了丰富的API和工具，用于编写异步代码，并提供了事件循环、协程、异步IO等功能。通过使用`async`和`await`关键字，可以定义协程函数，并在其中使用异步操作，以实现高效的异步编程。

异步编程的优点包括：

1. 高并发性：可以处理大量的并发任务，提高程序的吞吐量。
2. 更好的响应性：异步操作不会阻塞主线程，使得程序可以及时响应用户的请求。
3. 资源高效利用：由于异步操作不需要线程等资源来等待阻塞，可以更高效地利用系统资源。

然而，异步编程也存在一些挑战和注意事项，例如编写复杂的异步代码可能会增加代码的复杂性，需要注意处理并发操作时的同步和线程安全性问题。

总而言之，异步编程是一种提高程序并发性和响应性的编程模式，在处理IO密集型任务和并发操作时具有很大的优势。在Python中，可以使用`asyncio`库来实现异步编程，并通过协程和事件循环来管理和调度异步任务的执行。

---

协程（Coroutine）是一种轻量级的并发编程技术，可以在单线程内实现多个协作的执行流程。它可以在某个任务阻塞时，自动切换到另一个任务，从而实现任务之间的高效切换和并发执行。

在Python中，协程通常使用生成器函数和`yield`关键字来实现。通过使用`yield`语句暂停生成器函数的执行，并在需要时恢复执行，可以实现协程的特性。

下面是一个简单的示例，演示了如何使用协程来实现异步任务的执行：

```python
import asyncio

# 定义一个协程函数
async def async_task():
    print("开始执行异步任务")
    await asyncio.sleep(1)  # 模拟耗时操作
    print("异步任务执行完毕")

# 创建一个事件循环对象
loop = asyncio.get_event_loop()

# 将协程函数封装为任务并添加到事件循环中
task = loop.create_task(async_task())

# 执行事件循环，直到所有任务完成
loop.run_until_complete(task)
```

在上述示例中，通过定义一个协程函数`async_task`，并在其中使用`await`关键字来暂停执行，实现了异步任务的执行。通过`loop.create_task()`将协程函数封装为任务，并通过`loop.run_until_complete()`执行事件循环，直到任务完成。

协程的优势在于它可以提供更高效的并发执行和更低的资源消耗，特别适用于处理大量的IO密集型任务。在Python中，可以使用`asyncio`库来提供对协程的支持和管理，它提供了丰富的API和工具，用于编写异步代码并处理协程之间的交互和调度。

需要注意的是，协程的执行需要在异步环境中进行，例如使用`asyncio`库提供的事件循环。此外，Python还提供了一些其他的协程库和框架，如`gevent`和`twisted`，用于更高级的异步编程和网络应用开发。

---

## `Pillow`库-图像操作

Pillow 是一个 Python 图像处理库，提供了丰富的图像处理功能。下面是 Pillow 常用方法的说明和示例：

1. 打开和保存图像：
   - `Image.open(path)`: 打开指定路径的图像文件，并返回一个 `Image` 对象。
   - `Image.save(path, format)`: 将图像保存到指定路径，并指定保存的格式。

   示例：
   ```python
   from PIL import Image
   
   # 打开图像
   image = Image.open('image.jpg')
   
   # 保存图像
   image.save('output.jpg')
   ```

2. 调整图像大小：
   - `Image.resize(size)`: 调整图像的大小，参数 `size` 是一个元组，表示新的宽度和高度。

   示例：
   ```python
   from PIL import Image
   
   # 打开图像
   image = Image.open('image.jpg')
   
   # 调整图像大小
   new_size = (800, 600)
   resized_image = image.resize(new_size)
   
   # 保存调整后的图像
   resized_image.save('resized.jpg')
   ```

3. 图像旋转：
   - `Image.rotate(angle)`: 将图像按给定角度旋转，参数 `angle` 是旋转的角度。

   示例：
   ```python
   from PIL import Image
   
   # 打开图像
   image = Image.open('image.jpg')
   
   # 旋转图像
   rotated_image = image.rotate(90)
   
   # 保存旋转后的图像
   rotated_image.save('rotated.jpg')
   ```

4. 图像裁剪：
   - `Image.crop(box)`: 对图像进行裁剪，参数 `box` 是一个元组，表示裁剪区域的左上角和右下角坐标。

   示例：
   ```python
   from PIL import Image
   
   # 打开图像
   image = Image.open('image.jpg')
   
   # 裁剪图像
   box = (100, 100, 400, 300)  # 左上角坐标为 (100, 100)，右下角坐标为 (400, 300)
   cropped_image = image.crop(box)
   
   # 保存裁剪后的图像
   cropped_image.save('cropped.jpg')
   ```

5. 图像缩略图：
   - `Image.thumbnail(size)`: 创建图像的缩略图，参数 `size` 是一个元组，表示缩略图的大小。

   示例：
   ```python
   from PIL import Image
   
   # 打开图像
   image = Image.open('image.jpg')
   
   # 创建缩略图
   thumbnail_size = (200, 200)
   image.thumbnail(thumbnail_size)
   
   # 保存缩略图
   image.save('thumbnail.jpg')
   ```

以上是 Pillow 常用方法的一些示例，还有更多的方法可以用于图像处理，如图像滤镜、调整亮度对比度等。你可以根据具体的需求来查阅 Pillow 的官方文档以了解更多方法和参数的详细说明。

---

## `openpyxl`模块-Excel处理

openpyxl 是一个用于操作 Excel 文件的 Python 模块，它提供了一些常用方法来读取、修改和创建 Excel 文件。下面是 openpyxl 模块的一些常用方法、参数和示例：

1. 打开 Excel 文件：
   - `load_workbook(filename)`: 打开指定路径的 Excel 文件，并返回一个 `Workbook` 对象。

   示例：
   ```python
   from openpyxl import load_workbook
   
   # 打开 Excel 文件
   workbook = load_workbook('data.xlsx')
   ```

2. 选择工作表：
   - `active`: 返回当前活动的工作表。
   - `sheetnames`: 返回所有工作表的名称列表。
   - `get_sheet_by_name(name)`: 根据工作表名称获取工作表对象。

   示例：
   ```python
   # 选择活动工作表
   sheet = workbook.active
   
   # 获取所有工作表的名称
   sheet_names = workbook.sheetnames
   
   # 根据名称获取工作表
   sheet = workbook.get_sheet_by_name('Sheet1')
   ```

3. 读取和写入单元格数据：
   - `cell(row, column)`: 返回指定行列的单元格对象。
   - `value`: 单元格的值。

   示例：
   ```python
   # 读取单元格数据
   value = sheet.cell(row=1, column=1).value
   
   # 写入单元格数据
   sheet.cell(row=1, column=1).value = 'Hello, World!'
   ```

4. 保存 Excel 文件：
   - `save(filename)`: 将修改后的 Excel 文件保存到指定路径。

   示例：
   ```python
   # 保存 Excel 文件
   workbook.save('output.xlsx')
   ```

以上是 `openpyxl` 模块的一些常用方法和示例。你可以根据具体的需求来查阅 `openpyxl` 的官方文档，了解更多的方法和参数的详细说明。

---

## `docx`模块-Word处理

docx 是一个用于操作 Word 文档的 Python 模块，它提供了一些常用方法来读取、修改和创建 Word 文档。下面是 docx 模块的一些常用方法、参数和示例：

1. 打开 Word 文档：
   - `Document(filename)`: 打开指定路径的 Word 文档，并返回一个 `Document` 对象。

   示例：
   ```python
   from docx import Document
   
   # 打开 Word 文档
   document = Document('document.docx')
   ```

2. 读取和修改文档内容：
   - `paragraphs`: 返回文档中所有段落的列表。
   - `text`: 段落的文本内容。
   - `add_paragraph(text)`: 在文档末尾添加一个新段落，并设置文本内容。
   - `clear()`: 清空文档的所有内容。

   示例：
   ```python
   # 读取文档内容
   for paragraph in document.paragraphs:
       print(paragraph.text)
   
   # 添加新段落
   document.add_paragraph('This is a new paragraph.')
   
   # 清空文档内容
   document.clear()
   ```

3. 保存 Word 文档：
   - `save(filename)`: 将修改后的 Word 文档保存到指定路径。

   示例：
   ```python
   # 保存 Word 文档
   document.save('output.docx')
   ```

以上是 docx 模块的一些常用方法和示例。你可以根据具体的需求来查阅 docx 的官方文档，了解更多的方法和参数的详细说明。
