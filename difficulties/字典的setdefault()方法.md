## 字典的`setdefault()`方法

在Python中，`setdefault()`是字典对象的一个方法，用于获取指定键的值。如果键存在于字典中，则返回对应的值；如果键不存在，则插入指定键和默认值，并返回默认值。

`setdefault()`方法的语法如下：

`dict.setdefault(key, default_value)`
其中，key是要检查的键，default_value是键不存在时要设置的默认值。

下面是一个示例，演示了`setdefault()`方法的用法：

```
# 创建一个字典

student_scores = {'Alice': 85, 'Bob': 91, 'Chris': 78}

# 获取键的值

alice_score = student_scores.setdefault('Alice', 0)
print(alice_score)  # 输出：85

# 键不存在时设置默认值

john_score = student_scores.setdefault('John', 0)
print(john_score)  # 输出：0

print(student_scores)  # 输出：{'Alice': 85, 'Bob': 91, 'Chris': 78, 'John': 0}
```


在上面的示例中，student_scores字典已经包含了键值对 'Alice': 85'。当我们使用`setdefault()`方法获取'Alice'键时，方法返回键的现有值，即85。然后，我们使用`setdefault()`方法获取'John'键，由于该键在字典中不存在，方法会插入'John'键，并将0作为默认值返回。最后，我们打印出整个student_scores字典，包含了新插入的'John'键。