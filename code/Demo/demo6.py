# -*-  codeing = utf-8 -*-
# @Time : 2023/1/4 17:40
# @Author : LHJ青梦
# @File : demo6.py
# @Software: PyCharm

#namelist = []  #空列表

'''
namelist = ["zhang", "wang", "li"]

testlist = [1, "test"]

print(type(testlist[0]))    #可以存储混合类型数据
print(type(testlist[1]))


print(namelist[0])
print(namelist[1])
print(namelist[2])
'''
'''
namelist = ["zhang", "wang", "li"]

for name in namelist:
    print(name)

#print(len(namelist))    #列表长度

length = len(namelist)
i = 0
while i < length:
    print(namelist[i])
    i += 1
'''
'''
namelist = ["zhang", "wang", "li"]
#add   append()在末尾追加元素
nametemp = input("please input:")
namelist.append(nametemp)
for name in namelist:
    print(name)
'''
'''
#append列表当作元素，加入
a = [1,2]
b = [3,4]
a.append(b)
print(a)
#extend 将列表每个元素追加进入
a.extend(b)
print(a)
'''
'''
#增加 insert,指定下标为插入元素
a = [0, 1, 2]
a.insert(1, 3)  #[a,b]a表示元素插入下标所在位置，b表示为插入元素
print(a)
'''
'''
#删除
namelist = ["sherry", "les", "青梦", "YOLO"]
#del namelist[1]
#namelist.pop()#弹出末尾的元素
namelist.remove("les")#移除具体内容,如果有多个重复数据，但是remove只会从前往后遍历的，只删除找到的第一个
for name in namelist:
    print(name)
'''
'''
#改 根据下标指定修改

namelist = ["sherry", "les", "青梦", "YOLO"]
namelist[1] = "leshj"

for name in namelist:
    print(name)
'''
'''
# 查  [in,not in]
namelist = ["sherry", "les", "青梦", "YOLO"]
findName = input("please input:")

if findName in namelist:
    print("find success")
else:
    print("not find")
'''
'''
a = ["a", "b", "c", "a", "b"]

print(a.index("a", 1, 4))
#起点一到四,在这个范围查找
#可以查找指定下标范围的元素，并返回找到对应数据的下标
#print(a.index("a", 1, 3))
#范围区间左闭右开[a,b)
#找不到会报错，可以通过异常处理解决
'''
'''
a = ["a", "b", "c", "a", "b"]
print(a.count("c"))
#统计某个元素出现了几次
'''
'''
#排序反转
a = [1, 4, 2, 3]
print(a)
a.reverse() #将所有元素反转
print(a)
a.sort()    #排序，默认升序
print(a)
a.sort(reverse=True)    #反转后排序，也就是降序
print(a)
'''
'''
#schoolName = [[], [], []]   #有3个空元素的列表，每个元素都是空元素
schoolName = [["北京大学", "清华大学"], ["南开大学", "天津大学", "广州大学"], ["山东大学", "南京大学"]]

print(schoolName[0])
print(schoolName[0][1])
'''

'''
import random

offices = [[], [], []]

names = ["A", "B", "C", "D", "E", "F", "G", "H"]

for name in names:
    #每一个循环插入老师
    index = random.randint(0,  2)
    offices[index].append(name)

i = 1
for office in offices:
    print("办公室 %d 人数  %d" % (i, len(office)))
    i += 1
    for name in office:
        print("%s"%name, end="\t")
    print("\n")
    print("-"*20)
'''


products = [["iphone", 6888], ["MacPro", 14800], ["小米6", 2499], ["Coffee", 31], ["Book", 60], ["Nike", 699]]

i = 0
j = 0
k = 0
print("----商品列表-----")

for product in products:
    print(i, products[j][k], products[j][k-1])
    i += 1
    j += 1







