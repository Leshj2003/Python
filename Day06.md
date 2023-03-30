## Day06

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

