# Day05

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



