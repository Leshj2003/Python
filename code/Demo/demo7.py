# -*-  codeing = utf-8 -*-
# @Time : 2023/1/5 20:41
# @Author : LHJ青梦
# @File : demo7.py
# @Software: PyCharm
'''
####元组#####
tup1 = ()
print(type(tup1))

#tup2 = (50) #这个不是元组
#tup2 = (50,)    #用逗号间隔区分
tup2 = (50, 60, 70)#多个的话默认是元组的
print(type(tup2))
'''

'''
tup1 = ("abc", "def", 2000, 2010)
print(tup1[0])
print(tup1[-1]) #负数就是倒着访问
print(tup1[1:5])    #从下标为1开始，仍然运行，如果增加至刚刚好，仍是左闭右开
'''

##### 增 ######
'''
tup1 = (12, 34, 56)
tup2 = ("abc", "xyz")
tup = tup1 + tup2
print(tup)  #链接的概念，连在一起
'''

##### 删 ######
'''
tup1 = (12, 34, 56)
print(tup1)
del tup1    #直接删除了元组的整个变量,不允许删除某个值
print("删除后")
print(tup1)
'''
##### 改 ######

#tup1 = (12, 34, 56)
#tup1[0] = 100   #不允许这样修改的

##### 查 ######

################   字典   #################
#键值对，key-value.键唯一，值不唯一,通过键找值


#字典的定义
'''
info = {"name": "sherry", "age": 18}
#字典的访问
print(info["name"])
print(info["age"])
#如果访问的键不存在
#print(info["gender"])

#为了解决报错，不影响后续的操作以下操作,使用get方法，返回none
#print(info.get("gender"))

print(info.get("gender", "m"))  #可以设定默认值，默认值m(找不到才发挥作用，如果找到了则用找到的数据

'''

info = {"id":1, "name": "sherry", "age": 18}

#######  增  ########
'''
newID = input("please input:")
info["id"] = newID
print(info["id"])

'''

#######  删  ########

#[del]
'''
print("before:%s"%info["name"])
del info["name"]
'''
#print("after:%s"%info["name"]) #这个删除也是不止删除值，还删除了键，就是键值对一起删了
# del info    #删除了整个字典

#[clear] 清空
# print("before:%s"%info)
# info.clear()
# print("after:%s"%info)


#######  改  ########
#
# info["age"] = 20
# print(info["age"])


#######  查  ########
#便利
# print(info.keys())  #拿到所有的键:列表形式
# print(info.values())    #得到所有的值
# print(info.items())    #得到所有的项，每个键值对是一个元组

#遍历所有的值


# for key in info.keys():
#     print(key)
#
# for value in info.values():
#     print(value)

#遍历所有的键值对
# for key, value in info.items():
#     print("key=%s value=%s"%(key, value))


# mylist = ["a", "b", "c", "d"]
# #枚举函数，同时拿到列表的下标及内容
# for i, x in enumerate(mylist):
#     print(i, x)


#去重操作，设置set集合，example：




