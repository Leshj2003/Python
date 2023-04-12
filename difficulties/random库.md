## random库

Python中的random模块提供了生成随机数的函数，包括生成伪随机数、随机打乱序列、从序列中随机选择元素等。

常用的函数有：

1. random()：生成一个[0,1)之间的随机浮点数。

2. randint(a, b)：生成一个[a,b]之间的随机整数。

3. uniform(a, b)：生成一个[a,b]之间的随机浮点数。

4. choice(seq)：从序列seq中随机选择一个元素。

5. shuffle(seq)：将序列seq中的元素随机打乱。

6. sample(seq, k)：从序列seq中随机选择k个不重复的元素。

7. randrange([start], stop[, step])：从指定范围内随机选择一个数，step为步长。

此外，为了保证随机数的可重复性，random模块还提供了seed()函数，可以通过指定种子来初始化随机数生成器。

例如：

```python
import random

# 生成一个0-1之间的随机浮点数
print(random.random())

# 生成一个1-10之间的随机整数
print(random.randint(1, 10))

# 生成一个1-10之间的随机浮点数
print(random.uniform(1, 10))

# 从列表中随机选择一个元素
print(random.choice([1, 2, 3, 4, 5]))

# 将列表中的元素随机打乱
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print(lst)

# 从列表中随机选择两个不重复的元素
print(random.sample([1, 2, 3, 4, 5], 2))

# 生成一个0-10之间的随机偶数
print(random.randrange(0, 11, 2))

# 初始化随机数生成器的种子
random.seed(123)
print(random.random())

# 重新初始化随机数生成器的种子
random.seed(456)
print(random.random())
```

输出结果：

```python
0.3098327317161283
3
7.841868403618782
2
[2, 1, 5, 4, 3]
[1, 5]
6
0.052363598850944326
0.2660297586120167
```



---

### choice()函数

在Python中，choice()是一个内置函数，用于从一个序列中随机选择一个元素。它的语法如下：

```python
import random

random.choice(sequence)
```

其中，sequence是要选择元素的序列，可以是列表、元组、字符串等。

下面是一个例子，展示如何使用choice()函数从一个列表中随机选择一个元素：

```python
import random

fruits = ['apple', 'banana', 'orange', 'grape', 'kiwi']

random_fruit = random.choice(fruits)

print(random_fruit)
```

输出结果可能是：

```python
kiwi
```



---

### shuffle()函数

在Python中，shuffle()是一个内置函数，用于将一个序列中的元素随机排序。它的语法如下：

```python
import random

random.shuffle(sequence)
```

其中，sequence是要随机排序的序列，可以是列表、元组等。注意，shuffle()函数会修改原序列，因此在使用时应该先创建一个副本，以免影响原序列。

下面是一个例子，展示如何使用shuffle()函数将一个列表中的元素随机排序：

```python
import random

fruits = ['apple', 'banana', 'orange', 'grape', 'kiwi']

random.shuffle(fruits)

print(fruits)
```

输出结果可能是：

```python
['orange', 'kiwi', 'banana', 'grape', 'apple']
```