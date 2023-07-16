# python 中 if 的用法(if else, if not, elif)

**if语句实际上是：if True: …执行后面的语句**
 python 中的 if 有下面几种常见用法：
 if … else…
 if …elif…else…
 if not …
 if … not …

## 1.if … else …

```python
a = 1
if a == 1:
    print('true')
else:
    print('false')
    
# true
```


 实际上，还可以用用下面这种方式，**使代码更精简**：

```python
a = 1
print('true') if a == 1 else print('false')
# true
```


 赋值也是可以的：

```python
11 = 1
12 = 2
a = 11 if 11 is None else 12
print(a)
# 2
```

 

## 2. if … elif … else…

elif 是多条件判断语句，比如：

```python
a = 0
b = 10
c = 20
x = 15
if a < x < b:
    print('a < x < b')
elif b < x < c:
    print('b < x < c')
else:
    print('false')
    
# b < x < c
```


 当然，当条件很多时，可以有多个elif，比如上面这个简单的例子可以再增加几个条件

```python
if x < a:
    print('x < a')
elif a < x < b:
    print('a < x < b')
elif b < x < c:
    print('b < x < c')
elif x > c:
    print('x > c')
else:
    print('false')
    
# b < x < c
```

 

## 3.if not …

i在讲 if not 之前，得先弄清楚 not 在python中的意思：
 **not 是一个逻辑判断词**

```python
not True
# False
not False
# True
```


 当 not 与变量连用的时候：

```python
a = []
not a
# True
a = {}
not a
# True
a = ()
not a
# True
a = ''
not a
# True
a = None
not a
# True
a = False
not a
# True
a = True
not a
# False
a = [1]
not a
# False
```


 所以，**在python中，None, False, 空字符串 ‘’ ， 0， 空列表[]， 空字典{}， 空元组() 都相当于False。**

**要注意的是，虽然”0“是 False，但是 ”[0]" 是True** ，因为只有**空**列表为False，字典也是如此，**另外有空格的字符串 ’ ’ 也不算空字符串。**

```python
a = 0
not a
# True
a = [0]
not a
# False
a = {0}
not a
# False
a = (0)
not a
# True
```


 仔细的同学可能看到上面元组（0）并不是True，那是因为在**写元组tupple时，如果只有一个元素，需要在元素后面加上逗号，\**比如：（0,)，指定为元组类型，如果不加逗号，python会把它当成\**整型**，整数 0 为False，所以（0）也为False。

```python
a = (0,)
not a
# False
```


 弄清楚not之后，加上 if 就很简单了，如果if not 后面的语句是False，则执行冒号后面的语句，否则执行else（如果有else的话）。

```python
11 = 1
12 = None
if not 11:
    print(12)
if not 12:
    print(11)
    
# 1
```


 **注意**：有时候if not 的语句很长，又夹带is、and、or，容易理解错误，比如：

- if not x is a:

应该理解为if not (x is a) ,而不是if (not x) is a

- if not x or a =b:

应该理解为if (not x) or (ab),而不是 if not (x or ab)，当然这里a==b可以换成其他条件。or 换成and也是一样，也就是说，（and、or）和is不一样，要仔细甄别。
 if not语句是非常常用的语句，尤其在数据结构中。由于python语言的简洁，if not 和and. or. is.连用可以减少大量的代码空间。

## 4. if … not…

这种情况一般 not 与 is 连用，is not 直接按字面理解即可。理解为 if x (is not) None，而不是if x is (not None)。

```python
x = []
x is not None
# True
a = None
a is not None
# False
```

 

------

补充：
 在实际写代码的时候，经常遇到要判断None的情况，可能会遇见下面这些写法：
 if x is None:…#最好使用这种写法
 if not x:…
 if not x is None: …

而在判断None的过程，常常伴随着 [] 的判断，这时我们使用if not x是有问题的：

```python
a = None
b = {}
c = []
not a
# True
not b
# True
not c
# True
```


 因为上面讲过，not是逻辑判断，而列表、空字典等的逻辑和None是一样的，都是False，if not 是没办法区分的，输出的都是True。所以要确定变量=[]时对if not 的判断没有影响，否则会报错。

使用 if not x is None也是有问题的，这种写法容易误解为if (not x) is None，而实际上应该理解为 not (a is None)

```python
a = []
not a is None
# True
not(a is None)
# True
```


 a is None 返回False ，所以not(False)返回True，而实际上[] 并不是None，应该返回False

所以最好直接使用if x is None，简介明了。

```python
a = []
x = None
a is None
# False
x is None
# True
```


 a is b比较的a 和 b的id，只有a,b的id相同才会输出True:

```python
a = 1
b =      1
a is b
# True
id(a)
# 2000379707632
id(b)
# 2000379707632
```


 上面if … not …中的 is not其实是一样的道理