## 反向迭代`reversed()`

```py
items = [0,1,2,3,4,5,6]
temp_c = items[-5:-2]
print(temp_c)
```

* 切片为负数的时候一定要注意是从小到大，并且数清楚索引位置

---



reversed()是Python的一个内置函数，用于对序列进行反向迭代。它返回一个反向迭代器，可以逐个获取序列中的元素。

reversed()函数可以用于字符串、列表、元组等可迭代对象。它不会修改原始序列，只是返回一个反向的迭代器对象。

使用reversed()函数的语法如下：
```python
reversed(sequence)
```
其中，sequence表示要进行反向迭代的序列。

下面是一些使用reversed()函数的示例：
```python
# 反向迭代字符串
string = "Hello"
for char in reversed(string):
    print(char)  # 输出：o l l e H

# 反向迭代列表
numbers = [1, 2, 3, 4, 5]
for num in reversed(numbers):
    print(num)  # 输出：5 4 3 2 1

# 反向迭代元组
my_tuple = (1, 2, 3, 4, 5)
for item in reversed(my_tuple):
    print(item)  # 输出：5 4 3 2 1
```

需要注意的是，reversed()函数返回的是一个反向迭代器对象，如果需要将其转换为列表或其他类型的序列，可以使用list()函数进行转换。例如：
```python
numbers = [1, 2, 3, 4, 5]
reversed_numbers = reversed(numbers)
reversed_list = list(reversed_numbers)  # 将反向迭代器转换为列表
print(reversed_list)  # 输出：[5, 4, 3, 2, 1]
```