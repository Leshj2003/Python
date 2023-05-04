## `enumerate()`

`enumerate()` 是 Python 内置函数，用于将一个可迭代对象（如列表、字符串、元组等）组合为一个索引序列，同时返回索引和对应的元素值。

语法：
```python
enumerate(iterable, start=0)
```

参数：
- `iterable`：要进行枚举的可迭代对象，例如列表、字符串、元组等。
- `start`（可选）：指定索引的起始值，默认为 0。

返回值：
`enumerate()` 函数返回一个迭代器对象，每次迭代返回一个包含索引和对应元素值的元组。

例子：
```python
fruits = ['apple', 'banana', 'orange']

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

输出：
```
0 apple
1 banana
2 orange
```

在上述例子中，`enumerate()` 函数遍历列表 `fruits` 并返回每个元素的索引和值。通过使用 `for` 循环遍历迭代器对象，可以分别获取索引和元素值，并打印出来。

在上面给出的代码中，`enumerate()` 函数被用于遍历 `names` 和 `courses` 列表，同时获取每个元素的索引和值，用于在嵌套循环中访问 `scores` 列表的特定位置。

---

```python
names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
# 录入五个学生三门课程的成绩
# 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
# scores = [[None] * len(courses)] * len(names)
scores = [[None] * len(courses) for _ in range(len(names))]
for row, name in enumerate(names):
    for col, course in enumerate(courses):
        scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
        print(scores)
```

逐行解释以下代码：

1. `names = ['关羽', '张飞', '赵云', '马超', '黄忠']`：创建一个包含五个学生姓名的列表。

2. `courses = ['语文', '数学', '英语']`：创建一个包含三门课程名称的列表。

3. `scores = [[None] * len(courses) for _ in range(len(names))]`：使用列表推导式生成一个嵌套列表 `scores`，其中每个元素都被初始化为 `None`。这样创建了一个五行三列的二维列表，用于存储学生的成绩。

4. `for row, name in enumerate(names):`：使用 `enumerate()` 函数遍历 `names` 列表，同时获取索引和对应的值。`row` 变量表示行号，`name` 变量表示学生姓名。

5. `for col, course in enumerate(courses):`：使用 `enumerate()` 函数遍历 `courses` 列表，同时获取索引和对应的值。`col` 变量表示列号，`course` 变量表示课程名称。

6. `scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))`：通过用户输入获取学生的成绩，并将其转换为浮点数类型，然后将成绩赋值给 `scores` 列表中对应的位置，即第 `row` 行、第 `col` 列的位置。

7. `print(scores)`：打印当前的 `scores` 列表，显示更新后的成绩。

通过以上代码，逐行遍历 `names` 和 `courses` 列表的所有组合，让用户输入对应学生和课程的成绩，并将成绩保存在 `scores` 列表中的相应位置。最后，打印出更新后的成绩列表。

执行以上代码会根据用户的输入逐步录入五个学生三门课程的成绩，并输出当前录入的成绩情况。

具体输出的内容取决于用户输入的成绩，但是以下是一个可能的输出示例：

输入：
```python
请输入关羽的语文成绩: 80
[[80.0, None, None], [None, None, None], [None, None, None], [None, None, None], [None, None, None]]

请输入关羽的数学成绩: 85
[[80.0, 85.0, None], [None, None, None], [None, None, None], [None, None, None], [None, None, None]]

请输入关羽的英语成绩: 90
[[80.0, 85.0, 90.0], [None, None, None], [None, None, None], [None, None, None], [None, None, None]]

请输入张飞的语文成绩: 75
[[80.0, 85.0, 90.0], [75.0, None, None], [None, None, None], [None, None, None], [None, None, None]]

请输入张飞的数学成绩: 70
[[80.0, 85.0, 90.0], [75.0, 70.0, None], [None, None, None], [None, None, None], [None, None, None]]

...
```

以上输出示例展示了部分录入过程中的成绩情况，每次输入一个学生的一门课程成绩后，会更新相应的成绩记录在`scores`列表中。