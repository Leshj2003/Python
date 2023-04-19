# Total

---



##  print()函数



 输出函数print()

输出内容数字、字符串、含运算符的表达式

输出目的地显示器、文件

<img src="D:/Desktop/python/images/image-20230322223915674.png" />

输出形式换行，不换行

---



## 转义字符

\\ \  反斜杠\

\'  单引号

\" 双引号

\n  换行

\t   制表位（占4个字符）

\r  回车

print（"hello\rworld"）>world

\b  退位

print("hello\bworld") >hellworld



### 原字符

不希望转义字符起作用

在字符串之前加r/R

print(r"hello\nworld\\") 

---

chr() 转成字符型

print(chr(0b100111001011000))

ord() 转成十进制

print(ord(‘乘’))

---

## 标识符和保留字

* 字母、数字、下划线
* 不能以数字开头
* 不能是保留字
* 严格区分大小写

---

## 变量

由标识、类型、值组成

id(obj)、type(ojb)、print(obj)

内存垃圾：多次赋值，会被覆盖

 



数据类型：int float bool str

---

### 整数类型

默认十进制

还可以二进制0b、八进制0o、十六进制0x

---

### 浮点类型

浮点数计算可能会出现小数位不确定的情况

可导入模块解决

from decimal import Decimal

print(Decimal('1.1')+Decimal('2.2'))

---

### 布尔类型

True 1

False 0

---

### 字符串类型

可以用单引号、双引号、三引号

三引号可以分散多行

---

## 数据类型转换

<img src="D:/Desktop/python/images/uTools_1679646338693.png" />



## 注释

* 单行注释 #
* 多行注释 '''   '''

---

## 输入函数input()

返回值的类型是str

​	present = input('想要什么礼物')

​	print(present)

### input()高级使用

a = input()

b = input()

print(a + b)

#输入10，20，输出1020，+起到链接作用

#解决问题就是转换数据类型a = int(input()),b = int(input())

---

## 算术运算符

加+减-乘*除/整除//

取余运算符%

幂运算符**



* 整除就是取整

 一正一负的话，向下取整，eg:-9//4=-3    ->=-2.2

---

## 赋值运算符

* 从右到左运算

* 支持链式赋值 a = b = c = 20

* 支持参数赋值 += -= *= /= //= %=

* 支持系列解包赋值 a,b,c = 20,30,40

  ### 交换

  a,b = b,a

---

## 比较运算符

对变量或表达式的结果进行大小、真假等比较

\> < >= <= !=

== 对象value的比较

is,is not对象id的比较

* =赋值运算符，==比较运算符（比较的是值）
* is比较对象的标识使用

---

## 布尔运算符

and、or、  not、 in 、not in

<img src="D:/Desktop/python/Log/images/uTools_1679830744198.png"/>



eg:

a,b = 1,2

print(a==1 and b==2)#True

* not对布尔类型的操作数取反

* in，not in

---

## 位运算

位与&  对应数位都是1，结果数位才是1，否则为0

位或|   对应数位都是0，结果数位才是0，否则为1

左移位运算符<<  高位溢舍弃，低位补0

右移位运算符>>   低位移除舍弃，高位补0

<u> 转换成二进制，用二进制理解</u>

---

## 运算符的优先级

<img src="D:/Desktop/python/Log/images/uTools_1679832517676.png"/>



* （）

* 算术运算 幂
* 乘除
* 加减
* 位运算 
* 比较运算
* 赋值运算符



---

## 组织结构——顺序结构

> 顺序结构
>
> 选择结构 if语句
>
> 循环结构 while语句、for-in语句

---

## 对象的布尔值

<u>一切皆对象,所有对象都有一个布尔值</u>

* false
* 数值0
* 空字符串
* 空列表
* 空元组
* 空字典
* 空集合

---

## 单分支结构

``` Python
money = 1000

s = int(input('请输入取款金额'))

if money >= s:

	money = money - s

	print('取款成功，余额为；',money)
```

---

## 双分支结构

```python
num = int(input('请输入一个整数') )

if num % 2 == 0:

	print(num,'是偶数)

else:

print('是奇数')
```



---

## 多分支结构

```py
score = input('请输入成绩')

if score >= 90 and score <= 100:	#也可以90<=score<=100

	print('A')

elif score >= 80 and score <=89:

	print('B')

elif score >=70 and score <=79:

	print('C')

elif score >=60 and score <= 69:

	print('D')

elif score >=0 and score <=59:

	print('E')

else:

	print('对不起')
```



---

## 嵌套if

``` python
answer = input('你是会员嘛？y/n')
money = float(input('请输入您的购物金额：'))
if answer =='y':
    if money >= 200:
        print('打八折付款金额：',money * 0.8)
    elif money >= 100:
        print('打九折付款金额：',money * 0.9)
    else:
        print('不打折付款金额：',money)
else:
    if money >= 250:
        print('达九点五折付款金额：',money * 0.95)
    else:
        print('不打折付款金额：',money)
```



---

## 条件表达式

``` python
num1 = int(input())
num2 = int(input())

if num1 >= num2:
    print(num1,'大于等于',num2)
else:
    print(num1,'小于',num2)
```

* 使用条件表达式

``` python
num1 = int(input())
num2 = int(input())


print((str(num1)+'大于等于'+str(num2) if num1 >= num2 else (str(num1)+'小于'+str(num2))
#  加号连接欸需要都是字符串类型，true执行前面的，false执行后面的
```



----

## pass语句

* 语句什么都不做，只是一个占位符
* 还没想好怎么写的时候，为了搭建语法结构,程序不报错

```python
answer = input('你是会员吗')

if answer == 'y':
    pass
else:
    pass
```



---

## range()函数

* 用于生成整数数列
* 创建的三种方式：
  * range(stop)--[0,stop),步长为1
  * range(start,stop)--[start,stop),步长为1
  * range(start,stop,step)--[start,stop),步长为step

```python
r = range(10)	#默认从零开始，相差的为步长1
print(r)	#输出range(0,10)
print(list(r))
```



```python
r = range(1,10)
print(list(r))
```



```python
r = range(1,10,2)
print(list(r))
print(10 in r)
print(10 not in r)
```



---

## 循环结构-while函数()

* while
* for -in

```python
a = 1
while a < 10
	print(a)
    a  += 1
```



### 四部循环法

* 初始化变量
* 条件判断
* 条件执行体
* 改变变量

```python
#求0到4的累加和
sum = 0
#1、
a = 0
#2、
while a < 5:
#3、
	sum += a
    a += 1
#4、
print(sum)
```



### 练习

```python
#计算1-100的偶数和
a = 1
sum = 0
while a < 101:
    if a % 2 == 0:
   #if a % 2:奇数和
   #if not bool(a % 2):取反
        sum += a
    a += 1
print(sum)
       
```

---

## for-in循环

* in表达从（字符串、序列）中依次取值，又称为遍历
* for-in遍历的对象必须是可迭代对象

```python
for item in 'Python':
	print(item)
'''
P
y
t
h
o
n
'''

for i in range(10):
    print(i)
'''
和上面一样，输出0-9，输出10次
'''
```



```python
for _ in range(5):	#不用到变量
    print('人生苦短，我用python')
    
    
#使用for循环，计算1-100的偶数和
sum = 0
for item in range(1,101):
    if item % 2 == 0:
        sum += item
print(item)
```



---

## 练习-水仙花数

* 输出100-999之间的水仙花数
* 153=3\*3\*3+5\*5\*5+1\*1\*1

```python
for item in range(100,1000):
    a = item % 10	#个位
    b = item // 10 % 10	#十位
    c = item // 100	#百位
    if a ** 3 + b ** 3 + c ** 3 == item:
        print(item)
```

---

## break控制语句

* 用于结束循环结构，通常与分支结构if一起使用

```python
for item in range(3):
    pwd = input('请输入密码')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
```



```python
a = 0
while a < 3:
    pwd = input('请输入密码')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
    a += 1
```

---

## continue控制语句

* 用于结束当前循环，进入下一步循环，通常与分支结构if一起使用

```python
#输出1-50之间所有5的倍数
for item in range(1,51):
    if item % 5 == 0:
        print(item)

  
#使用continue
for item in range(1,51):
    if item % 5 != 0:
        continue
    print(item)
```

---

## else语句

* if:else:	if条件表达式不成立时执行
* while:else:	没有碰到break时执行
* for:else:	没有碰到break时执行

```python
for item in range(3):
    pwd = input('请输入密码')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码错误')
else:
    print('对不起，三次密码均输入错误')
        
```

```python
a = 0
while a < 3:
    pwd = input('请输入密码')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码错误')
    a += 1
else:
    print('对不起，三次密码均输入错误')
```

---

## 嵌套循环

```python
# 输出一个三行四列的矩形
for i in range(1,4):
    fro j in range(1,5):
        print('*'，end='\t')	#不换行
    print()	#换行
```

```python
# 打印一个直角三角形
for i in range(1,10):
    for j in range(1,i+1):
        print('*',end='')
    print()
```

```python
#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t')
    print()
```

---

## 二重循环中的break与continue

* 只用于本层的循环，不影响外层循环

```python
for i in range(5):
    for j in range(1,11):
        if j % 2 ==0:
            #break	# 输出5次1
            continue	#输出5次1 3 5 7 9
        print(j)

```

---

## 为什么需要列表

* 变量可以存储一个元素，而列表可以存储n个元素的”引用“
* 相当于其他语言的数组

```python
a = 10
lst = ['hello','world',98]
print(id(lst))
print(type(lst))
print(lst)
```

---

## 列表对象的创建

``` python
# 使用[]创建
lst1 = ['hello','world',98]
print(lst1)	#有序排序
print(lst[0]，lst[-3])	#索引映射
# 使用内置函数list()
lst2 = list(['hello','world',98])
```

| id:123       | id:456       | id:789    |
| ------------ | ------------ | --------- |
| type :str    | type :str    | type :int |
| value :hello | value :world | value :98 |

### 列表的特点

* 列表元素按顺序有序排序
* 索引映射唯一一个数据
* 列表可以存储重复的数据
* 任意数据类型混存
* 根据需要动态分配和回收内存

---

## 获取指定元素的索引

* index()

  * 如列表中存在n个相同，只返回相同元素中的第一个元素的索引
  * 如果查询的元素在列表中不存在，则会抛出`ValueError`
  * 还可以在指定的start和stop之间进行查找

* 获取单个元素

  * 正向索引从0到N-1  eg: `lst[0]`
  * 逆向索引-N到-1   eg: `lst[-N]`
  * 指定索引不存在，抛出`indexError`

  

```python
lst = ['hello','world',98.'hello']
print(lst.index('hello'))
#报错ValueError
#print(lst.index('Python'))
#print(lst.index('hello',1,3))
```

```python
lst = ['hello','world',98.'hello','world',234]
print(lst[2])
print(lst[-3])
#print(lst[10])
```

---

## 获取多个列表的多个元素—切片操作

列表名[`start`:`stop`:`step`]

* 切片的结果：原列表的拷贝
* 切片的范围：[start,stop)
* step默认为1
* step为正数：
  * [:`stop`:`step`]	第一个元素默认列表第一个元素
  * [`start`::`step`]    最后一个元素默认列表最后一个元素
* step为负数：
  * [:`stop`:`step`]	最后一个元素默认列表最后一个元素
  * [`start`::`step`]    第一个元素默认列表第一个元素

```python
lst = [10,20,30,40,50,60,70,80]
print(lst[1:6:1])
print('原列表',id(lst))
lst2 = lst[1:6:1]
print('切的片段',id(lst2))
print(lst[1:6])
print(lst[1:6:])
#start = 1,stop = 6,step = 2
print(lst[1:6:2])
#stop = 6,step = 2,start采用默认
print(lst[:6:2])
#start = 1,step = 2,stop采用默认
print(lst[1::2])
print('--------------步长为负数--------------')
print('原列表',lst)
print(lst[::-1])
#start = 7,stop省略，step=-1
print(lst[7::-1])
#start = 6,stop = 0,step = -2
print(lst[6:0:-2])
```



---

## 列表元素的判断及遍历

* 判断指定元素在列表中是否存在
  * ​	元素 in 列表名
  * ​    元素 not in 列表名
* 列表元素的遍历
  * for 迭代变量 in 列表名

```python
print('p' in 'python')
print('k' not in 'python')

lst = [10,20,'python','hello']
print(10 in lst)
print(100 in lst)
print(10 not in lst)
print(100 not in lst)

for item in lst:
    print(item)
```



---

## 列表元素的添加操作

| 增加操作 | 方法       | 操作描述                             |
| -------- | ---------- | ------------------------------------ |
|          | `append()` | 在列表的末尾添加一个元素             |
|          | `extend()` | 在列表的末尾至少添加一个元素         |
|          | `insert()` | 在列表的任意位置添加一个元素         |
|          | 切片       | 在列表的任意位置添加至少添加一个元素 |

```python
#向列表的末尾添加一个元素
lst = [10,20,30]
print('添加元素之前',lst,id(lst))
lst.append(100)
print('添加元素之后',lst,id(lst))
```

```python
lst2 = ['hello','world']
#lst.append(lst2)	#将lst2作为一个元素添加到列表的末尾,输出[10,20,30,100,['hello','world']]
lst.extend(lst2)	#输出[10,20,30,100,'hello','world']
print(lst)

```

```python
#在任意位置上添加一个元素
lst.insert(1,90)
print(lst)	#输出[10,90,20,30,100,'hello','world']

lst3 = [True,False,'hello']
#任意的位置上田添加N多个元素
lst[1:] = lst3
print(lst)	#输出[10,True,False,'hello']
```



---

## 列表元素的删除操作

| 删除操作 | 方法       | 操作描述                                                     |
| -------- | ---------- | ------------------------------------------------------------ |
|          | `remove()` | 1、一次删除一个元素<br />2、重复元素只删除第一个<br/>3、元素不存在 |
|          | `pop()`    | 1、删除一个指定索引位置上的元素<br/>2、指定索引不存在抛出`IndexError`<br/>3、不限定索引，删除列表中最后一个元素 |
|          | 切片       | 一次至少删除一个元素                                         |
|          | `clear()`  | 清空列表                                                     |
|          | `del`      | 删除列表                                                     |

```python
lst = [10,20,30,40,50,60,30]
lst.remove(30)	#从列表中列表中移除一个元素，如果有重复元素只移除第一个元素
print(lst)
#lst.remove(100)
```

```python
#pop()根据索引移除元素
lst.pop(1)
print(lst)
#lst.pop(5)
lst.pop()	#不指定参数，删除列表中最后一个
```

```python
print(------------切片操作删除至少一个元素，将产生一个新的列表对象------------)
new_list = lst[1:3]
print('原列表',lst)
print('切片后的列表',new_lst)

'''不产生新的列表对象，而是删除原列表中的内容'''
lst[1:3] = []
print(lst)
```

## 

---

## 获取多个列表的多个元素—切片操作

列表名[`start`:`stop`:`step`]

* 切片的结果：原列表的拷贝
* 切片的范围：[start,stop)
* step默认为1
* step为正数：
  * [:`stop`:`step`]	第一个元素默认列表第一个元素
  * [`start`::`step`]    最后一个元素默认列表最后一个元素
* step为负数：
  * [:`stop`:`step`]	最后一个元素默认列表最后一个元素
  * [`start`::`step`]    第一个元素默认列表第一个元素

```python
lst = [10,20,30,40,50,60,70,80]
print(lst[1:6:1])
print('原列表',id(lst))
lst2 = lst[1:6:1]
print('切的片段',id(lst2))
print(lst[1:6])
print(lst[1:6:])
#start = 1,stop = 6,step = 2
print(lst[1:6:2])
#stop = 6,step = 2,start采用默认
print(lst[:6:2])
#start = 1,step = 2,stop采用默认
print(lst[1::2])
print('--------------步长为负数--------------')
print('原列表',lst)
print(lst[::-1])
#start = 7,stop省略，step=-1
print(lst[7::-1])
#start = 6,stop = 0,step = -2
print(lst[6:0:-2])
```



---

## 列表元素的判断及遍历

* 判断指定元素在列表中是否存在
  * ​	元素 in 列表名
  * ​    元素 not in 列表名
* 列表元素的遍历
  * for 迭代变量 in 列表名

```python
print('p' in 'python')
print('k' not in 'python')

lst = [10,20,'python','hello']
print(10 in lst)
print(100 in lst)
print(10 not in lst)
print(100 not in lst)

for item in lst:
    print(item)
```



---

## 列表元素的添加操作

| 增加操作 | 方法       | 操作描述                             |
| -------- | ---------- | ------------------------------------ |
|          | `append()` | 在列表的末尾添加一个元素             |
|          | `extend()` | 在列表的末尾至少添加一个元素         |
|          | `insert()` | 在列表的任意位置添加一个元素         |
|          | 切片       | 在列表的任意位置添加至少添加一个元素 |

```python
#向列表的末尾添加一个元素
lst = [10,20,30]
print('添加元素之前',lst,id(lst))
lst.append(100)
print('添加元素之后',lst,id(lst))
```

```python
lst2 = ['hello','world']
#lst.append(lst2)	#将lst2作为一个元素添加到列表的末尾,输出[10,20,30,100,['hello','world']]
lst.extend(lst2)	#输出[10,20,30,100,'hello','world']
print(lst)

```

```python
#在任意位置上添加一个元素
lst.insert(1,90)
print(lst)	#输出[10,90,20,30,100,'hello','world']

lst3 = [True,False,'hello']
#任意的位置上田添加N多个元素
lst[1:] = lst3
print(lst)	#输出[10,True,False,'hello']
```



---

## 列表元素的删除操作

| 删除操作 | 方法       | 操作描述                                                     |
| -------- | ---------- | ------------------------------------------------------------ |
|          | `remove()` | 1、一次删除一个元素<br />2、重复元素只删除第一个<br/>3、元素不存在 |
|          | `pop()`    | 1、删除一个指定索引位置上的元素<br/>2、指定索引不存在抛出`IndexError`<br/>3、不限定索引，删除列表中最后一个元素 |
|          | 切片       | 一次至少删除一个元素                                         |
|          | `clear()`  | 清空列表                                                     |
|          | `del`      | 删除列表                                                     |

```python
lst = [10,20,30,40,50,60,30]
lst.remove(30)	#从列表中列表中移除一个元素，如果有重复元素只移除第一个元素
print(lst)
#lst.remove(100)
```

```python
#pop()根据索引移除元素
lst.pop(1)
print(lst)
#lst.pop(5)
lst.pop()	#不指定参数，删除列表中最后一个
```

```python
print(------------切片操作删除至少一个元素，将产生一个新的列表对象------------)
new_list = lst[1:3]
print('原列表',lst)
print('切片后的列表',new_lst)

'''不产生新的列表对象，而是删除原列表中的内容'''
lst[1:3] = []
print(lst)
```



---

## 列表元素的修改操作

* 为指定索引的元素赋予一个新值
* 为指定的切片赋予一个新值

```python
lst = [10,20,30,40]
lst[2] = 100
print(lst)
lst[1:3] = [300,400,500,600]
print(lst)
```





---

## 列表元素的排序操作

* 调用`sort()`方法，列有中的所有元素默认按照从小到大的顺序进行排序们可以指定reverse = True，进行降序排序
* 调用内置函数sorted()，可以指定reverse = True，进行降序排序，原列表不发生改变

```python
lst = [20,40,10,98,54]
print('排序前的列表',lst,id(lst))
#开始排序，调用列表对象的sort()方法，默认是升序
lst.sort()
print('排序后的列表',lst,id(lst))

#通过指定关键字参数，将列表中的元素进行降序排序
lst.sort(reverse = True)	#降序
print(lst)
lst.sort(reverse = False)	#升序
print(lst)

print('---------------内置函数sorted(),将产生一个新的列表对象')
lst = [20,40,10,98,54]
print('原列表',lst)
new_lst = sorted(lst)
print(lst)
print(new_lst)
#降序
desc_new = sorted(lst,reverse = True)
print(desc_lst)
```



---

## 列表生成式

* 语法格式[`i*i` for `i` in range(1,10)]
  * `i*i`表示列表元素的表达式，列表中真正的值
  * `i`自定义变量
  * range(1,10)可迭代对象
* 注意事项：“表示列表元素的表达式”中通常包含自定义变量

```python
lst = [i for i in range(1，10)]
#输出[1,2,3,4,5,6,7,8,9]
print(lst)
lst = [i*i for i in range(1，10)]
#输出[1,4,9,16,25,36,49,64,81]
print(lst)

'''列表中的元素的值为2，4，6，8，10'''
lst2 = [i * 2 for i in range(1,6)]
print(lst2)
```



---

## 字典

### 什么是字典

* 内置的数据结构之一，也是一个可变序列
* 键值对的方式存储数据，是一个无序的序列

```python
score = {'张三' : 100, '李四' : 98, '王五' : 45}
```

<img src="D:/Desktop/python/images/uTools_1680423849685.png"/>

### 字典的创建

* 

```python
scores = {'张三' : 100, '李四' : 98, '王五' : 45}
```

* 

```python
dict(name='jack',age=20)
```

### 字典的常用操作

* 字典中元素的获取
  * [ ] `scores['张三']`
  * get()方法    `scores.get('张三')`

* [ ]取值与使用get()取值的区别
  * [ ]如果字典中不存在指定的key，抛出`keyError`异常
  * get()方法取值，如果字典中不存在指定的key，并不会抛出`KeyError`而是返回None，可以通过参数设置默认的value,以便指定的key不存在时返回

```python
scores = {'张三' : 100, '李四' : 98, '王五' : 45}
print(scores['张三'])
print(scores.get('张三'))
print(scores.get('陈六'))	#返回None
print(scores.get('玛奇',99))	#输出99
```

---

## 字典元素的增删改

* key的判断

  * in	指定key在字典中存在返回True
  * not in    指定的key在字典中不存在返回True

* 字典元素的删除

  ```python
  del scores['张三']
  ```

* 字典元素的新增

  ```python
  scores['Jack'] = 90
  ```

  

```python
scores = {'张三' : 100, '李四' : 98, '王五' : 45}
print('张三' in scores)
print('张三' not in scores)

del scores('张三')	#删除指定的键值对
scores.clear()	#清空字典中的所有元素
print(scores)
scores['陈六'] = 98
print(scores)

scores['陈六'] = 100
print(scores)
```

## 

---

## 获取字典视图的三个方法

* keys()获取字典中所有key
* values()获取字典中所有的value
* items()获取字典中所有的key,value对

```python
scores  = ['张三':100,'李四':98,'王五':46]
keys = scores.keys()
print(keys)	#输出dict_keys(['张三','李四','王五'])
print(type(keys))	#输出dict_keys类型
print(list(keys))	#转换成列表
```

```python
scores  = ['张三':100,'李四':98,'王五':46]
values = scores.values()
print(values)
print(type(values))
print(list(values))
```

```python
scores  = ['张三':100,'李四':98,'王五':46]
items = scores.items()
print(item)	输出dict_items([('张三',100),('李四',98),('王五',46)])这是一个列表元组，元组（，）
```



---

## 字典元素的遍历

```python
scores  = ['张三':100,'李四':98,'王五':46]
for item in scores:
    print(item,scores[item],scores.get(item))
'''
输出
张三 100 100
李四 98 98
王五 46 46
'''
```



---

## 字典的特点

<img src="D:/Desktop/python/images/4.3.png"/>

* 因为是无序的所以不可以像列表一样插入在任意位置
* 不可以用列表做键，因为要求不可变对象



---

## 字典生成式

<img src="D:/Desktop/python/images/uTools_1680520834304.png"/>

### 内置函数zip()

```python
items = ['Fruits','Books','Others']
prices = [96,78,85]
d = {item.upper():price for item,price in zip(items,prices)}
print(d)
```

* `upper()`大写字母
* 压缩过程以短的那个压缩eg:

```python
items = ['Fruits','Books','Others']
prices = [96,78,85,100,200]
#输出：['Fruits':96,'Books':78,'Others':85]
```



---

## 元组

* Python内置数据结构之一，是一个不可变序列

**不可变序列与可变序列**

* 不可变序列：字符串、元组
  * 不可变序列：没有增删改查的操作

* 可变序列：列表、字典
  * 可变序列：可以对序列执行增删改操作，对象地址发生更改


```python
#可变序列	列表，字典
lst = [10,20,30]
print(id(lst))
lst.append(300)
print(id(lst))
#不可变序列，字符串、元组
s = 'hello'
print(id(s))
s += 'world'
print(id(s)) 
print(s)
```



---

## 元组的创建方式

* 直接小括号,小括号可以省略 

  ```python
  t = ('Python','hello',90)
  ```

* 使用内置函数tuple()

  ```python
  t = tuple(('Python','hello',90))
  ```

* 只包含一个元组的元素需要使用逗号和小括号

  ```python
  t = (10,)
  ```




## 

---

## 为什么将元组设计成可变序列

* 在多任务环境下，同时操作对象时不需要加锁

* 因此，在程序中尽量使用不可变序列

* 注意事项：

  * 元组中存储的时对象的引用

    a)如果元组中对象本身不可变对象，则不能引用其他对象

    b)如果元组中的对象时可变对象，则可变对象的引用不允许改变，但数据可以改变

<img src="D:/Desktop/python/images/uTools_1680576478883.png"/>

```python
t = (10,[20,30],9)
print(t)
print(type(t))
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))
#尝试将t[1]修改为100
print(id(100))
#t[1] = 100	#报错，元组不允许修改元素
t[1].append(100)
print(t,id(t[1]))	#物理地址不会改变
```

* `id()`查看内存的地址



---

## 元组的遍历

* 元组是可迭代对象，所以可以使用for...in进行遍历

```python
t = ('Python','world',98)
#使用索引
print(t[0])
print(t[1])
print(t[2])
#print(t[3])	IndexError,超出范围

#遍历
for item in t:
    print(item)
```



---

## 集合

* Python语言提供的内置数据结构
* 与列表、字典一样都属于可变类型的序列
* 集合是没有value的字典

**添加数据也会进行hash函数进行计算**

### 集合的创建方式

* 直接{}
* 使用内置函数set()

```python
#使用{}
s = {2,3,4,5,5,6,7,7}	#和字典一样不能存储重复，会去掉重复的，输出{2,3,4,5,6,7}
print(s)

#使用set()
s1 = set(range(6))
print(s1,type(s1))
s2 = set([1,2,3,3,4,5,5])
print(s2)	#将列表转换成集合，并去掉重复的
s3 = set((1,2,3,3,4,5))	#输出是无序的
print(s3)
s4 = set('Python')
print(s4)#输出{'n','h','p','y','o'}
s5 = set({12,3,4,4,55,7})
print(s5)
s6 = set()
print(s6)
```

* 如果创建一个空集合，不可以直接用``s = {}``，会输出成字典



---

## 集合的相关操作

* 集合元素的判断操作
  * in或not in
* 集合元素的新增操作
  * 调用`add()`方法，一次添加一个元素
  * 调用`update()`方法至少添加一个元素
* 集合元素的删除操作
  * 调用`remove()`方法，一次删除一个指定元素，如果指定的元素不存在抛出`KeyError`
  * 调用`discard()`方法，一次删除一个指定元素，如果指定的元素不存在不抛出异常
  * 调用`pop()`方法，一次只删除一个任意元素
  * 调用`clear()`方法，清空集合

```python
s = {10,20,30,405,60}
#集合元素的判断操作
print(10 in s)#True
print(100 in s)#False
print(10 not in s)#False
print(100 not in s)#True

#集合元素的新增操作
s.add(80)
print(S)
s.update({200,300,400})
print(s)
s.update((78,64,56))
print(s)

#集合的删除操作
s.remove(100)
print(s)
s.remove(500)#抛出KeyError
print(s)
s.discard(500)
print(s)
s.pop()	#删除任意，没有参数的
print(s)
s.clear()
print(s)
```



---

## 集合间的关系

* 两个集合是否相等
  * 可以使用运算符`==`或`!=`进行判断
* 一个集合是否是另一个集合的子集
  * 可以调用方法`issubset`进行判断
  * B是A的子集
* 一个集合是否是另一个集合的超集
  * 可以调用方法`issuperset`进行判断
  * A是B的超集
* 两个集合是否没有交集
  * 可以调用方法`isdisjoint`进行判断

```python
s = {10,20,30,40}
s2 = {30,40,20,10}
#两个集合是否相等，元素相同就相等
print(s == s2)	#True
print(s != s2)	#False
#子集
s1 = {10,20,30,40,50,60}
s2 = {10,20,30,40}
s3 = {10,20,90}
print(s2.issubset(s1))	#True
print(s3.issubset(s1))	#False
#超集
s1 = {10,20,30,40,50,60}
s2 = {10,20,30,40}
s3 = {10,20,90}
print(s1.issuperset(s2))	#True
print(s1.issuperset(s3))	#False
#交集
s1 = {10,20,30,40,50,60}
s2 = {10,20,30,40}
s3 = {10,20,90}
print(s2.isdisjoint(s3))	#False
s4 = {100,200,300}	#True
```

* 有交集就是False，没有交集是True------理解：disjoint不相交



---

## 集合的数学操作

<img src="D:/Desktop/python/images/uTools_1680607584023.png"/>

```python
#1、
s1 = {10,20,30,40}
s2 = {20,30,40,50,60}
print(s1.intersection(s2))#intersection交集等价于&，求交集
print(s1 & s2)
#2、
s1 = {10,20,30,40}
s2 = {20,30,40,50,60}
print(s1.union(s2))
print(s1 | s2)	#union联合、并集等价于|，求并集
#3、
print(s1.difference(s2))
print(s1-s2)	#difference差异等价于-，求差集
#4、
print(s1.symmetric_difference(s2))
print(s1 ^ s2)	#symmetric_difference对称差异等价于^,求对称差集
```



---

## 集合生成式

* 用于生成集合的公式
  * {`i*i` for `i` in range(1,10)}
* 将{ }修改成[ ]就是列表生成式
* 没有元组生成式

```python
#列表生成式
lst = [i*i for i in range(10)]
print(lst)

#集合生成式
s = {i*i for i in range(10)}
print(s)


```

<img src="D:/Desktop/python/images/uTools_1680608727336.png"/>



---

## 字符串的创建与驻留机制

* 字符串

在python中字符串是基本数据类型，是一个不可变的字符序列

<img src="D:/Desktop/python/images/uTools_1680609248242.png"/>

```python
a = 'Python'
b = "Python"
c = '''Python'''
print(a,id(a))
print(b,id(b))
print(c,id(c))
```



* 字符串的驻留机制

  <img src="D:/Desktop/python/images/uTools_1680609639933.png"/>

  * 像%就不是符合标识符
  * 运行之前，像join()就需要运行之后调用这个方法
  * `a = sys.intern(b)`

* 字符串驻留机制的优缺点

  <img src="D:/Desktop/python/images/uTools_1680610116005.png"/>



---

## 字符串的常用操作

### 查询操作

| 功能     | 方法名称   | 作用                                                         |
| -------- | ---------- | ------------------------------------------------------------ |
| 查询方法 | `index()`  | 查找子串`substr`第一次出现的位置,如果查找的字串不存在时，则抛出`ValueError` |
|          | `rindex()` | 查找子串`substr`最后一次出现的位置,如果查找的字串不存在时，则抛出`ValueError` |
|          | `find()`   | 查找子串`substr`第一次出现的位置,如果查找的字串不存在时，则返回-1 |
|          | `rfind()`  | 查找子串`substr`最后一次出现的位置,如果查找的字串不存在时，则返回-1 |

* r应为rear，后方的

```python
s = 'hello,hello'
print(s.index('lo'))	#输出3
print(s.find('lo'))
print(s.rindex('lo'))	#输出9
print(s.rfind('lo'))
```

建议用`find()`方法，不会报错

### 大小写转换

| 功能       | 方法名称       | 作用                                                         |
| ---------- | -------------- | ------------------------------------------------------------ |
| 大小写转换 | `upper()`      | 把字符串中所有都转成大写字母                                 |
|            | `lower()`      | 把字符串中所有都转成小写字母                                 |
|            | `swapcase()`   | 把字符串中所有大写字母转成小子字母，把所有小写字母都转成大写字母 |
|            | `capitalize()` | 把第一个字符转换成大写，把其余字符转换成小写                 |
|            | `title()`      | 把每个单词的第一个字符转换成大写，把每个单词的剩余字符转换成小写 |

```python
s = 'hello,python'
a = s.upper()
print(a)	#HELLO,PYTHON
#转换之后会产生一个新的字符串对象，物理地址发生改变，即使值相同
b = s.lower()
print(b)
print(b == a)	#判断值，True
print(b is a)	#判断内存地址，False
```

```python
s2 = 'hello,Python'
print(s2.swapcase())

print(s2.title())
```

### 对齐操作

| 功能       | 方法名称   | 作用                                                         |
| ---------- | ---------- | ------------------------------------------------------------ |
| 字符串对齐 | `center()` | 居中对齐，第一个参数指定宽度，第二个参数指定填充符，第二个字符是可选的，默认是空格，如果设置宽度小于实际宽度则返回原字符串 |
|            | `ljust()`  | 左对齐，第一个参数指定宽度，第二个参数指定填充符，第二个字符是可选的，默认是空格，如果设置宽度小于实际宽度则返回原字符串 |
|            | `rjust()`  | 右对齐，第一个参数指定宽度，第二个参数指定填充符，第二个字符是可选的，默认是空格，如果设置宽度小于实际宽度则返回原字符串 |
|            | `zfill()`  | 右对齐，左边用0填充，该方法只接收一个参数，用于指定字符串的宽度，如果设置宽度小于实际宽度则返回原字符串 |

```python
s = 'hello,Python'
print(s.center(20，*))
#输出 ****hello,Python****
print(s.ljust(20,*))
#输出hello,Python********
print(s.ljust(10))
#输出hello,Python
print(s.ljust(20))
#输出hello,Python        (有八个空格)

print('-8910'.zfill(8))
#输出-0008910
```

### 劈分操作

| 功能         | 方法名称   | 作用                                                         |
| ------------ | ---------- | ------------------------------------------------------------ |
| 字符串的劈分 | `split()`  | 从字符串的左边开始劈分，默认的劈分字符是空格字符，返回的值都是一个列表 |
|              |            | 以通过参数`sep`指定劈分字符串的劈分符                        |
|              |            | 通过参数`maxsplit`指定劈分字符串时的最大劈分次数，在经过最大劈分之后，剩余的子串会单独做为一部分 |
|              | `rsplit()` | 从字符串的右边开始劈分，默认的劈分字符是空格字符，返回的值都是一个列表 |
|              |            | 以通过参数`sep`指定劈分字符串的劈分符                        |
|              |            | 通过参数`maxsplit`指定劈分字符串时的最大劈分次数，在经过最大劈分之后，剩余的子串会单独做为一部分 |

```python
s = 'hello world Python'
lst = s.split()
print(lst)
#输出['hello','world','Python']
s1 = 'hello|world|Python'
print(s1.split(sep='|'))
print(s1.split(sep='|',maxsplit=1))
```

### 判断

| 功能             | 方法名称         | 作用                                                         |
| ---------------- | ---------------- | ------------------------------------------------------------ |
| 判断字符串的方法 | `isidentifier()` | 判断指定的字符是不是合法的标识符                             |
|                  | `isspace()`      | 判断指定的字符串是否全部有空白字符组成（回车、换行、水平制表符） |
|                  | `isalpha()`      | 判定指定的字符串是否全部由字母组成                           |
|                  | `isdecimal()`    | 判定指定字符串是否全部由十进制的数字组成                     |
|                  | `isnumeric()`    | 判定指定的字符串是否由全部数字组成                           |
|                  | `isalnum()`      | 判定指定字符串是否全部由字母和数字组成                       |

```python
s = 'hello,python'
print(s.isidentifier())
#False

print('\t'.isspace())	#True

print('abc'.isalpha())	#True
print('张三'.isalpha())	#True
print('张三1'.isalpha())	#False

print('123'.isdecimal())	#True
print('123四'.isdecimal())	#False

print('123'.isnumeric())	#True
print('123四'.isnumeric())	#True
#除此之外还有罗马数字

print('zbc123'.isalnum)	#True
print('张三123'.isalnum)	#True

```

* 合法的标识符:字母、数字、下划线

### 替换与合并

| 功能         | 方法名称    | 作用                                                         |
| ------------ | ----------- | ------------------------------------------------------------ |
| 字符串替换   | `replace()` | 第一个参数指定被替换的子串，第二个参数指定替换子串的字符串，该方法返回替换后得到的字符串，替换前的字符串不发生变化，调用该方法是可以用过第三个参数指定最大替换次数 |
| 字符串的合并 | `join()`    | 将列表或元组的字符串合并成一个字符串                         |

```python
s = 'hello,Python'
print(s.replace('Python','Java'))
s1 = 'hello,Python,Python,Python,Python'
print(s.replace('Python','Java',2))

lst = ['hello','Python','Java']
print('|'.join(lst))
print(''.join(lst))

t = ('hello','Java','Python')
print(''.join(t))

print('*'.join('Python'))
#输出P*y*t*h*o*n

```

---

## 

## 字符串的比较操作

<img src="D:/Desktop/python/images/uTools_1680694057050.png"/>

```python
print('apple' > 'app')	#True	#True
print('apple' > 'banana')	#False
print(ord('a'),ord('b'))
print(ord('杨'))	#输出26472

print(chr(97),chr(98))
print(chr(26472))

a = b = 'Python'
print(a==b)	#True
print(b==c)	#True

print(a is b)	#True
print(a is c)	#True
```

* ==与is的区别
  * == 比较的是value
  * is 比较的是id是否相等



---

## 字符串的切片

* 字符串是不可变类型
  * 不具备增删改等操作
  * 切片操作将产生新的对象

```python
s = 'hello,Python'
s1 = s[:5]
s2 = s[6:]
s3 = '!'
newstr = s1+s3+s2

print(s1)
print(s2)
print(newstr)
```

* [`start`:`end`:`step`]



---

## 格式化字符串

* %作为占位符
  * %s 字符串
  * %i或%d 整数
  * %f 浮点数
* { }作为占位符

```python
name = '张三'
age = 20
print('我叫%s,今年%d岁' % (name,age))

print('我叫{0},今年{1}岁,真的是{0}'.format(name,age))

print(f'我叫{name},今年{age}岁')
```

```python
print('%10d' % 99)	#10表示宽度
print('%.3f' % 3.1415926)	#表示保留三位小数
print('%10.3f' % 3.1415926)
```

```python
print('{0:.3}'.format(3.1415926))	#3表示三位数字3.14
print('{0:.3f}'.format(3.1415926))	#3表示三位小数
print('{0:10.3f}'.format(3.1415926))	#3表示三位小数
```



---

## 字符串的编码转换

<img src="D:/Desktop/python/images/uTools_1680697327431.png"/>

```python
s = '天涯共此时'
print(s.encode(encoding='GBK'))	#GBK编码格式中，一个中文占两个字符
print(s.encode(encoding='UTF-8'))	#UTF-8编码格式中，一个中文占三个字符

byte = s.encode(encoding='GBK')
print(byte.decode(encoding='GNK'))
```



---

## 函数的定义与调用

* 什么是函数

  * 函数就是执行特定任和以完成特定功能的一段代码

* 为什么需要函数

  * 复用代码
  * 隐藏实现细节
  * 提高可维护性
  * 提高可读性便于调试

* 函数的创建

  * ```python
    def 函数名 ([输入参数]):
        函数体
        [return ...]
    ```

```python
def calc(a,b):
    c = a + b
    return c

result = calc(10,20)
print(result)
```

---

## 

## 函数调用的参数传递

* 函数调用的参数传递
  * 位置实参
    * 根据形参对应的位置进行实参传递
  * 关键字实参
    * 根据形参名称进行实参传递

```python
def calc(a,b):	#a,b是形式参数，简称形参，位置是在函数的定义处
    c = a+b
    return c

result = calc(10,20)	#10，20称为实际参数，简称实参，位置是在函数的调用处
print(result)

res=calc(b=10,a=20)	# =左侧的变量称为关键字参数
print(res)
```

* 形参和实参可以名称不一样
* 在函数调用过程中，进行参数的传递，如果是不可变对象，在函数的修改不会影响实参的值
* 在函数调用过程中，进行参数的传递，如果是可变对象，在函数的修改会影响实参的值

```python
def fun(arg1,arg2):
    print('arg1:',arg1)
    print('arg2:',arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1:',arg1)
    print('arg2:',arg2)
    
n1 = 11
n2 = [22,33,44]
print('n1',n1)
print('n2',n2)
fun(n1,n2)	#将位置传参，实参与形参名称可以不相同

print('n1',n1)
print('n2',n2)
#最终输出
#n1 11
#n2 [22,33,44,10]

```



---

## 函数的返回值

* 函数返回多个值时，结果为元组
* 如果函数没有返回值，【执行函数完毕之后，不需要给调用处提供数据】return可以省略不写
* 函数的返回值，如果是1个，直接返回类型

```python
#非0为True，0为False
def fun(num):
    odd = []
    even = []
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
     return odd,even

print(fun([10,29,34,23,44,53,55])
```

```python
def fun1():
    print('hello')
    #return
    
fun1()
```

```python
def fun2():
    return 'hello'

res = fun2()
print(res)
```

```python
def fun3():
	return 'hello','world'
print(fun3())
#函数在定义时，是否需要返回值，视情况而定
```



---

## 函数的参数定义

* 函数定义默认值参数
  * 函数定义时，给形参设置默认值，只有与默认值不符的时候才需要传递实参

```python
def fun(a,b = 10):
    print(a,b)
    
fun(100)
fun(20,30)	#30会替换掉10
```



* 个数可变的位置参数
  * 定义函数时，可能无法事先确定传递的位置实参的个数时，使用可变的位置参数
  * 使用*定义个数可变的位置形参
  * 结果为一个元组
* 个数可变的关键字参数
  * 定义函数时，无法事先确定传递的关键字实参的个数时，使用可变的关键字参数
  * 使用**定义个数可变的关键字形参
  * 结果为一个字典

```python
def fun(*args):
    print(args)
    #print(args[0])
    
fun(10)
fun(10,30)
fun(30,105,50)
lst = [11,33,22]
fun(*lst)	#在函数调用时，将列表中的每个元素都转换为位置实参传入
```

```python
def fun1(**args):
    print(args)
    
fun1(a=10)
fun1(a=1,b=2,c=3)
dic = {'a':111,'b':222,'c':333}
fun(**dic)
'''
def fun2(*args,*a):
	pass#报错，只能是一个

def fun2(**args,**a):
	pass
	
	
def fun2(*args,**args)
'''
```

<img src="D:/Desktop/python/images/uTools_1680785894610.png"/>

```python
def fun(a,b,*,c,d):
    print(a)
    print(b)
    print(c)
    print(d)
    
fun(10,20,c=30,d=40)
#从*之后必须要关键字传参传入参数
```



---

## 变量的作用域

* 程序代码能访问该变量的区域

* 根据变量的有效范围可分为

  * 局部变量
    * 在函数内定义并使用的变量，只在函数内部有效，局部变量使用global声明，这个变量就会变成全局变量
  * 全部变量
    * 函数体外定义的变量，可作用于函数体外

  

```python
def fun(a,b):
    c = a + b	#c是局部变量，a,b为形参，也相当于局部变量
    print(c)
    
print(a)#报错，超出作用域范围，在函数体外

name='li'
print(name)
def fun1():
    print(name)
fun1()


def fun2():
    global age
    age = 20
    print(age)
fun2()
print(age)
```



---

## 递归函数

* 什么是递归函数
  * 如果在一个函数的函数体内调用了该函数本身，这个函数就成为递归函数
* 递归的组成部分
  * 递归调用与递归终止条件
* 递归的调用过程
  * 每递归调用一次函数，都会在栈内存分配一个栈帧
  * 每执行完一次函数，都会释放相应的空间
* 递归的优缺点
  * 缺点：占用内存多，效率低下
  * 优点：思路和代码简单

```python
#计算阶层
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
    
print(fac(6))
```

## 

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
|        | 二者相辅相成，并不是对立的<br />解决复杂问题，通过面向对象方式便于我们宏观上把握事物之间的复杂关系、方便我们分析整个系统；具体到微观操作，任然使用面向过程方式来处理 |                                          |



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

## 

---

## 类属性、类方法、静态方法

* 类属性：类中方法的变量称为类属性，被该类的所有对象所共享
* 类方法：使用`@classmethod`修饰的方法，使用类名直接访问的方法
* 静态方法：使用`@staticmethod`修饰的主法，使用类名直接访问的方法

```python
print(Student.native_place)	#访问类属性
Student.cm()	#调用类方法
Student.sm()	#调用静态方法
```

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
        
#print(Student.native_place)
stu1 = Student('张三',20)
stu2 = Student('李四',30)
print(stu1.native_place)
print(stu2.native_place)
Student.native_place = '天津'	#输出如果会变
print(stu1.native_place)
print(stu2.native_place)
```



---

## 动态绑定属性和方法

* Python是动态语言，在创建对象之后，可以动态地绑定属性和方法

  ```python
  def show():
      print('我是一函数')
  stu = Student('jack',20)
  stu.gender= '男'	#动态绑定性别
  print(stu.name,stu.age,stu.gender)
  stu.show=show	#动态绑定方法
  stu.show()
  ```

  

```python
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print(self.name+'在吃饭')
        
stu1 = Student('张三',20)
stu2 = Student('李四',30)
print(id(stu1))
print(id(stu2))
print('---------为stu2动态绑定性别属性--------')
stu2.gender('男')
print(stu1.name,stu1.age)
print(stu2.name,stu2.age,stu2.gender)

print('------------------------')
stu1.eat()
stu2.eat()
def show():
    print('定义在类之外的，称为函数')
stu1.show=show
stu1.show()

#stu2.show()	#因为stu2并还没有绑定show方法

```

<img src="D:/Desktop/python/images/uTools_1681044077622.png"/>



---

## 封装的实现方式

* 面向对象的三大特征

<img src = "D:/Desktop/python/images/uTools_1681093351742.png"/>

```python
class Car:
    def __init__(self,brand):
        self.brand = brand
    def start(self):
        print('汽车已启动....')
        
        
car = Car('BMW')
car.start()
print(car.brand)
```

```python
class Student:
    def __init__(self,name,age):
        self.name = name
        self.__age = age	#年龄不希望在类的外部被使用，所以加了两个__
    def show(self):
        print(self.name,self.__age)
stu = Student('张三',20)
stu.show()	#可以输出

print(stu.name)	#可以输出
print(stu.__age)	#不可以输出
print(dir(stu))
print(stu._Student__age)	#在类的外部可以通过 _Student__age  进行访问

```



---

## 继承及其实现方式

* 语法格式

  class 子类类名(父类1，父类2):

  ​	pass

* 如果一个类没有继承任何类，则默认继承`object`

* Python支持多继承

* 定义子类时，必须在其构造函数中调用父类的构造函数

```python
class Person(object):	#person继承object类
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name,self.age)
        
class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no = stu_no
        
class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear = teachofyear
        
 

stu = Student('张三',20,'1001')
teacher = Teacher('李四',34,10)

stu.info()
teacher.info()
```

### super()

**super()函数** 用于调用父类 (超类) 的方法。当一个类继承自多个父类时，使用 super() 函数可以方便地调用先辈类 (超类) 中的同名方法，而无需指定父类的名称。

super() 函数有两个参数：子类和子类的实例。它在继承层次结构中搜索下一个类，并返回该类的实例，这样就可以在子类中调用该类的方法了。

一般来说，super() 函数可以使用两种方式，分别是：

1.  无参方式：直接使用 super() 函数即可。

```python
class A:
    def __init__(self):
        print('A.__init__')

class B(A):
    def __init__(self):
        super().__init__()
        print('B.__init__')

B()  # 输出 A.__init__ 和 B.__init__
```

2.  有参方式：需要传递两个参数，第一个参数是当前子类的类名，第二个参数是当前子类的类对象。

```python
class A:
    def __init__(self):
        print('A.__init__')

class B(A):
    def __init__(self):
        super(B, self).__init__()
        print('B.__init__')

B()  # 输出 A.__init__ 和 B.__init__
```

总的来说，super() 函数对于实现多重继承的类非常有用，可以减少代码冗余，提高代码的可读性和可维护性。



---

## 方法重写

* 如果子类对继承自父类的某个属性或方法不满意，可以在子类中对其（方法体）进行重新编写
* 子类重写后的方法中可以通过`super().***()`调用父类中被重写的方法

```python
class Person(object):	#person继承object类
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name,self.age)
        
class Student(Person):
    def __init__(self,name,age,stu_no):
        super().__init__(name,age)
        self.stu_no = stu_no
        #方法重写
        def info(self):
            super().info()
            print(self.stu_no)
        
class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super().__init__(name,age)
        self.teachofyear = teachofyear
        #方法重写
 		def info(self):
            super().info()
            print('教龄',self.teachofyear)

stu = Student('张三',20,'1001')
teacher = Teacher('李四',34,10)

stu.info()
print('---------')
teacher.info()

```



---

## object类

* object类是所有类的父类，因此所有类都有object类的属性和方法。
* 内置函数`dir()`可以查看指定对象所有属性
* Object有一个`__str__()`方法，用于返回一个对于“对象的描述”，对应于内置函数`str()`经常用于`print()`方法，帮我们查看对象的信息，所以我们经常会对`__str__()`进行重写

```python
class Student:
    #pass
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return '我的名字{0},{1}岁了'.format(self.name,self.age)

stu = Student('张三',20)
print(dir(stu))
print(stu)	#默认调用__str__()这样的方法
```



---

## 多态的实现

* 简单地说，多态就是“具有多种形态”，它指的是：即便不知道一个变量所引用的对象到底是什么类型，仍然可以通过这个变量调用方法，在运行过程中根据变量所引用对象的类型，动态决定调用哪个对象中的方法

```python
class Animal:
    def eat(self):
        print('动物会吃')
        
class Dog(Animal):
    def eat(self):
        print('狗吃骨头')
        
class Cat(Animal):
    def eat(self):
        print('猫吃鱼')
        
class Person:
    def eat(self):
        print('人吃五谷杂粮')
        
        
        
def fun(obj):
    obj.eat()
    
fun(Cat())
fun(Dog())
fun(Animal())
print('-------------')
fun(Person())
```

* 静态语言和动态语言关于多态的区别
  * 静态语言实现多态的三个必要条件
    * 继承
    * 方法重写
    * 父类引用指向子类对象
  * 动态语言的多态崇尚“鸭子类型”当看到一只鸟走起来像鸭子、游泳起来像鸭子，收起来也像鸭子，那么这只鸟就可以被称为鸭子。在鸭子类型中，不需要关心对象是什么类型，到底是不是鸭子，只关心对象的行为。



---

## 特殊方法和特殊属性

|          | 名称         | 描述                                                         |
| -------- | ------------ | ------------------------------------------------------------ |
| 特殊属性 | `__dict__()` | 获得类对象或实例对象所绑定的所有属性和方法的字典             |
| 特殊方法 | `__len__()`  | 通过重写`__len__()`方法，让内置函数`len()`的参数可以自定义类型 |
|          | `__add__()`  | 通过重写`__add__()`方法，可使用自定义对象具有“+”功能         |
|          | `__new__()`  | 用于创建对象                                                 |
|          | `__init__()` | 对创建对象进行初始化                                         |

```python
class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
class D(A):
    pass
x = C('Jack',20)	#x是C类的一个实例对象
print(x.__dict__)	#实例对象的属性字典
print(C.__dict__)
print(x.__class__)	#输出了对象所属的类
print(C.__bases__)	#C类的父类类型的元素
print(C.__base__)	#类的基类
print(C.__mro__)	#类的层次结构
print(A.__subclasses__())	#子类的列表
```



```python
a = 20
b = 100
c = a + b
d = a.__add__(b)

print(c)
print(d)

class Student:
    def __init__(self,name):
        self.name = =name
    def __add__()(self,other):
        return self.name+other.name
    def __len__()(self):
        return len(self.name)
    
    
stu1 = Student('张三')
stu2 = Student('李四')

s = stu1+stu2	#实现了两个对象的加法运算
print(s)
s = stu1.__add__(stu2)
print(s)


lst = [11,22,33,44]
print(len(lst))
print(lst.__len__())
print(len(stu1))
```

```python
class Person(object):
        
    def __new__()(cls,*args,**kwargs):
        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建的对象的id为{0}'.format(id(obj)))
        return obj
    
    def __init__(self,name,age):
        print('__init__被调用了，self的id值为{0}'.format(id(sellf)))
        self.name = name
        self.age = age
        
        
print('object这个类对象的id为{0}'.format(id(object)))
print('Person这个类对象的id为{0}'.format(id(Person)))

#创建Person类的实例对象
p1 = Person('张三',20)
print('p1这个Person类的实例对象的id{0}'.format(id(p1)))
'''
obj是self的值
'''
```



---



### `__dict()__`函数

`__dict__()`是一个Python内置函数，用于获取对象的属性字典。字典中包含了对象的所有属性和值，以键值对的形式存在。

在Python中，几乎所有的对象都有`__dict__`方法，例如模块、类、实例等。其中，模块的`__dict__`属性包含了模块中的所有全局变量和函数，而类的`__dict__`属性包含了类定义中的所有属性和方法。

通过调用`__dict__()`方法，可以获取对象的属性字典，从而方便地查看对象的属性和对其进行操作。例如，可以通过添加、删除、更新字典中的键值对来动态地修改对象的属性。

以下是一个示例，展示了如何使用`__dict__()`方法从类和实例中获取属性字典：

```python
class MyClass:
    def __init__(self):
        self.x = 10
        self.y = 20
    
    def my_func(self):
        pass

obj = MyClass()
print(MyClass.__dict__)
# 输出: {'__module__': '__main__', '__init__': <function MyClass.__init__ at 0x7fb792d7ddc0>, 'my_func': <function MyClass.my_func at 0x7fb792d7de50>, '__dict__': <attribute '__dict__' of 'MyClass' objects>, '__weakref__': <attribute '__weakref__' of 'MyClass' objects>, '__doc__': None}

print(obj.__dict__)
# 输出: {'x': 10, 'y': 20}
```

### `__len__()`函数

`__len__()`是一个Python内置函数，用于获取对象的长度或元素个数。该方法常用于容器类型对象，如列表、元组、集合、字典等。

在Python中，几乎所有的容器类型对象都实现了`__len__()`方法。当我们调用`len()`函数时，实际上是在调用对象的`__len__()`方法。

以下是一个示例，展示了如何自定义一个类并实现`__len__()`方法：

```python
class MyList:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        return len(self.items)

my_list = MyList([1, 2, 3, 4, 5])
print(len(my_list))
# 输出: 5
```

在上述示例中，我们自定义了一个`MyList`类，该类包含了一个items属性，是一个列表。在类中实现了`__len__()`方法，该方法返回了items列表的长度，即元素个数。

当我们调用`len(my_list)`时，实际上是在调用my_list对象的`__len__()`方法，该方法返回了items列表的长度，即5。

需要注意的是，如果一个对象没有实现`__len__()`方法，那么调用`len()`函数会抛出`TypeError`异常。因此，如果我们自定义了一个容器类型的对象，需要实现`__len__()`方法，以保证它的使用和内置容器类型一致。

### `__add__()`函数

`__add__()`是一个Python内置函数，用于实现对象的加法运算。该方法常用于数值类型对象、字符串、列表、元组等可迭代对象。

在Python中，如果我们对两个对象进行加法运算（即使用"+"运算符），实际上是调用了对象的`__add__()`方法。如果没有实现`__add__()`方法，那么加法运算会抛出`TypeError`异常。

以下是一个示例，展示了如何实现一个自定义的类，并实现`__add__()`方法：

```python
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        real_part = self.real + other.real
        imag_part = self.imag + other.imag
        return Complex(real_part, imag_part)

c1 = Complex(2, 3)
c2 = Complex(4, 5)

c3 = c1 + c2
print(c3.real, c3.imag)
# 输出: 6 8
```

在上述示例中，我们自定义了一个Complex类，表示复数，包含了一个实部和一个虚部。并且在类中实现了`__add__()`方法，该方法返回了两个复数的和。

当我们执行"c1 + c2"时，实际上是在调用c1对象的`__add__()`方法，并将c2作为参数传入。该方法返回了两个复数的和，即Complex(6, 8)。

需要注意的是，如果两个对象的类型不兼容，那么加法运算会抛出`TypeError`异常。因此，在实现类的`__add__()`方法时，需要针对不同情况进行判断和处理，以确保加法运算的正确性。

### `__new__()`函数

`__new__()`是Python中的一个特殊方法，是在对象创建时调用的一个静态方法。该方法会返回一个新的对象，并在对象创建时执行一些必要的初始化操作。

`__new__()`方法是在对象创建阶段执行的第一个方法，它的作用是返回一个新对象，并将该对象传递给后续的初始化方法。在Python中，`__new__()`方法一般只在特殊的情况下被使用，比如自定义一个不可变类型，或是一个需要手动控制对象创建过程的类型。

以下是一个示例，展示了如何自定义一个类并实现`__new__()`方法：

```python
class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

a = Singleton()
b = Singleton()

print(a is b)
# 输出: True
```

在上述示例中，我们自定义了一个Singleton类，该类实现了单例模式，即只允许创建一个实例。在类中实现了`__new__()`方法，该方法会在对象创建时执行并返回一个新的对象。我们使用一个类变量_instance来保存类的唯一实例，如果不存在该实例，则创建一个新实例并将其赋值给_instance变量，否则直接返回_instance变量。

当我们创建Singleton类的两个对象a和b时，实际上是获取了同一个实例。因为在调用`__new__()`时，判断_instance变量是否为空，如果为空，则创建一个新实例并将其保存在_instance变量中，否则直接返回_instance变量。因此，在该示例中，a和b实际上都是同一个实例，所以a is b的结果为True。

需要注意的是，`__new__()`方法并不常用，仅在特定情况下才会用到，并且需要慎重使用。一般来说，在定义类时，我们更多地是关注`__init__()`方法，即在对象创建完毕后进行初始化操作的方法。

### `__init__`函数

`__init__()`是Python中的一个特殊方法，用于在对象创建后进行初始化操作。该方法会在对象创建后立即调用，并接受初始化参数。一般情况下，我们都会在该方法中对对象的属性进行初始化赋值。

以下是一个示例，展示了如何在类中实现`__init__()`方法：

```python
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

point = Point(2, 3)
print(point.x, point.y)
# 输出: 2 3
```

在上述示例中，我们自定义了一个Point类，该类表示二维坐标系中的一个点，包含了x和y两个属性。在类中实现了`__init__()`方法，该方法会在对象创建后立即被调用，在该方法中针对每个实例的属性进行了初始化赋值。

当我们创建一个Point对象时，需要传入x和y两个参数，如"point = Point(2, 3)"，此时会执行Point类的`__init__()`方法，并将2和3分别赋值给对象的x和y属性。

需要注意的是，`__init__()`方法只是用于对象的初始化操作，它不会返回任何值。如果需要获取对象的返回值，可以考虑使用`__new__()`方法。

此外，如果没有显式定义`__init__()`方法，Python解释器会自动调用一个默认的`__init__()`方法，该方法不接受任何参数，也不做任何事情。而如果定义了`__init__()`方法，那么当对象创建时就会自动调用该方法进行初始化操作。



## 

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

## 

---

## 编码格式的介绍

### 编码格式

* Python的解释器使用的是Unicode(内存)

* `.py`文件在磁盘上使用的是UTF-8存储(外存)

<img src="D:/Desktop/python/images/uTools_1681348289424.png"/>

```python
#修改编码格式,在文件最初添加以下，默认utf-8
#encoding = gbk
```



---

## 文件的读写原理

* 文件的读写俗称"IO操作"

* 文件读写操作流程

  1. 打开文件：使用Python内置的open()函数打开文件，可以指定文件的路径、文件名、打开方式等参数。

  2. 读写文件：使用文件对象的read()、readline()、write()等方法读写文件内容。

  3. 关闭文件：使用文件对象的close()方法关闭文件，释放系统资源。

  以下是一个简单的Python文件读写示例：

  ```python
  # 打开文件
  file = open('test.txt', 'r')
  
  # 读取文件内容
  content = file.read()
  
  # 打印文件内容
  print(content)
  
  # 关闭文件
  file.close()
  
  # 打开文件
  file = open('test.txt', 'w')
  
  # 写入文件内容
  file.write('Hello, World!')
  
  # 关闭文件
  file.close()
  ```

  在这个示例中，首先使用open()函数打开名为test.txt的文件，并指定打开方式为'r'（只读模式），然后使用文件对象的read()方法读取文件内容，并打印出来。接着，再次打开test.txt文件，指定打开方式为'w'（写入模式），使用文件对象的write()方法向文件中写入'Hello, World!'，最后使用close()方法关闭文件。

* 操作原理

  <img src= "D:/Desktop/python/images/uTools_1681349025369.png"/>

  

​		Python文件读写的具体实现原理是：当程序调用`open()`函数打开一个文件时，操作系统会根据文件名和路径查找文件并返回一个文		件对象。文件对象包含了文件的基本信息，如文件名、文件路径、文件大小、文件打开模式等。Python程序可以使用文件对象的方		法读写文件内容。

​		当程序调用文件对象的`read()`方法读取文件内容时，操作系统会将文件内容读入内存中，并返回给程序。程序可以使用读取到的文		件内容进行后续的处理。当程序调用文件对象的`write()`方法写入文件内容时，操作系统会将写入的内容缓存到内存中，并在适当的		时候将缓存中的内容写入到文件中。

​		当程序使用完文件后，应该使用文件对象的`close()`方法关闭文件。关闭文件时，操作系统会释放文件占用的资源，包括文件句柄、		缓存等。如果程序没有显式关闭文件，操作系统会在程序执行完毕后自动关闭文件。

​		总之，Python文件读写的操作原理是通过文件对象与操作系统进行交互来实现的，程序可以使用文件对象的方法读写文件内容，操		作系统会负责将文件内容读写到内存或磁盘中，并在适当的时候释放文件占用的资源。

## 文件的读写操作

* 内置函数`open()`创建文件对象

  <img src="D:/Desktop/python/images/uTools_1681349273734.png"/>

  

* 语法规则

  <img src="D:/Desktop/python/images/uTools_1681349334889.png"/>

```python
file = open('a.txt','r')
print(file.readlines())	#读取党建放进列表
file.close()
```

## 常用的文件打开模式

* 文件的类型
  * 按文件中数据的组织形式，文件分为以下两大类
    * **文本文件**：存储的是普通“字符"文本，默认为unicode字符集，可以使用记本事程序打开
    * **二进制文件**：把数据内容用“字节"进行存储，无法用记事本打开，必须使用专用的软件打开，举例：mp3音频文件，jpg图片，doc文档等

| 打开模式 | 描述                                                         |
| -------- | ------------------------------------------------------------ |
| r        | 以只读模式打开文件，文件的指针会放在文件的开头               |
| w        | 以只写模式打开文件，如果文件不存在则创建，如果文件存在，则覆盖原有内容，文件指针在文件的开头 |
| a        | 以追加模式打开文件，如果文件不存在则创建，文件指针在开头，如果问价存在，则在文件末尾追加内容，文件指针在源文件末尾 |
| b        | 以二进制方式打开文件，不能单独使用，需要与其他模式一起使用，rb,或者wb |
| +        | 以读写方式打开文件，不能单独使用，需要与其他模式一起使用，a+ |

###

Python中常用的文件打开模式有以下几种：

- `r`：只读模式，打开文件后只能读取文件内容，不能写入或修改文件。
- `w`：只写模式，打开文件后可以写入文件内容，如果文件已存在则会清空文件内容，如果文件不存在则会创建一个新的文件。
- `a`：追加模式，打开文件后可以写入文件内容，如果文件已存在则会在文件末尾追加内容，如果文件不存在则会创建一个新的文件。
- `x`：创建模式，创建一个新的文件并打开，如果文件已存在则会报错。
- `b`：二进制模式，打开文件时以二进制方式进行读写，适用于非文本文件（如图片、音频、视频等）。
- `t`：文本模式，打开文件时以文本方式进行读写，适用于文本文件。

以下是几个文件打开模式的例子：

```python
# 只读模式，打开一个名为test.txt的文件
file = open('test.txt', 'r')

# 只写模式，打开一个名为test.txt的文件，如果文件不存在则创建一个新的文件
file = open('test.txt', 'w')

# 追加模式，打开一个名为test.txt的文件，如果文件不存在则创建一个新的文件
file = open('test.txt', 'a')

# 创建模式，创建一个新的名为test.txt的文件
file = open('test.txt', 'x')

# 二进制模式，打开一个名为test.png的图片文件
file = open('test.png', 'rb')

# 文本模式，打开一个名为test.txt的文本文件
file = open('test.txt', 'rt')
```

在以上示例中，我们使用了不同的文件打开模式来打开文件，并创建了不同类型的文件对象。需要注意的是，使用完文件后应该使用文件对象的`close()`方法关闭文件，以释放文件占用的资源。

---

## 文件对象的常用方法

<img src="D:/Desktop/python/images/uTools_1681350431326.png"/>

Python文件对象有很多常用的方法，以下是其中一些：

- `read(size=-1)`：读取文件内容，返回字符串或字节串。如果指定了`size`参数，则最多读取`size`个字符或字节，否则读取整个文件内容。示例：

  ```python
  # 读取整个文件内容
  file = open('test.txt', 'r')
  content = file.read()
  file.close()
  
  # 读取前10个字符
  file = open('test.txt', 'r')
  content = file.read(10)
  file.close()
  ```

- `readline(size=-1)`：读取文件的一行内容，返回字符串或字节串。如果指定了`size`参数，则最多读取`size`个字符或字节，否则读取整行内容。示例：

  ```python
  # 读取第一行内容
  file = open('test.txt', 'r')
  line = file.readline()
  file.close()
  
  # 读取前10个字符
  file = open('test.txt', 'r')
  line = file.readline(10)
  file.close()
  ```

- `readlines(hint=-1)`：读取文件的所有行，返回包含每行内容的字符串或字节串列表。如果指定了`hint`参数，则最多读取`hint`个字符或字节，否则读取所有行内容。示例：

  ```python
  # 读取所有行内容
  file = open('test.txt', 'r')
  lines = file.readlines()
  file.close()
  
  # 读取前100个字符
  file = open('test.txt', 'r')
  lines = file.readlines(100)
  file.close()
  ```

- `write(string)`：向文件写入字符串或字节串，返回写入的字符数或字节数。示例：

  ```python
  # 向文件写入字符串
  file = open('test.txt', 'w')
  file.write('Hello, world!')
  file.close()
  
  # 向文件写入字节串
  file = open('test.bin', 'wb')
  file.write(b'\x01\x02\x03')
  file.close()
  ```

- `writelines(lines)`：向文件写入多行内容，参数`lines`是包含每行内容的字符串或字节串列表。示例：

  ```python
  # 向文件写入多行内容
  file = open('test.txt', 'w')
  lines = ['Hello\n', 'world\n']
  file.writelines(lines)
  file.close()
  ```

- `seek(offset[, whence])`：移动文件指针到指定位置，参数`offset`是偏移量，参数`whence`是起始位置，可选值为0（文件开头）、1（当前位置）和2（文件结尾）。示例：

  ```python
  # 移动文件指针到文件开头
  file = open('test.txt', 'r')
  file.seek(0, 0)
  content = file.read()
  file.close()
  
  # 移动文件指针到文件结尾
  file = open('test.txt', 'a')
  file.seek(0, 2)
  file.write('Hello, world!')
  file.close()
  ```

- `tell()`：返回当前文件指针的位置。示例：

  ```python
  # 获取当前文件指针的位置
  file = open('test.txt', 'r')
  content = file.read()
  pos = file.tell()
  file.close()
  ```

以上是Python文件对象的一些常用方法及示例，可以根据实际需求选择合适的方法进行文件读写操作。



---

## with语句

* with语句可以自动管理上下文资源，不论什么原因跳出with块都能确保文件正确的关闭，以此来达到释放资源的目的

<img src="D:/Desktop/python/images/uTools_1681372191817.png"/>

```python
with open('a.txt','r') as file:
    print(file.read())
    #不用手动close()
```

Python中的with语句用于自动管理资源，例如文件操作和网络连接等。它会在语句块开始前打开资源，在语句块结束时自动关闭资源，无论是正常结束还是发生异常。这种方式确保了资源在不再需要时能够正确关闭，避免了常见的资源泄漏问题。

以下是一个简单的例子，展示如何使用with语句来打开和关闭文件：

```python
with open('example.txt', 'r') as f:
    data = f.read()
    print(data)
```

在这个例子中，我们使用`open`函数打开一个名为`example.txt`的文件。使用`with`语句，我们将文件对象赋值给变量`f`。在语句块中，我们可以使用`f`对象读取文件内容并打印它。当语句块结束时，Python会自动关闭文件，释放资源。

在实际应用中，with语句可以用于许多不同的资源管理场景，例如数据库连接、网络连接、线程锁等。无论是什么资源，使用with语句都可以确保资源在不再需要时被正确关闭和释放。

### 上下文管理器

Python的上下文管理器是一种实现了`__enter__`和`__exit__`方法的对象，用于管理代码块的执行上下文。上下文管理器可以确保资源在代码块执行结束时被正确地关闭或清理。

当一个对象被作为上下文管理器使用时，它的`__enter__`方法会在代码块执行前被调用，`__exit__`方法会在代码块执行结束后被调用。在执行代码块期间，上下文管理器可以执行一些初始化或清理操作，例如打开和关闭文件、获取和释放锁等。

下面是一个简单的例子，展示如何使用上下文管理器来管理文件操作：

```python
class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with File('example.txt', 'r') as f:
    data = f.read()
    print(data)
```

在这个例子中，我们定义了一个名为`File`的类，它实现了上下文管理器的`__enter__`和`__exit__`方法。在`__enter__`方法中，我们打开文件并返回文件对象。在`__exit__`方法中，我们关闭文件。使用`with`语句，我们将文件对象赋值给变量`f`，在语句块中使用它来读取文件内容并打印它。当语句块结束时，Python会自动调用`__exit__`方法关闭文件。

除了使用类来实现上下文管理器外，Python还提供了`contextlib`模块，它包含了一些用于创建上下文管理器的实用函数和装饰器。使用`contextlib`模块，我们可以更方便地创建和使用上下文管理器。



---

## os模块的常用函数

* os模块是Python内置的与操作系统功能和文件系统相关的模块，该模块中的语句的执行结果通常与操作系统有关，在不同的操作系统上运行，得到的结果可能不一样。
* os模块与os.path模块用于对目录或文件进行操作

```python
import os
os.system('notepad.exe')
os.system('calc.exe')
#直接调用可执行文件
os.startfile('文件路径\\**.exe')	#双反斜杠，转义\
```

| 函数名                            | 描述                               |
| --------------------------------- | ---------------------------------- |
| **`os.getcwd()`**                 | 获取当前工作目录                   |
| **`os.chdir(path)`**              | 设置当前工作目录为指定路径         |
| **`os.listdir(path)`**            | 返回指定路径下的文件和目录列表     |
| **`os.mkdir(path)`**              | 创建一个新目录                     |
| **`os.makedirs(path)`**           | 递归创建一个新目录                 |
| **`os.rmdir(path)`**              | 删除指定目录（只能删除空目录）     |
| **`os.removedirs(path)`**         | 递归删除指定目录及其所有子目录     |
| `os.rename(src, dst)`             | 将文件或目录从src重命名为dst       |
| `os.remove(path)`                 | 删除指定文件                       |
| `os.path.abspath(path)`           | 返回指定路径的绝对路径             |
| `os.path.basename(path)`          | 返回指定路径的文件名或目录名       |
| `os.path.dirname(path)`           | 返回指定路径的父目录               |
| `os.path.exists(path)`            | 判断指定路径是否存在               |
| `os.path.isfile(path)`            | 判断指定路径是否为文件             |
| `os.path.isdir(path)`             | 判断指定路径是否为目录             |
| `os.path.join(path1, path2, ...)` | 将多个路径组合成一个新路径         |
| `os.path.split(path)`             | 将指定路径分割成目录和文件名两部分 |

以上是一些常用的os模块操作目录相关函数及其描述。可以使用这些函数来管理和操作文件和目录。

以下是常见的一些Python中的os模块操作目录相关函数及其例子：

1. `os.getcwd()`：获取当前工作目录

```python
import os

current_dir = os.getcwd()
print("当前工作目录：", current_dir)
```

2. `os.chdir(path)`：设置当前工作目录为指定路径

```python
import os

os.chdir('/Users/username/Desktop')
print("当前工作目录：", os.getcwd())
```

3. `os.listdir(path)`：返回指定路径下的文件和目录列表

```python
import os

dir_list = os.listdir('/Users/username/Desktop')
for item in dir_list:
    print(item)
```

4. `os.mkdir(path)`：创建一个新目录

```python
import os

os.mkdir('/Users/username/Desktop/NewFolder')
```

5. `os.rmdir(path)`：删除指定目录（只能删除空目录）

```python
import os

os.rmdir('/Users/username/Desktop/NewFolder')
```

6. `os.rename(src, dst)`：将文件或目录从src重命名为dst

```python
import os

os.rename('/Users/username/Desktop/old_name.txt', '/Users/username/Desktop/new_name.txt')
```

7. `os.remove(path)`：删除指定文件

```python
import os

os.remove('/Users/username/Desktop/test.txt')
```

8. `os.path.abspath(path)`：返回指定路径的绝对路径

```python
import os

absolute_path = os.path.abspath('test.txt')
print(absolute_path)
```

9. `os.path.exists(path)`：判断指定路径是否存在

```python
import os

path = '/Users/username/Desktop/test.txt'
if os.path.exists(path):
    print("文件存在")
else:
    print("文件不存在")
```

以上是一些常用的os模块操作目录相关函数的例子。这些函数可以帮助我们管理和操作文件和目录。



---

## path模块操作目录相关函数

| 函数名                             | 描述                               | 示例                                                         |
| ---------------------------------- | ---------------------------------- | ------------------------------------------------------------ |
| **`path.join(path1, path2, ...)`** | 将多个路径组合成一个新路径         | `os.path.join('/Users', 'username', 'Desktop')` 返回 `/Users/username/Desktop` |
| **`path.abspath(path)`**           | 返回指定路径的绝对路径             | `os.path.abspath('test.txt')` 返回 `/Users/username/Desktop/test.txt` |
| **`path.basename(path)`**          | 返回指定路径的文件名或目录名       | `os.path.basename('/Users/username/Desktop/test.txt')` 返回 `test.txt` |
| **`path.dirname(path)`**           | 返回指定路径的父目录               | `os.path.dirname('/Users/username/Desktop/test.txt')` 返回 `/Users/username/Desktop` |
| **`path.exists(path)`**            | 判断指定路径是否存在               | `os.path.exists('/Users/username/Desktop/test.txt')` 返回 `True` 或 `False` |
| `path.isfile(path)`                | 判断指定路径是否为文件             | `os.path.isfile('/Users/username/Desktop/test.txt')` 返回 `True` 或 `False` |
| **`path.isdir(path)`**             | 判断指定路径是否为目录             | `os.path.isdir('/Users/username/Desktop')` 返回 `True` 或 `False` |
| **`path.split(path)`**             | 将指定路径分割成目录和文件名两部分 | `os.path.split('/Users/username/Desktop/test.txt')` 返回 `('/Users/username/Desktop', 'test.txt')` |

以上是Python中path模块操作目录相关函数的详细说明以及示例。这些函数可以帮助我们更好地操作和管理文件和目录。



### 课堂案例-列出指定目录下的`.py`文件

```python
import os
path = os.getcwd()
lst = os.listdir(path)
for filename in lst:	#获取所有.py文件
    if  filename.endswith('.py'):
		print(filename)
```

### 补充-os.walk()

`os.walk()`是Python中的一个函数，用于遍历一个目录及其子目录中的所有文件和文件夹。它返回一个生成器对象，可以迭代获得当前目录、子目录和文件的路径信息。

以下是`os.walk()`函数的语法：

```python
for root, dirs, files in os.walk(top, topdown=True, onerror=None, followlinks=False):	#得到一个元组
    # 处理当前目录的代码
    for name in dirs:
        # 处理当前目录中的子目录的代码
    for name in files:
        # 处理当前目录中的文件的代码
```

- `top`：需要遍历的目录路径。
- `topdown`：遍历的顺序，默认为从上到下。
- `onerror`：遍历出错时的处理方式，默认为抛出异常。
- `followlinks`：是否遍历符号链接指向的路径，默认为不遍历。

以下是一个使用`os.walk()`遍历目录的示例：

```python
import os

root_path = '/Users/username/Desktop'
for root, dirs, files in os.walk(root_path):
    # 打印当前目录路径
    print('当前目录：', root)
    # 打印当前目录中的子目录名
    print('子目录：', dirs)
    # 打印当前目录中的文件名
    print('文件：', files)
```

以上代码会遍历`/Users/username/Desktop`目录及其子目录中的所有文件和文件夹，并打印它们的路径信息。













