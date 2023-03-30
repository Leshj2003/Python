# -*-  codeing = utf-8 -*-
# @Time : 2023/1/20 18:15
# @Author : LHJ青梦
# @File : testBs4.py
# @Software: PyCharm
import re

from bs4 import BeautifulSoup

file = open("./baidu.html", "rb")

html = file.read()

bs = BeautifulSoup(html, "html.parser")     #解析器是html parser，形成树形结构
#找到第一个找到的标签
# print(bs.title)
# print(bs.a)
# print(bs.head)

#1.Tag 标签及其内容，只能拿到第一个找到的

#2.NavigableString
# print(bs.title.string)      #只要里面的内容
#
# print(type(bs.title.string))

# print(bs.a.attrs)       #快速拿到标签的属性

#3.BeautifulSoup    表示整个文档

# print(type(bs))

# print(bs.name)
#
# print(bs)


#4.注释 是一个特殊的NavigableString，输出不包含注释符号
#
# print(bs.a.string)
# print(type(bs.a.string))


# ——————————————————————————————————————————

# 文档的遍历

# print(bs.head.contents)       #查询到的为列表
# print(bs.head.contents[1])


# 文档的搜索
#(1)find_all()
# 字符串过滤：会查找与字符串完全匹配的内容
# t_list = bs.find_all("a")       #查询到的为列表

#正则表达式搜索：使用search（）方法来匹配内容

# t_list = bs.find_all(re.compile("a"))

# 方法搜索，传入一个函数，根据要求搜索

# def name_is_exists(tag):
#     return tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exists)
#
#
# for item in t_list:
#     print(item)


# print(t_list)

#2.kwargs   参数

# t_list = bs.find_all(id="head")
# t_list = bs.find_all(class_="True")
# t_list = bs.find_all(href="http://news.baidu.com/")
# for item in t_list:
#     print(item)

#3.text参数

# # t_list = bs.find_all(text="hao123")
# t_list = bs.find_all(text=["hao123", "地图", "贴吧"])
#
# t_list = bs.find_all(text=re.compile("\d"))     #应用正则表达式来查找包含特定的文本的内容(标签的字符串

#4.limit参数

# t_list = bs.find_all("a", limit=3)    #限定多少个
#
# for item in t_list:
#     print(item)




# css选择器

# print(bs.select(('title')))

#__
# # t_list = bs.select('title')     #通过标签查找
# t_list = bs.select(".item")     #通过类名查找
# t_list = bs.select("#u1")       #通过id查找
# t_list = bs.select("a[class='bri']")      #通过属性查找
# t_list = bs.select("head > title")      #通过子标签查找

# for item in t_list:
#     print(item)


t_list = bs.select(".item ~ .bri")      #通过兄弟节点查找







